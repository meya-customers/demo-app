#!/usr/bin/env bash
# Sync a snapshot of this repo (meya-ai/demo-app) to the public mirror
# (meya-customers/demo-app) on the `main` branch.
#
# Matches the historical "Snapshot" commit pattern. Copies only files tracked
# by git in the source, so .gitignore'd content (e.g. vault.secret.yaml) cannot
# leak. Paths in EXCLUDE_PREFIXES (internal CI) are kept out of the mirror.
# Stops before pushing so you can review the diff first.
#
# Usage:
#   scripts/sync-public.sh            # stage snapshot, show diff, stop
#   scripts/sync-public.sh --push     # additionally commit + push
#
# Env overrides (used by CI):
#   PUBLIC_REPO    target repo URL (may embed an auth token)
#   PUBLIC_BRANCH  target branch (default: main)
#   COMMIT_MSG     commit message (default: Snapshot)

set -euo pipefail

PUBLIC_REPO="${PUBLIC_REPO:-https://github.com/meya-customers/demo-app.git}"
PUBLIC_BRANCH="${PUBLIC_BRANCH:-main}"
COMMIT_MSG="${COMMIT_MSG:-Snapshot}"

# Tracked paths kept OUT of the public mirror (prefix match). Internal CI
# workflows reference secrets the mirror does not have, so they must not
# run there.
EXCLUDE_PREFIXES=(
  ".github/workflows/"
)

SRC="$(git -C "$(dirname "$0")/.." rev-parse --show-toplevel)"
WORK="$(mktemp -d)"
trap 'echo "Snapshot worktree left at: $WORK"' EXIT

echo "==> Cloning $PUBLIC_REPO ($PUBLIC_BRANCH) into $WORK/public"
git clone --quiet --branch "$PUBLIC_BRANCH" --depth 1 "$PUBLIC_REPO" "$WORK/public"

echo "==> Wiping tracked files in public worktree"
(
  cd "$WORK/public"
  git ls-files -z | xargs -0 rm -f
  find . -type d -empty -not -path './.git*' -delete 2>/dev/null || true
)

echo "==> Copying tracked files from $SRC (excluding: ${EXCLUDE_PREFIXES[*]})"
(
  cd "$SRC"
  git ls-files -z | while IFS= read -r -d '' f; do
    for prefix in "${EXCLUDE_PREFIXES[@]}"; do
      case "$f" in "$prefix"*) continue 2 ;; esac
    done
    mkdir -p "$WORK/public/$(dirname "$f")"
    cp "$f" "$WORK/public/$f"
  done
)

echo "==> Safety check: no secret files in snapshot"
if compgen -G "$WORK/public/vault.secret*.yaml" > /dev/null; then
  echo "ABORT: vault.secret*.yaml found in snapshot" >&2
  exit 1
fi
if [ -d "$WORK/public/.meya" ] || [ -d "$WORK/public/.claude" ]; then
  echo "ABORT: local state directory (.meya or .claude) found in snapshot" >&2
  exit 1
fi

cd "$WORK/public"
git add -A

if git diff --cached --quiet; then
  echo "==> No changes vs public repo. Nothing to do."
  exit 0
fi

echo
echo "==> Staged changes vs public $PUBLIC_BRANCH:"
git diff --cached --stat
echo
echo "Worktree: $WORK/public"
echo "Inspect:  cd $WORK/public && git diff --cached"

if [ "${1:-}" = "--push" ]; then
  echo
  echo "==> Committing and pushing to $PUBLIC_BRANCH"
  git commit -m "$COMMIT_MSG"
  git push origin "$PUBLIC_BRANCH"
  echo "==> Done."
else
  echo
  echo "Re-run with --push (or run manually) to publish:"
  echo "  cd $WORK/public && git commit -m 'Snapshot' && git push origin $PUBLIC_BRANCH"
fi
