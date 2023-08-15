from abc import ABC, abstractmethod
class IUser():
    def __init__(self, med, name_):
        self.mediator = med
        self.name = name_
    @abstractmethod
    def send(self, msg):
        pass
    @abstractmethod
    def receive(self, msg):
        pass

class Chat_Mediator:
    def __init__(self):
        self.users = []
    def add_user(self, user):
        self.users.append(user)
    def send_message(self, msg, user):
        for u in self.users:
            if u != user:
                u.receive(msg)

class User(IUser):
    def send(self, msg):
        print(f'Sending message from {self.name}:' + msg)
        self.mediator.send_message(msg, self)
    def receive(self, msg):
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