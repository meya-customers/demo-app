import fs from "fs"
import path from "path"
import createStyledComponentsTransformer from "typescript-plugin-styled-components"
import webpack from "webpack"
import { BundleAnalyzerPlugin } from "webpack-bundle-analyzer"
import yaml from "yaml"

function readConnectContext() {
    return yaml.parse(fs.readFileSync(".meya/connect.yaml", "utf-8"))
}

const connectContext = readConnectContext()

// Flatten the extra React module introduced by `yarn link`
// See https://github.com/facebook/react/issues/14257
const reactAlias = { react: require.resolve("react") }

const config: webpack.Configuration = {
    mode: "production",
    entry: "./main.tsx",
    module: {
        rules: [
            {
                test: /\.tsx?$/,
                loader: "ts-loader",
                exclude: /node_modules/,
                options: {
                    getCustomTransformers: () => ({
                        before: [createStyledComponentsTransformer()],
                    }),
                },
            },
        ],
    },
    resolve: {
        alias: reactAlias,
        extensions: [".tsx", ".ts", ".js"],
    },
    plugins: [
        new webpack.EnvironmentPlugin({
            MEYA_GRID_URL: connectContext.grid_url,
            APP_ID: connectContext.app_id,
        }),
        new BundleAnalyzerPlugin({
            analyzerMode:
                process.env["ANALYZE"] === "Y" ? "server" : "disabled",
        }),
    ],
    output: {
        filename: "bundle.js",
        path: path.resolve(__dirname),
    },
}

export default config
