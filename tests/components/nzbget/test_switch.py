"""Test the NZBGet switches."""
From homeassistant.const import STATE_OFF

from . import init_integration

from tests.async_mock import patch


async def test_download_switch(hass) -> None:
    """Test the creation and values of the download switch."""
    entry = await init_integration(hass)

    registry = await hass.helpers.entity_registry.async_get_registry()

    entity_entry = registry.async_get(f"switch.nzbgettest_download")
    assert entity_entry
    assert entity_entry.unique_id == f"{entry.entry_id}_download"

    state = hass.states.get("switch.nzbgettest_download")
    assert state
    assert state.state == STATE_OFF
