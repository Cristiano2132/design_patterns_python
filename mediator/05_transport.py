from abc import ABC, abstractmethod
from typing import Collection

class ITransportable(ABC):
    @abstractmethod
    def embark(self):
        pass
    
    @abstractmethod
    def disembark(self):
        pass
    
    @abstractmethod
    def idle(self):
        pass
    
    @abstractmethod
    def activate(self):
        pass

class ITransportUnit(ABC):
    @abstractmethod
    def arrive(self):
        pass
    
    @abstractmethod
    def depart(self):
        pass
    
    @abstractmethod
    def travel(self):
        pass
    
    @abstractmethod
    def start_embarkation(self):
        pass
    
    @abstractmethod
    def start_disembarkation(self):
        pass

class HeadQuarters:
    def __init__(self):
        self.units = []
        self.transporters = []

    def register_transportable(self, unit):
        self.units.append(unit)
        
    def register_transport_unit(self, unit):
        self.transporters.append(unit)

    def start_embarkation_process(self, transporter):
        print(f"HeadQuarters starting embarkation process on {transporter}")
        for t in self.units:
            t.embark()
            t.idle()
        print("Embarkation process finished.")

    def start_disembarkation_process(self, transporter):
        print(f"HeadQuarters starting disembarkation process on {transporter}")
        for t in self.units:
            t.activate()
            t.disembark()
        print("Disembarkation process finished.")
        
    def unit_activated(self, unit):
        print("Unit activated...")

    def unit_idled(self, unit):
        print("Unit idled...")

    def unit_embarked(self, unit):
        print("Unit embarked...")

    def unit_disembarked(self, unit):
        print("Unit disembarked...")

class TransportableFightingUnit(ITransportable):
    def __init__(self, headquarters):
        self.headquarters = headquarters
        self.headquarters.register_transportable(self)

    def embark(self):
        print(f"{self} embarking...")
        self.headquarters.unit_embarked(self)

    def disembark(self):
        print(f"{self} disembarking...")
        self.headquarters.unit_disembarked(self)

    def idle(self):
        print(f"{self} idling...")
        self.headquarters.unit_idled(self)

    def activate(self):
        print(f"{self} activating...")
        self.headquarters.unit_activated(self)

class TransportShip(ITransportUnit):
    def __init__(self, headquarters):
        self.headquarters = headquarters
        self.headquarters.register_transport_unit(self)

    def arrive(self):
        print(f"{self} arriving...")
        
    def start_embarkation(self):
        print(f"{self} starting embarkation...")
        self.headquarters.start_embarkation_process(self)
        
    def start_disembarkation(self):
        print(f"{self} starting disembarkation...")
        self.headquarters.start_disembarkation_process(self)
        
    def depart(self):
        print(f"{self} departing...")
        
    def travel(self):
        print(f"{self} travelling...")
        
    def __str__(self):
        return self.__class__.__name__

# Client Code
hq = HeadQuarters()
unit1 = TransportableFightingUnit(hq)
unit2 = TransportableFightingUnit(hq)
ship = TransportShip(hq)

# Ship arrives in its own time
ship.arrive()

# Mediator controls the Transportable units
ship.start_embarkation()
ship.depart()
ship.travel()
ship.arrive()
ship.start_disembarkation()
