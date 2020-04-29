from dataclasses import dataclass
from meya.button.spec import ButtonSpecUnion
from meya.component.element import Component
from meya.element.field import element_field
from meya.entry import Entry
from meya.orb.composer_spec import ComposerSpec
from meya.text.event.say import SayEvent
from typing import List
from typing import Optional


@dataclass
class SayUpperComponent(Component):
    say_upper: Optional[str] = element_field(signature=True)
    quick_replies: List[ButtonSpecUnion] = element_field(default_factory=list)
    composer: ComposerSpec = element_field(default_factory=ComposerSpec)

    async def start(self) -> List[Entry]:
        quick_replies = self.activate_button_triggers(self.quick_replies)
        say_event = SayEvent(
            composer=self.composer,
            member_id=self.member_id,
            quick_replies=quick_replies.buttons,
            text=self.say_upper.upper(),
            thread_id=self.entry.thread_id,
        )
        return self.respond(say_event, *quick_replies.triggers)
