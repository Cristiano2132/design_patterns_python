from abc import ABCMeta, abstractmethod

class ILight(metaclass=ABCMeta):
    @abstractmethod
    def turnON(self):
        pass
    
    @abstractmethod
    def turnOFF(self):
        pass

class IMediator(metaclass=ABCMeta):
    @abstractmethod
    def registerLight(self, light: ILight):
        pass

    @abstractmethod
    def unRegisterLight(self, light: ILight):
        pass

    @abstractmethod
    def turnOffAllOtherLights(self, light: ILight):
        pass

    @abstractmethod
    def notifyMediator(self, light: ILight):
        pass

class LightMediator(IMediator):
    def __init__(self):
        self.trafficSignal = set()

    def registerLight(self, light: ILight):
        self.trafficSignal.add(light)

    def unRegisterLight(self, light: ILight):
        self.trafficSignal.remove(light)

    def turnOffAllOtherLights(self, light: ILight):
        for l in self.trafficSignal:
            if l != light:
                l.turnOFF()
        print("------------------------------")

    def notifyMediator(self, light: ILight):
        self.turnOffAllOtherLights(light)


class Light:
    class State:
        ON = "ON"
        OFF = "OFF"

    def __init__(self, color: str, LightMediator: IMediator):
        self.color = color
        self.currentState = None
        self.LightMediator = LightMediator
        LightMediator.registerLight(self)

    def turnON(self):
        self.currentState = self.State.ON
        print(f"{self} is turned {self.currentState}")
        self.LightMediator.notifyMediator(self)

    def turnOFF(self):
        self.currentState = self.State.OFF
        print(f"{self} is turned {self.currentState}")

    def __hash__(self):
        return hash(self.color)

    def __eq__(self, other):
        if isinstance(other, Light):
            return self.color == other.color
        return False

    def __str__(self):
        return self.color


if __name__ == "__main__":
    lightMediator = LightMediator()
    red = Light("Red", lightMediator)
    green = Light("Green", lightMediator)
    yellow = Light("Yellow", lightMediator)

    red.turnON()
    green.turnON()
    yellow.turnON()
