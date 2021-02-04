from dataclasses import dataclass
from meya.component.element import Component
from meya.element.field import element_field
from meya.element.field import response_field
from meya.entry import Entry
from random import randint
from typing import List


@dataclass
class GuessInitComponent(Component):
    @dataclass
    class Response:
        result: int = response_field(sensitive=True)

    sensitive: bool = element_field(default=True)
    from_: int = element_field()
    to: int = element_field()

    async def start(self) -> List[Entry]:
        secret = randint(self.from_, self.to)
        return self.respond(data=self.Response(secret))
