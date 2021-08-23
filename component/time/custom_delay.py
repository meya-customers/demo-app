import asyncio

from dataclasses import dataclass
from meya.component.element import Component
from meya.entry import Entry
from typing import List


@dataclass
class CustomDelayComponent(Component):
    async def start(self) -> List[Entry]:
        print("CUSTOM DELAY START")
        await asyncio.sleep(10)
        print("CUSTOM DELAY END")
        return self.respond()
