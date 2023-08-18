from abc import ABCMeta, abstractmethod
import time
from typing import List

class ISubject(metaclass=ABCMeta):
    """
    Abstract Subject - Abstract patient in this demo
    """

    def add_obs(self):
        pass

    def remove_obs(self):
        pass

    def notify_observers(self):
        pass


class IObserver():
    """
    Abstract Observer - Abstract medical device in this demo
    """

    def update(self):
        pass


class CovidPatient(ISubject):
    """
    Concrete Subject - Patient
    """

    def __init__(self, name):
        self.__observers: List[IObserver] = []
        self.name = name
        self.__physio_params = {"temperature": 0.0, "heartrate": 0.0, "oxygen": 0.0, "respiration": 0.0}

    def add_obs(self, observer: IObserver):
        self.__observers.append(observer)

    def remove_obs(self, observer: IObserver):
        self.__observers.remove(observer)

    def notify_observers(self, arg=0):
        for o in self.__observers:
            o.update(self, arg)

    def set_value(self, measure_type, val):
        if measure_type in self.__physio_params:
            self.__physio_params[measure_type] = val
            self.notify_observers()
        else:
            print("Parameter type \"{}\" not yet supported.".format(measure_type))

    def get_value(self, measure_type):
        if measure_type in self.__physio_params:
            return self.__physio_params[measure_type]
        else:
            return None


class Thermometer(IObserver):
    """
    Concrete Observer - Thermometer
    """
    def __init__(self):
        pass

    def update(self, subject: ISubject, arg):
        if subject.__class__ == CovidPatient:
            temp = subject.get_value("temperature")
            if temp > 37.8:
                print("EMCY - " + "Temperature too high: " + str(temp))
            elif temp < 36.0:
                print("EMCY - " + "Temperature too slow: " + str(temp))
            else:
                pass
        else:
            pass


class HeartBeatMonitor(IObserver):
    """
    Concrete Observer - heartbeat monitor
    """

    def __init__(self):
        pass

    def update(self, subject: ISubject, arg):
        if subject.__class__ == CovidPatient:
            hr = subject.get_value("heartrate")
            if hr > 120:
                print("EMCY - " + "Heart rate too high: " + str(hr))
            elif hr < 35:
                print("EMCY - " + "Heart rate too slow:  " + str(hr))
            else:
                pass
        else:
            pass


if __name__ == "__main__":
    patient = CovidPatient("John")
    thermometer = Thermometer()
    heart_beat_monitor = HeartBeatMonitor()

    # now kick off the simulation
    for i in range(0, 15):
        time.sleep(0.5)
        print("====== Time step {} =======".format(i + 1))

        # At round #3: thermometer is added for monitoring temperature
        # At round #5: heartbeatMonitor is added for monitoring heart rate
        # At round #10: thermometer is removed

        if i == 3:
            patient.add_obs(thermometer)
        elif i == 5:
            patient.add_obs(heart_beat_monitor)
        elif i == 10:
            patient.remove_obs(thermometer)

        # simulating the variation of patient's physiological parameters
        if i % 3 == 0:
            patient.set_value("temperature", 35.5 + 0.5 * i)
        elif i % 3 == 1:
            patient.set_value("heartrate", 30 + 10 * i)
        else:
            patient.set_value("oxygen", 5.0 + 0.05 * i)
