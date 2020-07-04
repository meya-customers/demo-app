from dataclasses import dataclass
from meya.component.element.interactive import InteractiveComponent
from meya.element.field import element_field
from meya.entry import Entry
from meya.text.event.say import SayEvent
from typing import List


@dataclass
class FloodComponent(InteractiveComponent):
    count: int = element_field(default=256)

    async def start(self) -> List[Entry]:
        return self.respond(
            *[SayEvent(text=f"Flood - {i}") for i in range(self.count)]
        )
