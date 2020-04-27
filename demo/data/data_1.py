from dataclasses import dataclass
from demo.data.data_1a import Data1A


@dataclass
class Data1:
    x: int
    y: Data1A
