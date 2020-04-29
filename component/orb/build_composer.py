from dataclasses import dataclass
from meya.component.element import Component
from meya.component.element import ComponentResponse
from meya.entry import Entry
from typing import List


@dataclass
class BuildComposerComponent(Component):
    async def start(self) -> List[Entry]:
        flow = self.entry.data
        composer = {}
        for key in ["focus", "placeholder", "visibility"]:
            if key in flow:
                composer[key] = flow[key]
        return self.respond(data=ComponentResponse(composer))
