from dataclasses import dataclass
from meya.component.element import Component
from meya.element.field import element_field
from meya.entry import Entry
from typing import List


@dataclass
class UserSetComponent(Component):
    clear: bool = element_field()
    error: bool = element_field()

    async def start(self) -> List[Entry]:
        if self.clear:
            self.user.user_data_1 = None
            self.user.user_data_2 = None
            self.user.user_data_3 = None
            self.user.user_data_4 = None
            self.user.user_data_5 = None
        else:
            self.user.user_data_1 = []
            self.user.user_data_2 = {}
            self.user.user_data_3 = {"key": None}
            self.user.user_data_4 = {"key1": "x", "key2": None}
            self.user.user_data_5 = [
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
