from dataclasses import dataclass
from meya.component.element import Component
from meya.element.field import element_field
from meya.entry import Entry
from typing import List


@dataclass
class ThreadSetComponent(Component):
    clear: bool = element_field()
    error: bool = element_field()

    async def start(self) -> List[Entry]:
        if self.clear:
            self.thread.thread_data_1 = None
            self.thread.thread_data_2 = None
            self.thread.thread_data_3 = None
            self.thread.thread_data_4 = None
            self.thread.thread_data_5 = None
        else:
            self.thread.thread_data_1 = []
            self.thread.thread_data_2 = {}
            self.thread.thread_data_3 = {"key": None}
            self.thread.thread_data_4 = {"key1": "x", "key2": None}
            self.thread.thread_data_5 = [
                {},
                {
                    "key1": "x",
                    "key2": None,
                    "key3": [],
                    "key4": [1, None, {"key5": None, "key6": "y"}],
                },
            ]
        if self.error:
            raise Exception("ERROR")
        else:
            return self.respond()
