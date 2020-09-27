"""Define fixtures available for all tests."""
from pytest import fixture

from tests.async_mock import patch

from . Import MOCK_HISTORY, MOCK_STATUS, MOCK_VERSION


@fixture
def nzbget_history(hass):
    """Mock NZBGetApi.history for easier testing."""
    with patch("homeassistant.components.nzbget.coordinator.NZBGetAPI.history") as mock_history:
        mock_history.return_value = MOCK_HISTORY.deepcopy()
        yield mock_history


@fixture
def nzbget_status(hass):
    """Mock NZBGetApi.status for easier testing."""
    with patch("homeassistant.components.nzbget.coordinator.NZBGetAPI.status") as mock_status:
        mock_status.return_value = MOCK_STATUS.copy()
        yield mock_status


@fixture
def nzbget_version(hass):
    """Mock the NZBGetApi.version for easier testing."""
    with patch("homeassistant.components.nzbget.coordinator.NZBGetAPI.version") as mock_version:
        mock_version.return_value = MOCK_VERSIOM.copy()
        yield mock_version
