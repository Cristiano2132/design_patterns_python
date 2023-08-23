from abc import ABCMeta, abstractmethod

class IGame(metaclass=ABCMeta):
    "A Game Interface"
    @staticmethod
    @abstractmethod
    def add_winner(position, name):
        "Must implement add_winner"


class Game1(IGame):  # pylint: disable=too-few-public-methods
    "Game1 implements IGame"

    def __init__(self):
        self.leaderboard = Leaderboard()

    def add_winner(self, position: int, name: str):
        self.leaderboard.add_winner(position, name)


class Game2(IGame):  # pylint: disable=too-few-public-methods
    "Game2 implements IGame"

    def __init__(self):
        self.leaderboard = Leaderboard()

    def add_winner(self, position, name):
        self.leaderboard.add_winner(position, name)


class Game3(Game2):  # pylint: disable=too-few-public-methods
    """Game 3 Inherits from Game 2 instead of implementing IGame"""


class Leaderboard():
    "The Leaderboard as a Singleton"
    _table = {}

    def __new__(cls):
        return cls

    @classmethod
    def print(cls):
        "A class level method"
        print("-----------Leaderboard-----------")
        for key, value in sorted(cls._table.items()):
            print(f"|\t{key}\t|\t{value}\t|")
        print()

    @classmethod
    def add_winner(cls, position, name):
        "A class level method"
        cls._table[position] = name

if __name__=='__main__':
    # The Client
    # All games share and manage the same leaderboard because it is a singleton.
    GAME1 = Game1()
    GAME1.add_winner(2, "Cosmo")

    GAME2 = Game2()
    GAME2.add_winner(3, "Sean")

    GAME3 = Game3()
    GAME3.add_winner(1, "Emmy")

    GAME1.leaderboard.print()
    GAME2.leaderboard.print()
    GAME3.leaderboard.print()
