from abc import ABCMeta, abstractmethod
from typing import List

class ISubject(metaclass=ABCMeta):
    """
    Abstract Subject - Abstract patient in this demo
    """

    @abstractmethod
    def register_observer(self):
        pass

    @abstractmethod
    def remove_observer(self):
        pass

    @abstractmethod
    def notify_observers(self):
        pass


class IObserver(metaclass=ABCMeta):
    """
    Observer Interface
    """

    @abstractmethod
    def update(self):
        pass


class Subject(ISubject):
    """
    Concrete Subject - Patient
    """

    def __init__(self, product_name: str, product_price: float, availability: str):
        self.observers: List[IObserver] = []
        self.product_name = product_name
        self.product_price = product_price
        self.availability = availability

    def get_availability(self):
        return self.availability

    def set_availability(self, availability):
        self.availability = availability
        self.notify_observers()

    def register_observer(self, observer: IObserver):
        print(f"({self.product_name}) Observer Added:", observer.user_name)
        self.observers.append(observer)

    def remove_observer(self, observer: IObserver):
        print(f"({self.product_name}) Observer Removed:", observer.user_name)
        self.observers.remove(observer)

    def notify_observers(self):
        print("Product Name:", self.product_name, ", product Price:", self.product_price,
              f"is Now {self.availability}. So, notifying all Registered users ")
        print()
        for observer in self.observers:
            observer.update(self.availability)


class Observer(IObserver):
    """
    Concrete Observer class
    """

    def __init__(self, user_name: str):
        self.user_name = user_name

    def add_subscriber(self, subject: ISubject):
        subject.register_observer(self)

    def remove_subscriber(self, subject: ISubject):
        subject.remove_observer(self)

    def update(self, availability):
        print("Hello", self.user_name, ", Product is now", availability, "on Amazon")


if __name__ == "__main__":

    # Create a Product with Out of Stock Status
    red_mi = Subject("Red MI Mobile", 10000, "Available")
    
    user1 = Observer("Anurag")
    user2 = Observer("Pranaya")
    user3 = Observer("Priyanka")

    user1.add_subscriber(red_mi)
    user2.add_subscriber(red_mi)
    user3.add_subscriber(red_mi)

    red_mi.set_availability("Out Of Stock")
    user3.remove_subscriber(red_mi)
    red_mi.set_availability("Available")
