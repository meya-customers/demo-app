from dataclasses import dataclass
from demo.data.data_1 import Data1
from demo.data.data_1a import Data1A
from meya.component.element import Component
from meya.element.field import element_field
from meya.element.field import response_field
from meya.entry import Entry
from typing import List


@dataclass
class Data2ComponentResponse:
    result: Data1 = response_field()
    extra: str = response_field()


@dataclass
class Data2Component(Component):
    data_1: Data1 = element_field()

    async def start(self) -> List[Entry]:
        data = Data1(
            x=self.data_1.x + 8, y=Data1A(z={**self.data_1.y.z, "qqq": 90})
        )
        return self.respond(
            data=Data2ComponentResponse(result=data, extra="extra!")
        )
