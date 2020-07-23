# Google Actions Console Setup

Follow the instructions documented in the
`meya.google.actions.integration.integration.GoogleActionsIntegration` element class.

# Webhook Setup

Update the `YOUR_WEBHOOK_URL` value in the `actions.json` file and run the
following command using your `PROJECT_ID`.

```shell script
./gactions --verbose update --action_package actions.json --project PROJECT_ID
```
