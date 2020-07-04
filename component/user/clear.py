from dataclasses import dataclass
from meya.component.element import Component
from meya.element.field import element_field
from meya.entry import Entry
from typing import List


@dataclass
class UserClearComponent(Component):
    user_id: str = element_field()

    async def start(self) -> List[Entry]:
        await self.user.load(self.user_id)
        self.user.clear()
        return self.respond()
