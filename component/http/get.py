from dataclasses import dataclass
from meya.component.element import Component
from meya.component.element import ComponentResponse
from meya.entry import Entry
from typing import List


@dataclass
class HttpGetComponent(Component):
    async def start(self) -> List[Entry]:
        response = await self.http.get("https://httpbin.org/json")
        return self.respond(data=ComponentResponse(response.data))
