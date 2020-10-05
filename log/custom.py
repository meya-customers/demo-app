from dataclasses import dataclass
from meya import env
from meya.entry import Entry
from meya.http.entry.response import HttpResponseEntry
from meya.log.element import LogElement
from meya.text.event import TextEvent
from typing import List
from yarl import URL


@dataclass
class CustomLogElement(LogElement):
    async def process(self) -> List[Entry]:
        if isinstance(self.entry, TextEvent) and "custom_log" in (
            self.entry.text or ""
        ):
            msg = f"CUSTOM TEXT LOG: {self.entry.text}"
            print(msg)
            self.log.info(msg)

        elif (
            isinstance(self.entry, HttpResponseEntry)
            and URL(self.entry.url).origin() == URL(env.grid_url).origin()
        ):
            request = await self.http.find_request(self.entry.request_id)
            if "custom_log" in request.params.get("text", ""):
                msg = f"CUSTOM HTTP LOG: {request.params} {self.entry.data}"
                print(msg)
                self.log.info(msg)

        return []
