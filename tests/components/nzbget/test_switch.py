"""Test the NZBGet switches."""
from homeassistant.components.switch.const import DOMAIN as SWITCH_DOMAIN
from homeassistant.const import (
    ATTR_ENTITY_ID,
    SERVICE_TURN_OFF,
    SERVICE_TURN_ON,
    STATE_OFF,
    STATE_ON,
)

from . import MOCK_STATUS, init_integration

from tests.async_mock import MagicMock, patch


async def test_download_switch(hass) -> None:
    """Test the creation and values of the download switch."""
    status = MagicMock(return_value=MOCK_STATUS.copy())
    entry = await init_integration(hass, status=status)
    registry = await hass.helpers.entity_registry.async_get_registry()

    entity_id = "switch.nzbgettest_download"
    entity_entry = registry.async_get(entity_id)
    assert entity_entry
    assert entity_entry.unique_id == f"{entry.entry_id}_download"

    state = hass.states.get(entity_id)
    assert state
    assert state.state == STATE_OFF

    # test downloads paused
    status.return_value["DownloadPaused"] = True

    await hass.helpers.entity_component.async_update_entity(entity_id)
    await hass.async_block_till_done()

    state = hass.states.get(entity_id)
    assert state
    assert state.state == STATE_ON


async def test_download_switch_services(hass) -> None:
    """Test download switch services."""
    await init_integration(hass)
    entity_id = "switch.nzbgettest_download"

    with patch("homeassistant.components.nzbget.coordinator.NZBGetAPI.pausedownload") as pause_mock:
        await hass.services.async_call(
            SWITCH_DOMAIN,
            SERVICE_TURN_OFF,
            {ATTR_ENTITY_ID: entity_id},
            blocking=True,
        )
        pause_mock.assert_called_once()

    with patch("homeassistant.components.nzbget.coordinator.NZBGetAPI.resumedownload") as resume_mock:
        await hass.services.async_call(
            SWITCH_DOMAIN,
            SERVICE_TURN_ON,
            {ATTR_ENTITY_ID: entity_id},
            blocking=True,
        )
        resume_mock.assert_called_once()
