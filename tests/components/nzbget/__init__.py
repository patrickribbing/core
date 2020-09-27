"""Tests for the NZBGet integration."""
from datetime import timedelta

from homeassistant.components.nzbget.const import DOMAIN
from homeassistant.const import (
    CONF_HOST,
    CONF_NAME,
    CONF_PASSWORD,
    CONF_PORT,
    CONF_SCAN_INTERVAL,
    CONF_SSL,
    CONF_USERNAME,
    CONF_VERIFY_SSL,
)

from tests.async_mock import patch
from tests.common import MockConfigEntry


ENTRY_CONFIG = {
    CONF_HOST: "10.10.10.30",
    CONF_NAME: "NZBGetTest",
    CONF_PASSWORD: "",
    CONF_PORT: 6789,
    CONF_SSL: False,
    CONF_USERNAME: "",
    CONF_VERIFY_SSL: False,
}

USER_INPUT = {
    CONF_HOST: "10.10.10.30",
    CONF_NAME: "NZBGet",
    CONF_PASSWORD: "",
    CONF_PORT: 6789,
    CONF_SSL: False,
    CONF_USERNAME: "",
}

YAML_CONFIG = {
    CONF_HOST: "10.10.10.30",
    CONF_NAME: "GetNZBsTest",
    CONF_PASSWORD: "",
    CONF_PORT: 6789,
    CONF_SCAN_INTERVAL: timedelta(seconds=5),
    CONF_SSL: False,
    CONF_USERNAME: "",
}

async def init_integration(
    hass,
    *,
    skip_entry_setup: bool = False,
) -> MockConfigEntry:
    """Set up the NZBGet integration in Home Assistant."""
    entry = MockConfigEntry(domain=DOMAIN, data=ENTRY_CONFIG)
    entry.add_to_hass(hass)

    if not skip_entry_setup:
        await hass.config_entries.async_setup(entry.entry_id)
        await hass.async_block_till_done()

    return entry


def _patch_async_setup(return_value=True):
    return patch(
        "homeassistant.components.nzbget.async_setup",
        return_value=return_value,
    )


def _patch_async_setup_entry(return_value=True):
    return patch(
        "homeassistant.components.nzbget.async_setup_entry",
        return_value=return_value,
    )


def _patch_history(return_value=MOCK_HISTORY):
    return patch(
        "homeassistant.components.nzbget.coordinator.NZBGetAPI.history",
        return_value=return_value,
    )


def _patch_status(return_value=MOCK_STATUS):
    return patch(
        "homeassistant.components.nzbget.coordinator.NZBGetAPI.status",
        return_value=return_value,
    )


def _patch_version(return_value=MOCK_VERSION):
    return patch(
        "homeassistant.components.nzbget.coordinator.NZBGetAPI.version",
        return_value=return_value,
    )
