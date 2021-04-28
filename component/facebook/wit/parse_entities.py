from dataclasses import dataclass
from meya.component.element import Component
from meya.element.field import element_field
from meya.entry import Entry
from typing import List
from typing import Optional


@dataclass
class WitParseEntities(Component):
    entities: Optional[dict] = element_field(default=False)

    async def start(self) -> List[Entry]:
        if not self.entities:
            return self.respond(data={})

        return self.respond(
            data=dict(
                entities=[
                    {"name": entity["name"], "value": entity["body"]}
                    for entity in list(self.entities.values())[0]
                ]
            )
        )
