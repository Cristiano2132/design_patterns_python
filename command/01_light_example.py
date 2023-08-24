from datetime import datetime
from typing import Dict, Type
import time
from abc import ABCMeta, abstractmethod

class ICommand(metaclass=ABCMeta):
    "The switch interface, that all commands will implement"

    @staticmethod
    @abstractmethod
    def execute():
        "The required execute method that all command objects will use"

class ILight(metaclass=ABCMeta):
    "The Light interface, that all light objects will implement"

    @staticmethod
    @abstractmethod
    def turn_on():
        "The required turn_on method that all light objects will use"

    @staticmethod
    @abstractmethod
    def turn_off():
        "The required turn_off method that all light objects will use"

"The Light. The Receiver"

class Light(ILight):
    "The Receiver"

    @staticmethod
    def turn_on():
        "A set of instructions to run"
        print("Light turned ON")

    @staticmethod
    def turn_off():
        "A set of instructions to run"
        print("Light turned OFF")

"""
The Switch (Invoker) Class.
You can flick the switch and it then invokes a registered command
"""

class RemoteControl:
    "The Invoker Class."

    def __init__(self):
        self._commands: Dict[str, Type[ICommand]] = {}
        self._history: list = []

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
            #or if you want to record these replays in history
            #self.execute(command[1])

"""
A Command object, that implements the ISwitch interface and runs the
command on the designated receiver
"""


class SwitchOnCommand(ICommand):  # pylint: disable=too-few-public-methods
    "Switch On Command"

    def __init__(self, light: ILight):
        self._light = light

    def execute(self):
        self._light.turn_on()

"""
A Command object, that implements the ISwitch interface and runs the
command on the designated receiver
"""

class SwitchOffCommand(ICommand):  # pylint: disable=too-few-public-methods
    "Switch Off Command"

    def __init__(self, light: ILight):
        self._light = light

    def execute(self):
        self._light.turn_off()

if __name__ == "__main__":
    print("Running the Light Example")
    print("-------------------------")
    # Create a receiver
    LIGHT = Light()

    # Create Commands
    SWITCH_ON = SwitchOnCommand(LIGHT)
    SWITCH_OFF = SwitchOffCommand(LIGHT)

    # Register the commands with the invoker
    SWITCH = RemoteControl()
    SWITCH.register("ON", SWITCH_ON)
    SWITCH.register("OFF", SWITCH_OFF)

    # Execute the commands that are registered on the Invoker
    SWITCH.execute("ON")
    SWITCH.execute("OFF")
    SWITCH.execute("ON")
    SWITCH.execute("OFF")

    

    # show history
    SWITCH.show_history()

    # replay last two executed commands
    SWITCH.replay_last(2)