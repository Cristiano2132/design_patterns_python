from abc import ABCMeta, abstractmethod
import datetime
import time
from typing import Dict, Type

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

class RemoteControl:
    def __init__(self):
        self._commands: Dict[str, Type[ICommand]] = {}
        self._history = []

    def show_history(self):
        "Print the history of each time a command was invoked"
        for row in self._history:
            print(
                f"{datetime.fromtimestamp(row[0]).strftime('%H:%M:%S')}"
                f" : {row[1]}"
            )

    def register(self, command_name: str, command: ICommand):
        "Register commands in the Invoker"
        self._commands[command_name] = command

    def execute(self, command_name: str):
        "Execute any registered commands"
        if command_name in self._commands.keys():
            self._commands[command_name].execute()
            self._history.append((time.time(), command_name))
        else:
            print(f"Command [{command_name}] not recognised")

    def replay_last(self, number_of_commands: int):
        "Replay the last N commands"
        commands = self._history[-number_of_commands:]
        for command in commands:
            self._commands[command[1]].execute()

# Concrete command classes
class LightOnCommand(ICommand):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()


class LightOffCommand(ICommand):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_off()


class FanOnCommand(ICommand):
    def __init__(self, fan):
        self.fan = fan

    def execute(self):
        self.fan.turn_on()


class FanOffCommand(ICommand):
    def __init__(self, fan):
        self.fan = fan

    def execute(self):
        self.fan.turn_off()


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




if __name__ == "__main__":
    # Create the receiver
    light = Light()
    fan = Fan()

    # Create the invoker
    remote = RemoteControl()

    # Create the commands
    light_on = LightOnCommand(light)
    light_off = LightOffCommand(light)
    fan_on = FanOnCommand(fan)
    fan_off = FanOffCommand(fan)

    # Register the commands
    remote.register("light_on", light_on)
    remote.register("light_off", light_off)
    remote.register("fan_on", fan_on)
    remote.register("fan_off", fan_off)

    # Execute the commands
    remote.execute("light_on")
    remote.execute("light_off")
    remote.execute("fan_on")
    remote.execute("fan_off")