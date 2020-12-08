from dataclasses import dataclass
from meya.element.field import response_field
from meya.text.trigger import TextTrigger
from meya.text.trigger.trigger import TextTriggerResponse
from meya.trigger.entry.match import TriggerMatchEntry
from typing import Any
from typing import Dict
from typing import Optional


@dataclass
class FlowRoutingTrigger(TextTrigger):
    @dataclass
    class Response(TextTriggerResponse):
        flow: str = response_field()
        jump: Optional[str] = response_field()
        data: Optional[Dict[str, Any]] = response_field()

    async def match(self) -> TriggerMatchEntry:
        if not self.entry.text.startswith("routing_"):
            return self.fail()

        intents = {
            "status": ("flow.text.status", "status_ephemeral", None),
            "upper": ("flow.text.say_upper", "say", {"result": "example"}),
            "availability": ("flow.time.availability", None, None),
        }

        for intent, response in intents.items():
            if intent in self.entry.text:
                confidence = float(len(f"routing_{intent}")) / float(
                    len(self.entry.text)
                )
                flow, jump, data = response
                return self.succeed(
                    confidence=confidence,
                    data=self.Response(
                        result=self.entry.text, flow=flow, jump=jump, data=data
                    ),
                )

        return self.fail()
