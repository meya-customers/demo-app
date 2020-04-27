from dataclasses import dataclass
from demo.data.data_1 import Data1
from demo.data.data_1a import Data1A
from meya.component.element import Component
from meya.element.field import response_field
from meya.entry import Entry
from typing import List


@dataclass
class Data1ComponentResponse:
    result: Data1 = response_field()


@dataclass
class Data1Component(Component):
    async def start(self) -> List[Entry]:
        data = Data1(x=4, y=Data1A(z={4.42: True, "www": None}))
        return self.respond(data=Data1ComponentResponse(data))
