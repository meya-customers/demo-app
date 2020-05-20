import pytest

from component.text.say_upper import SayUpperComponent
from meya.element.element_test import create_component_start_entry
from meya.element.element_test import create_flow_next_entry
from meya.element.element_test import verify_process_element
from meya.orb.composer_spec import ComposerEventSpec
from meya.text.event.say import SayEvent
from meya.util.generate_id import generate_member_id


@pytest.mark.asyncio
async def test_component():
    component = SayUpperComponent(say_upper="Testing!")
    component_start_entry = create_component_start_entry(component)
    say_event = SayEvent(
        composer=ComposerEventSpec(),
        member_id=generate_member_id(component_start_entry.bot_id),
        quick_replies=[],
        text="TESTING!",
        thread_id=component_start_entry.thread_id,
    )
    flow_next_entry = create_flow_next_entry(bot_entry=component_start_entry)
    await verify_process_element(
        component, component_start_entry, [say_event, flow_next_entry]
    )
