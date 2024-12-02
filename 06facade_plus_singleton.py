"""
facade pattern
==============

- facade pattern is useful to communicate with complex software system.

- when to use facade pattern?
# simplified interface
# managing complex subsystems
# layered subsystem architecture
"""


class Sensor(object):
    """This is sensor"""

    def __init__(self):
        pass

    def sensor_on(self):
        """sensor on when the temp is not normal"""
        print("sensor is on")

    def sensor_off(self):
        """sensor off when the temp is normal"""
        print("sensor is off")


class Smoke(object):
    """This is smoke"""

    def __init__(self):
        pass

    def smoke_on(self):
        """smoke on"""
        print("smoke is on")

    def smoke_off(self):
        """some off"""
        print("smoke is off")


class Light(object):
    """This is light"""

    def __init__(self):
        pass

    def light_on(self):
        """light on"""
        print("light is on")

    def light_off(self):
        """light off"""
        print("light is off")


class Meta(type):
    """This is Metaclass"""

    _instance = {}

    def __call__(cls, *args, **kwargs):
        """if the instance is created, don't create"""

        if cls not in cls._instance:
            cls._instance[cls] = super(Meta, cls).__call__(*args, **kwargs)

            return cls._instance[cls]


class Facade(metaclass=Meta):
    """This is facade class"""

    def __init__(self):
        self._sensor = Sensor()
        self._smoke = Smoke()
        self._light = Light()

    def emergency(self):
        self._sensor.sensor_on()
        self._smoke.smoke_on()
        self._light.light_on()

    def no_emergency(self):
        self._sensor.sensor_off()
        self._smoke.smoke_off()
        self._light.light_off()


if __name__ == "__main__":
    facade = Facade()
    facade1 = Facade()
    print(facade)
    print(facade1)  # o/p: None
    temp = 67

    if temp > 60:
        print("The temp is {}".format(temp))
        facade.emergency()
    else:
        print("The temp is {}".format(temp))
        facade.no_emergency()
