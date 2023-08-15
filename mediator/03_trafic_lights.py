from abc import ABC, abstractmethod

class ILight(ABC):
    @abstractmethod
    def turnON(self):
        pass
    
    @abstractmethod
    def turnOFF(self):
        pass


class LightMediator:
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

    def __init__(self, color, LightMediator):
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
