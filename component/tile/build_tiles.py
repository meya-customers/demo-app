import random

from dataclasses import dataclass
from meya.button.spec import ButtonSpec
from meya.component.element import Component
from meya.component.element import ComponentResponse
from meya.entry import Entry
from meya.tile.spec import TileCell
from meya.tile.spec import TileSpec
from typing import List


@dataclass
class BuildTilesComponent(Component):
    async def start(self) -> List[Entry]:
        flow = self.entry.data
        tile_count = flow["tile_count"]
        image = flow["image"]
        title = flow["title"]
        description = flow["description"]
        cell_row_count = flow["cell_row_count"]
        cell_count = flow["cell_count"]
        link_button_count = flow["link_button_count"]
        button_count = flow["button_count"]

        sagan_ipsum = "Circumnavigated how far away ship of the imagination star stuff harvesting star light great turbulent clouds a billion trillion"
        sagan_ipsum_words = sagan_ipsum.split(" ")
        tiles = []
        for _ in range(tile_count):
            rows = []
            for _ in range(cell_row_count):
                cells = []
                for _ in range(cell_count):
                    cells.append(
                        TileCell(
                            cell=random.choice(sagan_ipsum_words).title(),
                            value=random.choice(sagan_ipsum_words).lower(),
                        )
                    )
                rows.append(cells)
            button_offset = (
                tile_count + len(tiles) * link_button_count * button_count
            )
            buttons = []
            for _ in range(link_button_count):
                button = button_offset + len(buttons)
                buttons.append(
                    ButtonSpec(
                        text=f"Link button {button}",
                        url=f"https://cataas.com/cat/says/Link%20button%20{button}",
                    )
                )
            for _ in range(button_count):
                button = button_offset + len(buttons)
                buttons.append(
                    ButtonSpec(text=f"Button {button}", result=button)
                )
            tile = len(tiles)
            tiles.append(
                TileSpec(
                    title=f"Title {tile}" if title else None,
                    description=sagan_ipsum if description else None,
                    result=None if buttons else tile,
                    image={"url": f"https://cataas.com/cat/says/Tile%20{tile}"}
                    if image
                    else None,
                    rows=rows if rows else None,
                    buttons=buttons if buttons else None,
                )
            )
        return self.respond(data=ComponentResponse(tiles))
