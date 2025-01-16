"""Inels meter class for iNels BUS."""

from pyinels.device.pyBase import pyBase

from pyinels.const import (
    UNITS_DICT,
    ERROR_VALUE
)


class pyMeter(pyBase):
    """Meter class based on InelsDevice."""

    def __init__(self, device):
        """Initialize object."""
        super().__init__(device)

    @property
    def value(self):
        """Value of the device."""
        val = self._device.value[self._device.id]

        if isinstance(val, str):
            return ERROR_VALUE
        else:
            val = max(val, self._device.min_display_value) \
                if self._device.min_display_value else val
            val = min(val, self._device.max_display_value) \
                if self._device.max_display_value else val
            val = val * self._device.multiplicator \
                if self._device.multiplicator else val
            val = val * self._device.addition \
                if self._device.addition else val
            val = round(val, self._device.decimal_digits) \
                if self._device.decimal_digits else val
            return val

    @property
    def units(self):
        """Units of the device."""
        if self._device.units not in UNITS_DICT:
            return None
        return UNITS_DICT.get(self._device.units)
