"""Class Api resources returned from the iNels BUS."""
import logging

from pyinels.exception import ApiClassTypeException

from pyinels.const import (
    ATTR_DOWN,
    ATTR_GROUP,
    ATTR_ID,
    ATTR_READ_ONLY,
    ATTR_RELE,
    ATTR_TEMP,
    ATTR_TEMP_SET,
    ATTR_TITLE,
    ATTR_TYPE,
    ATTR_UP,
    ATTR_MIN_DISP,
    ATTR_MAX_DISP,
    ATTR_MULTIPLICATOR,
    ATTR_DECIMAL_DIGITS,
    ATTR_ADDITION,
    ATTR_UNITS,
    INELS_BUS_ATTR_DICT
)

_LOGGER = logging.getLogger(__name__)


class ApiResource:
    """Object returned from the iNels BUS."""

    @property
    def id(self):
        """Id of the object."""
        if INELS_BUS_ATTR_DICT.get(ATTR_ID) not in self.__json:
            return None
        return self.__json[INELS_BUS_ATTR_DICT.get(ATTR_ID)]

    @property
    def title(self):
        """Name of the object."""
        return self.__json[INELS_BUS_ATTR_DICT.get(ATTR_TITLE)]

    @property
    def type(self):
        """Type of the object."""
        return self.__json[INELS_BUS_ATTR_DICT.get(ATTR_TYPE)]

    @property
    def temperature(self):
        """Temperature of the object."""
        if INELS_BUS_ATTR_DICT.get(ATTR_TEMP) not in self.__json:
            return None
        return self.__json[INELS_BUS_ATTR_DICT.get(ATTR_TEMP)]

    @property
    def temperature_set(self):
        """Temperature of the object."""
        if INELS_BUS_ATTR_DICT.get(ATTR_TEMP_SET) not in self.__json:
            return None
        return self.__json[INELS_BUS_ATTR_DICT.get(ATTR_TEMP_SET)]

    @property
    def rele(self):
        """Rele of the object."""
        if INELS_BUS_ATTR_DICT.get(ATTR_RELE) not in self.__json:
            return None
        return self.__json[INELS_BUS_ATTR_DICT.get(ATTR_RELE)]

    @property
    def read_only(self):
        """Read only of the object."""
        if INELS_BUS_ATTR_DICT.get(ATTR_READ_ONLY) not in self.__json:
            return None
        return self.__json[INELS_BUS_ATTR_DICT.get(ATTR_READ_ONLY)]

    @property
    def down(self):
        """Shutter down of the object."""
        if INELS_BUS_ATTR_DICT.get(ATTR_DOWN) not in self.__json:
            return None
        return self.__json[INELS_BUS_ATTR_DICT.get(ATTR_DOWN)]

    @property
    def up(self):
        """Shutter up of the object."""
        if INELS_BUS_ATTR_DICT.get(ATTR_UP) not in self.__json:
            return None
        return self.__json[INELS_BUS_ATTR_DICT.get(ATTR_UP)]

    @property
    def group(self):
        """Group from where the object is loaded."""
        if INELS_BUS_ATTR_DICT.get(ATTR_GROUP) not in self.__json:
            return None
        return self.__json[INELS_BUS_ATTR_DICT.get(ATTR_GROUP)]

    @property
    def value(self):
        """Value of the returned object."""
        if hasattr(self, '_ApiResource__value'):
            return self.__value

        return None

    def set_value(self, value):
        self.__value = value

    def write_value(self, value):
        """Set value to the device."""

        if isinstance(value, int) or isinstance(value, float):
            value = {f'{self.id}': f'{value}'}

        self.__api.write(self, value)
        self.set_value(value)

    def __init__(self, json, api):
        """Initializer of the Api resource."""
        self.__json = json
        self.__api = api
        self.__value = None

    def get_value(self):
        """Read the current value of the device."""
        try:
            raw = None

            # shutter in action
            if self.up is not None and \
                    self.down is not None:

                raw = self.__api.read([self.up, self.down])
            else:
                raw = self.__api.read([self.id])

            self.set_value(raw)

            return self.value
        except ApiClassTypeException as ex:
            self.set_value(None)
            raise ex
        except Exception as ex:
            raise ex

        return None

    @property
    def is_available(self):
        """Device availability property."""
        value = None
        # first test when device has any value
        if (hasattr(self, '_ApiResource__value')
                and self._ApiResource__value is not None):
            return True
        else:
            # if not then try to observer
            value = self.get_value()
        # when the result is None then the device is not available
        return False if value[self.id] is None else True

    @property
    def min_display_value(self):
        """Minimal display value of the object."""
        if INELS_BUS_ATTR_DICT.get(ATTR_MIN_DISP) not in self.__json:
            return None
        return float(self.__json[INELS_BUS_ATTR_DICT.get(ATTR_MIN_DISP)])

    @property
    def max_display_value(self):
        """Maximal display value of the object."""
        if INELS_BUS_ATTR_DICT.get(ATTR_MAX_DISP) not in self.__json:
            return None
        return float(self.__json[INELS_BUS_ATTR_DICT.get(ATTR_MAX_DISP)])

    @property
    def multiplicator(self):
        """Multiplication coefficient for the value of the object."""
        if INELS_BUS_ATTR_DICT.get(ATTR_MULTIPLICATOR) not in self.__json:
            return None
        return float(self.__json[INELS_BUS_ATTR_DICT.get(ATTR_MULTIPLICATOR)])

    @property
    def decimal_digits(self):
        """Decimal digits of value of the object."""
        if INELS_BUS_ATTR_DICT.get(ATTR_DECIMAL_DIGITS) not in self.__json:
            return None
        return int(self.__json[INELS_BUS_ATTR_DICT.get(ATTR_DECIMAL_DIGITS)])

    @property
    def addition(self):
        """Addition coefficient for the value of the object."""
        if INELS_BUS_ATTR_DICT.get(ATTR_ADDITION) not in self.__json:
            return None
        return float(self.__json[INELS_BUS_ATTR_DICT.get(ATTR_ADDITION)])

    @property
    def units(self):
        """Units of the value of the object."""
        if INELS_BUS_ATTR_DICT.get(ATTR_UNITS) not in self.__json:
            return None

        return self.__json[INELS_BUS_ATTR_DICT.get(ATTR_UNITS)]
