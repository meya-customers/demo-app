import pytest

from component.text.say_upper import SayUpperComponent
from meya.element.element_test import create_component_start_entry
from meya.element.element_test import create_flow_next_entry
from meya.element.element_test import verify_process_element
from meya.text.event.say import SayEvent


@pytest.mark.asyncio
async def test_component():
    component = SayUpperComponent(say_upper="Testing!")
    component_start_entry = create_component_start_entry(component)
    say_event = SayEvent(text="TESTING!")
    flow_next_entry = create_flow_next_entry(bot_entry=component_start_entry)
    await verify_process_element(
        component, component_start_entry, [say_event, flow_next_entry]
    )
