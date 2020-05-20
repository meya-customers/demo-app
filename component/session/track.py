import datetime

from dataclasses import dataclass
from meya.component.element import Component
from meya.entry import Entry
from meya.session.event.page.open import PageOpenEvent
from typing import List


@dataclass
class TrackComponent(Component):
    async def start(self) -> List[Entry]:
        if not self.user.visits:
            self.user.visits = {"first": self.now(), "last": self.now()}
        else:
            self.user.visits["last"] = self.now()
        page_open_event = PageOpenEvent.from_typed_dict(
            self.entry.data["event"], self.type_registry
        )
        self.user.page_open_url = page_open_event.url
        return self.respond()

    @staticmethod
    def now():
        return "{0:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.now())
