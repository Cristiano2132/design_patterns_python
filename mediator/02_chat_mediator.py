# https://www.tutorialandexample.com/mediator-design-pattern-in-python

from abc import ABCMeta, abstractmethod
from typing import List

class IMediator(metaclass=ABCMeta):
    @abstractmethod
    def add_user(self):
        pass

    @abstractmethod
    def send_message(self):
        pass


class IUser(metaclass=ABCMeta):
    @abstractmethod
    def send(self):
        pass
    @abstractmethod
    def receive(self):
        pass


class Chat_Mediator(IMediator):
    def __init__(self)-> None:
        self.users: List[IUser] = []

    def add_user(self, user: IUser)-> None:
        self.users.append(user)

    def send_message(self, msg: str, user: IUser)-> None:
        for u in self.users:
            if u != user:
                u.receive(msg)

class User(IUser):
    def __init__(self, med: IMediator, name_: str)-> None:
        self.mediator = med
        self.name = name_

    def send(self, msg: str)-> None:
        print(f'Sending message from {self.name}:' + msg)
        self.mediator.send_message(msg, self)

    def receive(self, msg: str)-> None:
        print(f'{self.name} received a Message:' + msg)


if __name__ == '__main__':
    mediator = Chat_Mediator()
    consumer1 = User(mediator, "Sweta")
    consumer2 = User(mediator, "Aditya")
    consumer3 = User(mediator, "Rakhi")
    consumer4 = User(mediator, "Mishri")
    mediator.add_user( consumer1)
    mediator.add_user( consumer2)
    mediator.add_user( consumer3)
    mediator.add_user( consumer4)
    consumer1.send("Hello, every one is invited and we feel immense pleasure to accompanied by you .")