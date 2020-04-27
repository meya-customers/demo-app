import { ThemeValue } from "@meya-ai/meya-orb"
import { renderOrb } from "@meya-ai/meya-orb"
import React from "react"

function main() {
    if (new URLSearchParams(window.location.search).get("embed") === "false") {
        const mount = document.querySelector("#orb-mount") as HTMLDivElement
        mount.remove()
    }
    renderOrb({
        connectionOptions: {
            gridUrl: process.env.MEYA_GRID_URL as string,
            appId: process.env.APP_ID as string,
            integrationId: "demo.integration.orb",
        },
        theme: {
            ...ThemeValue,
            brandColor: "#4989ea",
            botAvatarMonogram: "D",
        },
        container: document.querySelector("#orb-mount"),
        windowFunctions: true,
    })
}

main()
