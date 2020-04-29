from dataclasses import dataclass
from meya.component.element import Component
from meya.component.spec import ComponentSpec
from meya.element.field import element_field
from meya.entry import Entry
from typing import List


@dataclass
class ControlIfEvenComponent(Component):
    if_even: int = element_field(signature=True)
    then: ComponentSpec = element_field()
    else_: ComponentSpec = element_field()

    async def start(self) -> List[Entry]:
        if self.if_even % 2 == 0:
            return self.flow_control_action(self.then)
        else:
            return self.flow_control_action(self.else_)
