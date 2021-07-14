from dataclasses import dataclass
from dataclasses import field
from meya.button.spec import ButtonElementSpec
from meya.component.element.interactive import InteractiveComponent
from meya.core.meta_level import MetaLevel
from meya.element.field import element_field
from meya.entry import Entry
from meya.orb import composer_spec
from meya.orb.composer_spec import ComposerFocus
from meya.tile.event.ask import TileAskEvent
from meya.tile.spec import TileButtonStyle
from meya.tile.spec import TileEventSpec
from meya.tile.spec import TileLayout
from typing import List
from typing import Optional


@dataclass
class ComposerElementSpec(composer_spec.ComposerElementSpec):
    focus: Optional[ComposerFocus] = field(default=ComposerFocus.BLUR)


@dataclass
class YesNoTileComponent(InteractiveComponent):
    text: str = element_field()
    composer: ComposerElementSpec = element_field(
        default_factory=ComposerElementSpec, level=MetaLevel.ADVANCED
    )

    async def start(self) -> List[Entry]:
        # Modeled after TileAskComponent
        buttons_specs = [
            ButtonElementSpec(text="Yes", result="Y"),
            ButtonElementSpec(text="No", result="N"),
        ]

        buttons = self.get_buttons_and_triggers(buttons_specs)
        triggers = buttons.triggers

        tiles = [TileEventSpec(buttons=buttons.buttons, title=self.text)]

        ask_tiles_event = TileAskEvent(
            button_style=TileButtonStyle.ACTION,
            layout=TileLayout.COLUMN,
            text=None,
            tiles=tiles,
        )

        return self.respond(ask_tiles_event, *triggers)
