from abc import ABCMeta, abstractmethod
import datetime
import re
import time
from typing import Dict, Type
import inspect

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
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.turn_on()

class LightOffCommand(ICommand):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.turn_off()

class FanOnCommand(ICommand):
    def __init__(self, fan: Fan):
        self.fan = fan

    def execute(self):
        self.fan.turn_on()

class FanOffCommand(ICommand):
    def __init__(self, fan: Fan):
        self.fan = fan

    def execute(self):
        self.fan.turn_off()


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

    def snake_case(self, class_name):
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', class_name)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

    def auto_register_commands(self, module):
        for name, obj in inspect.getmembers(module):
            if inspect.isclass(obj) and issubclass(obj, ICommand) and obj != ICommand:
                command_name = self.snake_case(name.replace("Command", ""))
                self.register(command_name, obj())

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

if __name__ == "__main__":
    remote = RemoteControl()
    light = Light()
    fan = Fan()

    remote.auto_register_commands(globals())

    # Execute the commands
    remote.execute("light_on_command")
    remote.execute("light_off_command")
    remote.execute("fan_on_command")
    remote.execute("fan_off_command")

