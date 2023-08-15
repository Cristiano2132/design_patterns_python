from abc import ABCMeta, abstractmethod
from typing import List

class IMediator(metaclass=ABCMeta):
    @abstractmethod
    def register_flight(self, flight):
        pass

    @abstractmethod
    def request_landing(self, flight, terminal):
        pass

    @abstractmethod
    def grant_landing(self, flight, terminal):
        pass

    @abstractmethod
    def notify_other_flights(self, landed_flight, terminal):
        pass


class IFlight(metaclass=ABCMeta):
    name: str
    terminal: int
    atc: IMediator

    @abstractmethod
    def request_to_land(self, terminal):
        pass

    @abstractmethod
    def receive_notification(self, landed_flight):
        pass


class ATCTower(IMediator):
    def __init__(self)-> None:
        self.flights: List[IFlight] = []

    def register_flight(self, flight: IFlight) -> None:
        self.flights.append(flight)

    def request_landing(self, flight: IFlight, terminal: int)-> bool:
        for other_flight in self.flights:
            if other_flight != flight and other_flight.terminal == terminal:
                return False
        return True

    def grant_landing(self, flight: IFlight, terminal: int)-> None:
        print(f"ATC: {flight.name}, you are clear to land at Terminal {terminal}.")
        self.notify_other_flights(flight, terminal)

    def notify_other_flights(self, landed_flight: IFlight, terminal: int)-> None:
        for other_flight in self.flights:
            if other_flight != landed_flight and other_flight.terminal == terminal:
                other_flight.receive_notification(landed_flight)

class Flight(IFlight):
    def __init__(self, name: str, terminal: int, atc: IMediator)-> None:
        self.name = name
        self.terminal = terminal
        self.atc = atc
        self.atc.register_flight(self)

    def request_to_land(self, terminal)-> None:
        if self.atc.request_landing(flight = self, terminal = terminal):
            self.atc.grant_landing(flight = self, terminal = terminal)
        else:
            print(f"{self.name}: Unable to land at Terminal {terminal}. Waiting for clearance.")

    def receive_notification(self, landed_flight)-> None:
        print(f"{self.name}: {landed_flight.name} is landing at my terminal. Holding position.")


    # def __hash__(self)-> int:
    #     return hash(self.name)

    def __eq__(self, other)-> bool:
        if isinstance(other, Flight):
            return self.name == other.name
        return False

    def __str__(self)-> str:
        return self.name
    
if __name__ == "__main__":
    atc_tower = ATCTower()

    flight_101 = Flight("Flight 101", 1, atc_tower)
    flight_202 = Flight("Flight 202", 2, atc_tower)
    flight_707 = Flight("Flight 707", 1, atc_tower)
    flight_808 = Flight("Flight 808", 3, atc_tower)

    flight_101.request_to_land(1)
    flight_202.request_to_land(2)
    flight_707.request_to_land(1)
    flight_808.request_to_land(3)
