from dataclasses import dataclass
from meya.bot.entry import BotEntry
from meya.element.field import process_field
from meya.entry import Entry
from meya.flow.entry.start import FlowStartEntry
from meya.integration.element import Integration
from typing import List


@dataclass
class CustomIntegration(Integration):
    entry: BotEntry = process_field()

    async def process(self) -> List[Entry]:
        if isinstance(self.entry, FlowStartEntry) and "ask" in self.entry.flow:
            self.log.info(f"Ask flow reached? {self.entry.flow}")
        return []
