from dataclasses import dataclass
from meya.component.element import Component
from meya.element.field import element_field
from meya.element.field import response_field
from meya.entry import Entry
from meya.util.enum import SimpleEnum
from typing import List


class GuessNumberResult(SimpleEnum):
    HIGH = "high"
    LOW = "low"
    CORRECT = "correct"


@dataclass
class GuessNumberComponent(Component):
    @dataclass
    class Response:
        result: GuessNumberResult = response_field()

    secret: int = element_field()
    guess: int = element_field()

    async def start(self) -> List[Entry]:
        if self.secret == self.guess:
            result = GuessNumberResult.CORRECT
        elif self.secret > self.guess:
            result = GuessNumberResult.HIGH
        else:
            result = GuessNumberResult.LOW
        return self.respond(data=self.Response(result))
