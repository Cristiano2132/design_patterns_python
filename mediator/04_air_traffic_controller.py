from abc import ABC, abstractmethod

class IFlight(ABC):
    @abstractmethod
    def land(self):
        pass
    
    @abstractmethod
    def takeoff(self):
        pass

class ATC:
    def __init__(self):
        self.flights = []
    
    def add_flight(self, flight):
        self.flights.append(flight)
    
    def request_landing(self, flight):
        for other_flight in self.flights:
            if other_flight != flight:
                other_flight.land()

    def request_takeoff(self, flight):
        for other_flight in self.flights:
            if other_flight != flight:
                other_flight.takeoff()

class Flight(IFlight):
    def __init__(self, name, atc):
        self.name = name
        self.atc = atc
        self.atc.add_flight(self)
    
    def land(self):
        print(f'{self.name} is requesting landing clearance from ATC')
    
    def takeoff(self):
        print(f'{self.name} is requesting takeoff clearance from ATC')

if __name__ == '__main__':
    atc = ATC()
    flight1 = Flight("Flight 1", atc)
    flight2 = Flight("Flight 2", atc)
    flight3 = Flight("Flight 3", atc)

    flight1.land()
    flight2.takeoff()
