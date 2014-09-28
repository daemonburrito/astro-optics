import math


class OpticsBaseItem(object):
    def __unicode__(self):
        return getattr(self, 'name', '')

    def __str__(self):
        return self.__unicode__()


class OpticalSystem(object):
    focal_length = 0.0 # mm
    aperture = 0.0 # mm

    _f_ratio = 0.0

    @property
    def f_ratio(self):
        if not self._f_ratio:
            self._f_ratio = self.focal_length / self.aperture
        return self._f_ratio


class System(OpticsBaseItem, OpticalSystem):
    ota = None
    ep = None
    sensor = None

    _camera = None
    _magnification = 0.0

    @property
    def magnification(self):
        if not self._magnification:
            if self.ep and self.ota:
                self._magnification = self.ota.focal_length / self.ep.focal_length

            # No EP and a sensor means prime focus
            elif self.sensor and self.ota:
                self._magnification = self.ota.focal_length / self.sensor.diagonal

        return self._magnification

    @property
    def camera(self):
        return self._camera

    def __setattr__(self, name, value):
        if name == 'camera':
            self.sensor = value.sensor
            self._camera = value
        else:
            super(System, self).__setattr__(name, value)


class OTA(OpticsBaseItem, OpticalSystem):
    pass


class Sensor(OpticsBaseItem):
    width = 0.0
    height = 0.0

    _diagonal = None

    @property
    def diagonal(self):
        if not self._diagonal:
            self._diagonal = math.sqrt(
                math.pow(self.width, 2) + math.pow(self.height, 2))
        return self._diagonal


class EP(OpticsBaseItem, OpticalSystem):
    barrel_size = 0.0
    eye_relief = 0.0


class DSLR(OpticsBaseItem):
    sensor = None

