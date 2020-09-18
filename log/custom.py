from dataclasses import dataclass
from meya.entry import Entry
from meya.log.element import LogElement
from meya.text.event import TextEvent
from typing import List


@dataclass
class CustomLogElement(LogElement):
    async def process(self) -> List[Entry]:
        if (
            isinstance(self.entry, TextEvent)
            and "custom_log" in self.entry.text
        ):
            print(f"CUSTOM TEXT LOG: {self.entry.text}")
        return []
