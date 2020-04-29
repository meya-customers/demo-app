import pytest

from component.core.data_1 import Data1Component
from meya.element.element_test import clone_flow_next
from meya.element.element_test import create_component_start_entry
from meya.element.element_test import verify_process_component


@pytest.mark.asyncio
async def test_component():
    component = Data1Component()
    start_component_entry = create_component_start_entry(component)
    flow_next_entry = clone_flow_next(
        bot_entry=start_component_entry,
        update_data=dict(
            result={"x": 4, "y": {"z": {4.42: True, "www": None}}}
        ),
    )
    await verify_process_component(
        component=component,
        component_entry=start_component_entry,
        expected_pub_entries=[flow_next_entry],
    )
