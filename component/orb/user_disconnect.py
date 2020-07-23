from dataclasses import dataclass
from meya.component.element import Component
from meya.element.field import element_field
from meya.entry import Entry
from typing import List


@dataclass
class UserDisconnectComponent(Component):
    disconnect_user_id: str = element_field(signature=True)

    async def start(self) -> List[Entry]:
        await self.user.load(self.disconnect_user_id)
        self.user.orb_sessions = None
        return self.respond()
