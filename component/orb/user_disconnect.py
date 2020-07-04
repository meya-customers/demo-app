from dataclasses import dataclass
from meya.component.element import Component
from meya.element.field import element_field
from meya.entry import Entry
from typing import List


@dataclass
class UserDisconnectComponent(Component):
    disconnect_member_id: str = element_field(signature=True)

    async def start(self) -> List[Entry]:
        member = await self.member_view.get_for_thread(
            self.disconnect_member_id
        )
        user = await self.user_view.load_for_integration(
            member.integration_id, member.integration_user_id
        )
        user.orb_sessions = None
        return self.respond(
            *user.changes,
            MemberLeaveEvent(
                member_id=member.member_id,
                thread_id=member.thread_id,
                integration_id=member.integration_id,
                integration_name=member.integration_name,
                integration_thread_id=member.integration_thread_id,
                integration_user_id=member.integration_user_id,
                role=member.role,
            ),
        )
