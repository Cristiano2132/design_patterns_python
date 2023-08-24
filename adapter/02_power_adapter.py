class PowerSocket:
    """
       PowerSocket base class 
    """
    def __init__ (self, hole_num, shape, volt):
        self.__num_holes = hole_num
        self.__hole_shape = shape
        self.__volt = volt

    def get_hole_num(self):
        return self.__num_holes 

    def get_hole_shape(self):
        return self.__hole_shape 

    def get_volt(self):
        return self.__volt 

### some concrete PowerSocket classes
class ChineseSocket(PowerSocket):
    def __init__ (self, name: str = "CHINESE"):
        super().__init__(3, "FLAT", 220)
        self.name = name
    
    def __eq__(self, other):
        if isinstance(other, ChineseSocket):
            return self.name == other.name
        return False

    def __str__(self):
        return self.name

class EuropeanSocket(PowerSocket):
    def __init__ (self, name: str = "EUROPEAN"):
        super().__init__(2, "ROUND", 220)
        self.name = name

    def __eq__(self, other):
        if isinstance(other, EuropeanSocket):
            return self.name == other.name
        return False

    def __str__(self):
        return self.name       

class TaiwaneseSocket(PowerSocket):
    def __init__ (self, name: str = "TAIWANESE"):
        super().__init__(2, "FLAT", 110)
        self.name = name

    def __eq__(self, other):
        if isinstance(other, TaiwaneseSocket):
            return self.name == other.name
        return False
    
    def __str__(self):
        return self.name

class Chinese3PinPlug():
    def __init__(self, name: str = "CHINESE3PINPLUG"):
        self.pins = 3
        self.volt = 220
        self.pin_shape = "FLAT" 
        self.name = name
    
    def __eq__(self, other):
        if isinstance(other, Chinese3PinPlug):
            return self.name == other.name
        return False
    
    def __str__(self):
        return self.name
    

class Laptop:
    def __init__(self):
        self.plug = Chinese3PinPlug()

    def charge(self, socket, power_in_watt):
        res = False     
        if isinstance(socket, PowerSocket):
            res = (self.plug.pins == socket.get_hole_num()) and \
                  (self.plug.pin_shape == socket.get_hole_shape()) and  \
                  (self.plug.volt == socket.get_volt())
        else:
            print("Socket is not an instance of PowerSocket")

        if res:
            current = round(power_in_watt / self.plug.volt, 2)
            print(f"Start charging...., Plug: {self.plug} Socket: {socket}" )
        else:
            print(f"Socket and plug not compatible, Plug: {self.plug} Socket: {socket}.")
        return res
    
if __name__ == "__main__":
    laptop = Laptop() # instance of my Redmi Laptop

    # I am in China mainland
    ch_socket = ChineseSocket()
    laptop.charge(socket=ch_socket, power_in_watt=235)

    # I am in France
    eu_socket = EuropeanSocket()
    laptop.charge(socket=eu_socket, power_in_watt=235)

    # I am in Taipei 
    tw_socket = TaiwaneseSocket()
    laptop.charge(socket=tw_socket, power_in_watt=235)
