from dataclasses import dataclass
from meya.component.element.interactive import InteractiveComponent
from meya.element.field import element_field
from meya.entry import Entry
from meya.text.event.say import SayEvent
from typing import List
from typing import Optional


@dataclass
class SayUpperComponent(InteractiveComponent):
    say_upper: Optional[str] = element_field(signature=True)

    async def start(self) -> List[Entry]:
        say_event = SayEvent(text=self.say_upper.upper())
        return self.respond(say_event)
