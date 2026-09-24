import asyncio

from dataclasses import dataclass
from http import HTTPStatus
from meya.entry import Entry
from meya.integration.element import Integration
from typing import ClassVar
from typing import List


@dataclass
class ReleaseTimeoutIntegration(Integration):
    NAME: ClassVar[str] = "release_timeout"
    show_get_status: ClassVar[bool] = False

    async def rx(self) -> List[Entry]:
        try:
            delay = float(self.request.params.get("delay", "0"))
        except ValueError:
            delay = 0

        if delay not in (5.5, 6.5):
            return self.respond(
                status=HTTPStatus.BAD_REQUEST,
                data={"ok": False, "error": "delay must be 5.5 or 6.5"},
                headers={"Access-Control-Allow-Origin": "*"},
            )

        await asyncio.sleep(delay)
        return self.respond(
            status=HTTPStatus.OK,
            data={"ok": True, "delay": delay},
            headers={"Access-Control-Allow-Origin": "*"},
        )
