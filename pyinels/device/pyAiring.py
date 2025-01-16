"""Inels airing class for iNels BUS."""

from pyinels.device.pyBase import pyBase


class pyAiring(pyBase):
    """Airing class based on InelsDevice."""

    def __init__(self, device):
        """Initialize pyAiring class."""
        super().__init__(device)
