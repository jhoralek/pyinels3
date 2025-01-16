"""Unit testing of iNels switch library."""
from pyinels.const import ATTR_AIRING

from tests.const_test import (
    TEST_API_CLASS_NAMESPACE,
    TEST_API_ROOM_DEVICES,
    TEST_API_READ_DATA,
    TEST_HOST,
    TEST_PORT,
    TEST_RAW_AIRING,
    TEST_VERSION
)

from pyinels.api import Api
from pyinels.device.pyAiring import pyAiring

from unittest.mock import patch
from unittest import TestCase

AIRING_ID = "RE12_VT_equipment_room"
AIRING_NAME = "Equipment_room"

AIRING_RETURN_OFF = {AIRING_ID: 0}
AIRING_RETURN_ON = {AIRING_ID: 1}


class PyAiringTest(TestCase):
    """Class to test iNels airing library."""

    def setUp(self):
        """Setup all necesary instances and mocks."""
        self.patches = [
            patch(f'{TEST_API_CLASS_NAMESPACE}.ping', return_value=True),
            patch(f'{TEST_API_CLASS_NAMESPACE}.{TEST_API_ROOM_DEVICES}',
                  return_value=TEST_RAW_AIRING),
            patch(f'{TEST_API_CLASS_NAMESPACE}.{TEST_API_READ_DATA}',
                  return_value=AIRING_RETURN_OFF),
            patch(f'{TEST_API_CLASS_NAMESPACE}._Api__writeValues',
                  return_value=None)
        ]

        for p in self.patches:
            p.start()

        self.api = Api(TEST_HOST, TEST_PORT, TEST_VERSION)
        """Setup all neccessary async stuff."""
        airings = [device for device in self.api.getRoomDevices(
            'garage') if device.type == ATTR_AIRING]

        self.airing = pyAiring(airings[0])

    def tearDown(self):
        """Destroy all instances and mocks."""
        self.api = None
        self.airing = None
        patch.stopall()
        self.patches = None

    def test_state(self):
        """Test the state of the pyAiring."""
        s = self.airing

        s.update()
        # the airing at the beggining should be turned off
        self.assertFalse(s.state)

    def test_unique_id_and_name_presented(self):
        """Test when the unique id is presented."""
        s = self.airing

        self.assertIsNotNone(s.unique_id)
        self.assertIsNotNone(s.name)

        self.assertEqual(s.unique_id, AIRING_ID)
        self.assertEqual(s.name, AIRING_NAME)

    def test_turn_on(self):
        """Test turn on the airing."""
        s = self.airing

        s.update()
        self.assertFalse(s.state)

        with patch.object(self.api, TEST_API_READ_DATA,
                          return_value=AIRING_RETURN_ON):
            s.turn_on()

            s.update()
            self.assertTrue(s.state)

    def test_turn_off(self):
        """Test turn off the airing."""
        s = self.airing

        with patch.object(self.api, TEST_API_READ_DATA,
                          return_value=AIRING_RETURN_ON):
            s.turn_on()

            s.update()
            self.assertTrue(s.state)

        s.turn_off()

        s.update()
        self.assertFalse(s.state)
