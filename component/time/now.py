import datetime

from dataclasses import dataclass
from meya.component.element import Component
from meya.element.field import response_field
from meya.entry import Entry
from typing import List


@dataclass
class TimeNowComponent(Component):
    @dataclass
    class Response:
        result: str = response_field()

    async def start(self) -> List[Entry]:
        result = str(datetime.datetime.utcnow())
        return self.respond(data=self.Response(result=result))
