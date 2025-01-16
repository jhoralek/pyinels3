"""Unit testing of iNels switch library."""
from pyinels.const import ATTR_METER

from tests.const_test import (
    TEST_API_CLASS_NAMESPACE,
    TEST_API_ROOM_DEVICES,
    TEST_API_READ_DATA,
    TEST_HOST,
    TEST_PORT,
    TEST_RAW_METER,
    TEST_VERSION,
)

from pyinels.api import Api
from pyinels.device.pyMeter import pyMeter

from unittest.mock import patch
from unittest import TestCase

HUMIDITY_METER_ID = "Humidity_cellar"
HUMIDITY_METER_NAME = "Humidity cellar"
HUMIDITY_METER_UNITS = "Percentage"
HUMIDITY_METER_RETURN_VALUE = {HUMIDITY_METER_ID: 48.56}


class PyMeterTest(TestCase):
    """Class to test iNels meter library."""

    def setUp(self):
        """Setup all necesary instances and mocks."""
        self.patches = [
            patch(f'{TEST_API_CLASS_NAMESPACE}.ping', return_value=True),
            patch(f'{TEST_API_CLASS_NAMESPACE}.{TEST_API_ROOM_DEVICES}',
                  return_value=TEST_RAW_METER),
            patch(f'{TEST_API_CLASS_NAMESPACE}.{TEST_API_READ_DATA}',
                  return_value=HUMIDITY_METER_RETURN_VALUE),
        ]

        for p in self.patches:
            p.start()

        self.api = Api(TEST_HOST, TEST_PORT, TEST_VERSION)
        """Setup all neccessary async stuff."""
        meters = [device for device in self.api.getRoomDevices(
            'garage') if device.type == ATTR_METER]

        self.meter = pyMeter(meters[0])

    def tearDown(self):
        """Destroy all instances and mocks."""
        self.api = None
        self.meter = None
        patch.stopall()
        self.patches = None

    def test_unique_id_and_name_presented(self):
        """Test when the unique id is presented."""
        s = self.meter

        self.assertIsNotNone(s.unique_id)
        self.assertIsNotNone(s.name)

        self.assertEqual(s.unique_id, HUMIDITY_METER_ID)
        self.assertEqual(s.name, HUMIDITY_METER_NAME)
        self.assertEqual(s.units, HUMIDITY_METER_UNITS)
