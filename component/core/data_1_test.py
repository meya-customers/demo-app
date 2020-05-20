import pytest

from component.core.data_1 import Data1Component
from meya.element.element_test import create_component_start_entry
from meya.element.element_test import create_flow_next_entry
from meya.element.element_test import verify_process_element


def test_sanity():
    assert True


@pytest.mark.asyncio
async def test_component():
    component = Data1Component()
    component_start_entry = create_component_start_entry(component, "xxx")
    flow_next_entry = create_flow_next_entry(
        bot_entry=component_start_entry,
        data=dict(result={"x": 4, "y": {"z": {4.42: True, "www": None}}}),
    )
    await verify_process_element(
        component, component_start_entry, [flow_next_entry]
    )
