import random
import threading
import time
from threading import Lock

class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
    

class SafeSingletonMeta(type):
    """
    This is a thread-safe implementation of Singleton.
    """

    _instances = {}

    _lock: Lock = Lock()
    """
    We now have a lock object that will be used to synchronize threads during
    first access to the Singleton.
    """

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        # Now, imagine that the program has just been launched. Since there's no
        # Singleton instance yet, multiple threads can simultaneously pass the
        # previous conditional and reach this point almost at the same time. The
        # first of them will acquire lock and will proceed further, while the
        # rest will wait here.
        with cls._lock:
            # The first thread to acquire the lock, reaches this conditional,
            # goes inside and creates the Singleton instance. Once it leaves the
            # lock block, a thread that might have been waiting for the lock
            # release may then enter this section. But since the Singleton field
            # is already initialized, the thread won't create a new object.
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):
    
    def __init__(self) -> None:
        time.sleep(2)
        self.value = random.randint(1, 100)
        print(f"No Threading Safe: {threading.current_thread().name}: {self} and value: {self.value}\n")
        type(self).__inited = True

class SafeSingleton(metaclass=SafeSingletonMeta):
    
    def __init__(self) -> None:
        time.sleep(2)
        self.value = random.randint(1, 100)
        print(f"Safe: {threading.current_thread().name}: {self} and value: {self.value}\n")
        type(self).__inited = True
        
def execute_in_thread(n_threads, singleton_class):
    def create_singleton_instances():
        s = singleton_class()
    threads = []
    for i in range(n_threads):
        t = threading.Thread(target=create_singleton_instances)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()


if __name__=='__main__':
    print("--------------------------------------------------")
    print("                Safe Singleton")
    print("--------------------------------------------------")

    execute_in_thread(10, SafeSingleton)
    print("--------------------------------------------------")
    print("                No Threading Safe")
    print("--------------------------------------------------")
    execute_in_thread(10, Singleton)
    
    