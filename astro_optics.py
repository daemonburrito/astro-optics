"""Optics calculations."""
import math
from lib import *

# Some concrete components

class Q70(EP):
    focal_length = 32.0
    barrel_size = 2.0


class OrionXT8(OTA):
    name = "Orion XT8"
    focal_length = 1200.0
    aperture = util.UnitConverter.inches_to_mm(8)


class EOSSensor(Sensor):
    name = "Canon EOS CMOS"

    tech = "cmos"
    width = 22.5
    height = 15
    resolution = 3504


class Canon20D(DSLR):
    name = "Canon 20D"

    def __init__(self):
        self.sensor = EOSSensor()

# Example setup

system = System()
system.camera = Canon20D()
system.ota = OrionXT8()
"""
>>> system.magnification
44.37601569801833
"""

