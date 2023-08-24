import random
import threading
import time
from threading import Lock

class MyClass():
    
    def __init__(self) -> None:
        time.sleep(2)
        self.value = random.randint(1, 100)
        print(f"No Threading Safe: {threading.current_thread().name}: {self} and value: {self.value}\n")
        type(self).__inited = True

def singleton_decorator(cls, *args, **kwargs):
    """ defines a Thread-safe Singleton decorator """
    instance = {}
    lock = threading.Lock()

    def wrapper_singleton(*args, **kwargs):
        if cls not in instance:
            with lock:  # Acquire the lock before instance creation
                if cls not in instance:  # Check again within the lock
                    instance[cls] = cls(*args, **kwargs)
        return instance[cls]

    return wrapper_singleton

@singleton_decorator
class Singleton(MyClass):
    def __init__(self) -> None:
        super().__init__()

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
    print("                Safe Threading Singleton")
    print("--------------------------------------------------")

    execute_in_thread(10, Singleton)
    print("--------------------------------------------------")
    print("                No Singleton")
    print("--------------------------------------------------")
    execute_in_thread(10, MyClass)
    
    