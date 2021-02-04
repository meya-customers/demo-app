from dataclasses import dataclass
from meya.element.field import element_field
from meya.text.trigger import TextTrigger
from meya.trigger.element import TriggerMatchResult


@dataclass
class PalindromeTrigger(TextTrigger):
    minimum: int = element_field(default=5)

    async def match(self) -> TriggerMatchResult:
        text = self.entry.text

        if len(text) >= self.minimum and text == "".join(reversed(text)):
            return self.succeed()
        else:
            return self.fail()
