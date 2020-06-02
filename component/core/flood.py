from dataclasses import dataclass
from meya.component.element import Component
from meya.element.field import element_field
from meya.entry import Entry
from meya.orb.composer_spec import ComposerEventSpec
from meya.text.event.say import SayEvent
from typing import List


@dataclass
class FloodComponent(Component):
    count: int = element_field(default=256)

    async def start(self) -> List[Entry]:
        return self.respond(
            *[
                SayEvent(
                    composer=ComposerEventSpec(),
                    member_id=self.member_id,
                    quick_replies=[],
                    text=f"Flood - {i}",
                    thread_id=self.entry.thread_id,
                )
                for i in range(self.count)
            ]
        )
