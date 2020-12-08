import jwt

from dataclasses import dataclass
from meya.component.element import Component
from meya.element.field import element_field
from meya.entry import Entry
from meya.zendesk.sunshine_conversations.integration import (
    SunshineConversationsIntegration,
)
from meya.zendesk.sunshine_conversations.integration import (
    SunshineConversationsIntegrationRef,
)
from typing import List


@dataclass
class SunshineConversationsJwtComponent(Component):
    @dataclass
    class Response:
        result: str

    integration: SunshineConversationsIntegrationRef = element_field()
    external_id: str = element_field()

    async def start(self) -> List[Entry]:
        integration: SunshineConversationsIntegration = await self.resolve(
            self.integration
        )
        result = jwt.encode(
            {"scope": "appUser", "userId": self.external_id},
            integration.secret,
            algorithm="HS256",
            headers={"kid": integration.key_id},
        )
        return self.respond(data=self.Response(result))
