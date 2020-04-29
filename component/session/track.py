import datetime

from dataclasses import dataclass
from meya.component.element import Component
from meya.entry import Entry
from typing import List


@dataclass
class TrackComponent(Component):
    async def start(self) -> List[Entry]:
        if not self.user.visits:
            self.user.visits = {"first": self.now(), "last": self.now()}
        else:
            self.user.visits["last"] = self.now()
        return self.respond()

    @staticmethod
    def now():
        return "{0:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.now())
