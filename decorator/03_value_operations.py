from abc import ABCMeta, abstractmethod

class IValue(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def __str__():
        pass

class Value(IValue):
    def __init__(self, value: IValue):
        self.value = value

    def __str__(self):
        return str(self.value)

class Add(IValue):
    def __init__(self, val1: IValue, val2: IValue):
        val1 = getattr(val1, 'value', val1)
        val2 = getattr(val2, 'value', val2)
        self.value = val1 + val2

    def __str__(self):
        return str(self.value)

class Sub(IValue):
    def __init__(self, val1: IValue, val2: IValue):
        val1 = getattr(val1, 'value', val1)
        val2 = getattr(val2, 'value', val2)
        self.value = val1 - val2

    def __str__(self):
        return str(self.value)

if __name__ == "__main__":
    A = Value(1)
    B = Value(2)
    C = Value(5)

    print(Add(A, B))
    print(Add(A, 100))
    print(Sub(C, A))
    print(Sub(Add(C, B), A))
    print(Sub(100, 101))
    print(Add(Sub(Add(C, B), A), 100))
    print(Sub(123, Add(C, C)))
    print(Add(Sub(Add(C, 10), A), 100))
    print(A)
    print(B)
    print(C)
