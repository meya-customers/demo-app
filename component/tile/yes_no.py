from dataclasses import dataclass
from meya.button.spec import ButtonSpec
from meya.component.element import Component
from meya.element.field import element_field
from meya.entry import Entry
from meya.orb.composer_spec import ComposerEventSpec
from meya.orb.composer_spec import ComposerFocus
from meya.tile.event.ask import TileAskEvent
from meya.tile.spec import TileButtonStyle
from meya.tile.spec import TileEventSpec
from meya.tile.spec import TileLayout
from meya.util.generate_id import generate_member_id
from typing import List


@dataclass
class YesNoTileComponent(Component):
    text: str = element_field()

    async def start(self) -> List[Entry]:
        # Modeled after TileAskComponent
        buttons_specs = [
            ButtonSpec(text="Yes", result="Y"),
            ButtonSpec(text="No", result="N"),
        ]

        buttons = self.get_buttons_and_triggers(buttons_specs)
        triggers = buttons.triggers

        tiles = [TileEventSpec(buttons=buttons.buttons, title=self.text)]

        ask_tiles_event = TileAskEvent(
            button_style=TileButtonStyle.ACTION,
            composer=ComposerEventSpec(focus=ComposerFocus.BLUR),
            layout=TileLayout.COLUMN,
            member_id=generate_member_id(self.entry.bot_id),
            quick_replies=[],
            text=None,
            tiles=tiles,
            thread_id=self.entry.thread_id,
        )

        return self.respond(ask_tiles_event, *triggers)
