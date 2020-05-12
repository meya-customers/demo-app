import pytest

from component.text.say_upper import SayUpperComponent
from meya.element.element_test import clone_flow_next
from meya.element.element_test import create_component_start_entry
from meya.element.element_test import verify_process_component
from meya.orb.composer_spec import ComposerSpec
from meya.text.event.say import SayEvent
from meya.util.generate_id import generate_member_id


@pytest.mark.skip(reason="TODO: needs to be fixed")
@pytest.mark.asyncio
async def test_component():
    bot_id = "b1"
    thread_id = "t1"
    component = SayUpperComponent(say_upper="Testing!")
    start_component_entry = create_component_start_entry(
        component, bot_id=bot_id, thread_id=thread_id
    )
    say_event = SayEvent(
        composer=ComposerSpec(),
        member_id=generate_member_id(bot_id),
        quick_replies=[],
        text="TESTING!",
        thread_id=thread_id,
    )
    flow_next_entry = clone_flow_next(bot_entry=start_component_entry)
    await verify_process_component(
        component=component,
        component_entry=start_component_entry,
        expected_pub_entries=[say_event, flow_next_entry],
    )
