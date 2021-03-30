import argparse
import re
import sys

from yarl import URL


def main():
    parser = argparse.ArgumentParser(
        description=(
            "Edit the given text file replacing all occurrences of "
            "'grid.meya.ai', 'cdn.meya.ai' and  'app-*'."
        )
    )
    parser.add_argument(
        "--grid-url",
        dest="grid_url",
        help="The Grid URL to use e.g. 'https://grid.meya.ai'",
        required=True,
    )
    parser.add_argument(
        "--cdn-url",
        dest="cdn_url",
        help="The CDN URL to use e.g. 'https://cdn.meya.ai'",
        required=True,
    )
    parser.add_argument(
        "--app-id",
        dest="app_id",
        help="The app ID to use e.g. 'app-73c6d31d4f544a72941e21fb518b5737'",
        required=True,
    )
    parser.add_argument(
        "text_file", default=sys.stdin, type=argparse.FileType("r"), nargs="?"
    )
    args = parser.parse_args()

    grid_url = args.grid_url
    grid_domain = URL(grid_url).host
    cdn_url = args.cdn_url
    cdn_domain = URL(cdn_url).host
    app_id = args.app_id
    content = args.text_file.read()

    content = re.sub(r"grid\.meya\.ai", grid_domain, content, re.M)
    content = re.sub(r"cdn\.meya\.ai", cdn_domain, content, re.M)
    content = re.sub(
        r"appId: \"app-[a-f0-9]*\"", f'appId: "{app_id}"', content, re.M
    )

    print(content)


if __name__ == "__main__":
    main()
