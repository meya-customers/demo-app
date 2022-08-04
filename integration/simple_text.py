from dataclasses import dataclass
from http import HTTPStatus
from meya.db.view.thread import ThreadView
from meya.entry import Entry
from meya.voice.integration.integration import VoiceIntegration
from typing import ClassVar
from typing import List


@dataclass
class SimpleTextIntegration(VoiceIntegration):
    NAME: ClassVar[str] = "simple_text"

    async def rx(self) -> List[Entry]:
        integration_user_id = self.request.params.get("user_id")
        text = self.request.params.get("text")

        if not integration_user_id or not text:
            return self.respond(
                data=dict(ok=False, error="`user_id` and `text` required."),
                status=HTTPStatus.BAD_REQUEST,
            )

        await self.event_user.identify(integration_user_id)
        await self.thread.identify(
            integration_user_id,
            default_data=dict(primary_user_id=self.event_user.id),
            data=dict(voice=True),
        )

        session = await ThreadView.get(integration_user_id)
        session.simple_request_id = self.request.request_id

        event = self.get_event_from_text(
            forms=session.simple_forms or [],
            quick_replies=session.simple_quick_replies or [],
            text=text,
        )

        return [*session.changes, event]

    async def tx(self) -> List[Entry]:
        integration_user_id = await self.thread.try_reverse_lookup()
        if not integration_user_id:
            return []

        session = await ThreadView.get(integration_user_id)
        events = await self.get_thread_events(session, self.entry)

        forms = self.get_forms(events)
        if forms is not None:
            session.simple_forms = forms
        session.simple_quick_replies = self.get_quick_replies(events)

        text = self.get_text_from_events(events)

        response = self.create_response(
            request_id=session.simple_request_id,
            status=HTTPStatus.OK,
            data=dict(ok=True, text=text),
            url=self.gateway_webhook_url,
        )
        session.simple_request_id = None

        return [*session.changes, response]
