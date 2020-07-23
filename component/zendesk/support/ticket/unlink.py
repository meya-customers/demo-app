from dataclasses import dataclass
from meya.component.element import Component
from meya.db.view.thread import ThreadMode
from meya.element.field import element_field
from meya.entry import Entry
from meya.zendesk.support.integration import ZendeskSupportIntegrationRef
from typing import List


@dataclass
class ZendeskSupportTicketUnlinkComponent(Component):
    integration: ZendeskSupportIntegrationRef = element_field()

    async def start(self) -> List[Entry]:
        await self.thread.unlink(integration_id=self.integration.ref)
        self.thread.mode = ThreadMode.BOT
        return self.respond()
