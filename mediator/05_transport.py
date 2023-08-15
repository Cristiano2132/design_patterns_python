from abc import ABCMeta, abstractmethod
from typing import List

class ITransportable(metaclass=ABCMeta):
    """Interface for transportable units."""

    @abstractmethod
    def embark(self):
        """Embark the transportable unit onto a transporter."""
        pass
    
    @abstractmethod
    def disembark(self):
        """Disembark the transportable unit from a transporter."""
        pass
    
    @abstractmethod
    def idle(self):
        """Set the transportable unit to idle state."""
        pass
    
    @abstractmethod
    def activate(self):
        """Activate the transportable unit for action."""
        pass

class ITransportUnit(metaclass=ABCMeta):
    """Interface for transport vehicles."""

    @abstractmethod
    def arrive(self):
        """Signal that the transport unit has arrived."""
        pass
    
    @abstractmethod
    def depart(self):
        """Signal that the transport unit has departed."""
        pass
    
    @abstractmethod
    def travel(self):
        """Signal that the transport unit is traveling."""
        pass
    
    @abstractmethod
    def start_embarkation(self):
        """Start the process of embarking transportable units."""
        pass
    
    @abstractmethod
    def start_disembarkation(self):
        """Start the process of disembarking transportable units."""
        pass

class IMediator(metaclass=ABCMeta):
    """Interface for mediators."""

    @abstractmethod
    def register_transportable(self, unit):
        """Register a transportable unit with the mediator."""
        pass
    
    @abstractmethod
    def register_transport_unit(self, unit):
        """Register a transport unit with the mediator."""
        pass
    
    @abstractmethod
    def start_embarkation_process(self, transporter):
        """Start the process of embarking transportable units onto a transporter."""
        pass
    
    @abstractmethod
    def start_disembarkation_process(self, transporter):
        """Start the process of disembarking transportable units from a transporter."""
        pass
    
    @abstractmethod
    def unit_activated(self, unit):
        """Handle the activation of a transportable unit."""
        pass
    
    @abstractmethod
    def unit_idled(self, unit):
        """Handle the idling of a transportable unit."""
        pass
    
    @abstractmethod
    def unit_embarked(self, unit):
        """Handle the embarkation of a transportable unit."""
        pass
    
    @abstractmethod
    def unit_disembarked(self, unit):
        """Handle the disembarkation of a transportable unit."""
        pass

class HeadQuarters(IMediator):
    """Central controller for managing interaction between transportable units and transport vehicles."""

    def __init__(self):
        self.units: List[ITransportUnit] = []
        self.transporters: List[ITransportable] = []

    def register_transportable(self, unit: ITransportUnit):
        """Register a transportable unit with the headquarters."""
        self.units.append(unit)
        
    def register_transport_unit(self, unit: ITransportUnit):
        """Register a transport unit with the headquarters."""
        self.transporters.append(unit)

    def start_embarkation_process(self, transporter: ITransportable):
        """Start the process of embarking transportable units onto a transporter."""
        print(f"HeadQuarters starting embarkation process on {transporter}")
        for t in self.units:
            t.embark()
            t.idle()
        print("Embarkation process finished.")

    def start_disembarkation_process(self, transporter: ITransportable):
        """Start the process of disembarking transportable units from a transporter."""
        print(f"HeadQuarters starting disembarkation process on {transporter}")
        for t in self.units:
            t.activate()
            t.disembark()
        print("Disembarkation process finished.")
        
    def unit_activated(self, unit: ITransportUnit):
        """Handle the activation of a transportable unit."""
        print("Unit activated...")

    def unit_idled(self, unit: ITransportUnit):
        """Handle the idling of a transportable unit."""
        print("Unit idled...")

    def unit_embarked(self, unit: ITransportUnit):
        """Handle the embarkation of a transportable unit."""
        print("Unit embarked...")

    def unit_disembarked(self, unit: ITransportUnit):
        """Handle the disembarkation of a transportable unit."""
        print("Unit disembarked...")

class TransportableFightingUnit(ITransportable):
    """Concrete class representing a transportable fighting unit."""

    def __init__(self, headquarters: IMediator, name: str):
        self.headquarters = headquarters
        self.name = name
        self.headquarters.register_transportable(self)

    def embark(self):
        """Embark the transportable fighting unit onto a transporter."""
        print(f"{self} embarking...")
        self.headquarters.unit_embarked(self)

    def disembark(self):
        """Disembark the transportable fighting unit from a transporter."""
        print(f"{self} disembarking...")
        self.headquarters.unit_disembarked(self)

    def idle(self):
        """Set the transportable fighting unit to idle state."""
        print(f"{self} idling...")
        self.headquarters.unit_idled(self)
    
    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        if isinstance(other, TransportableFightingUnit):
            return self.name == other.name
        return False

    def __str__(self):
        return self.name

    def activate(self):
        """Activate the transportable fighting unit for action."""
        print(f"{self} activating...")
        self.headquarters.unit_activated(self)

class TransportShip(ITransportUnit):
    """Concrete class representing a transport ship."""

    def __init__(self, headquarters: IMediator):
        self.headquarters = headquarters
        self.headquarters.register_transport_unit(self)

    def arrive(self):
        """Signal that the transport ship has arrived."""
        print(f"{self} arriving...")
        
    def start_embarkation(self):
        """Start the process of embarking transportable units onto the ship."""
        print(f"{self} starting embarkation...")
        self.headquarters.start_embarkation_process(self)
        
    def start_disembarkation(self):
        """Start the process of disembarking transportable units from the ship."""
        print(f"{self} starting disembarkation...")
        self.headquarters.start_disembarkation_process(self)
        
    def depart(self):
        """Signal that the transport ship has departed."""
        print(f"{self} departing...")
        
    def travel(self):
        """Signal that the transport ship is traveling."""
        print(f"{self} travelling...")
        
    def __str__(self):
        return self.__class__.__name__

if __name__ == "__main__":
    # Client Code
    hq = HeadQuarters()
    unit1 = TransportableFightingUnit(headquarters=hq, name="Unit 1")
    unit2 = TransportableFightingUnit(headquarters=hq, name="Unit 2")
    ship = TransportShip(hq)

    print('-' * 50)
    print('# Ship arrives to collect units')
    print('-' * 50)
    ship.arrive()
    print('# Mediator controls the Transportable units')
    ship.start_embarkation()

    print('-' * 50)
    print('Ship departs to final destination')
    print('-' * 50)
    ship.depart()
    ship.travel()
    ship.arrive()
    print('-' * 50)
    ship.start_disembarkation()
    print('# Mediator controls the Transportable units')
