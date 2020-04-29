from dataclasses import dataclass
from meya.component.element import Component
from meya.entry import Entry
from meya.log.scope import Scope
from typing import List


@dataclass
class LogComponent(Component):
    async def start(self) -> List[Entry]:
        self.log.debug("DEBUG", scope=Scope.BOT)
        self.log.info("INFO", context={"alpha": 4})
        self.log.warning("WARNING 🌕", 1, 2, 3)
        self.log.error("ERROR 🔺")
        try:
            print(1 / 0)
        except ZeroDivisionError:
            self.log.exception(scope=Scope.DEVELOPER)
        print([][0])
        return self.respond()
