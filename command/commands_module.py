from abc import ABCMeta, abstractmethod

# Command interface
class ICommand(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        pass

class ISmartDevice(metaclass=ABCMeta):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

# Receiver classes
class Light(ISmartDevice):
    def turn_on(self):
        print("Light is ON")

    def turn_off(self):
        print("Light is OFF")

class Fan(ISmartDevice):
    def turn_on(self):
        print("Fan is ON")

    def turn_off(self):
        print("Fan is OFF")

# Concrete command classes
class LightOnCommand(ICommand):
    def __init__(self, light: Light = Light()):
        self.light = light

    def execute(self):
        self.light.turn_on()

class LightOffCommand(ICommand):
    def __init__(self, light: Light = Light()):
        self.light = light

    def execute(self):
        self.light.turn_off()

class FanOnCommand(ICommand):
    def __init__(self, fan: Fan = Fan()):
        self.fan = fan

    def execute(self):
        self.fan.turn_on()

class FanOffCommand(ICommand):
    def __init__(self, fan: Fan = Fan()):
        self.fan = fan

    def execute(self):
        self.fan.turn_off()