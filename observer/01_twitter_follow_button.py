from abc import ABCMeta, abstractmethod
from typing import List

# Interface for Subject
class Subject(metaclass=ABCMeta):
    @abstractmethod
    def register(self):
        pass
    
    @abstractmethod
    def unregister(self):
        pass
    
    @abstractmethod
    def notify_all_observers(self):
        pass

# Interface for Observer
class Observer(metaclass=ABCMeta):
    @abstractmethod
    def update(self):
        pass

# Concrete class for Celebrity (Subject)
class Celebrity(Subject):
    def __init__(self, celebrity_name):
        self.celebrity_name = celebrity_name
        self.followers: List[Subject] = []
    
    def register(self, subject: Subject):
        self.followers.append(subject)
        print(subject, "has started following", self.celebrity_name)
    
    def unregister(self, subject: Subject):
        self.followers.remove(subject)
        print(subject, "has stopped following", self.celebrity_name)
    
    def notify_all_observers(self, tweet: str):
        for follower in self.followers:
            follower.update(self.celebrity_name, tweet)
        print()
    
    def tweet(self, tweet: str):
        print("\n", self.celebrity_name, "has tweeted ::", tweet, "\n")
        self.notify_all_observers(tweet)

# Concrete class for Follower (Observer)
class Follower(Observer):
    def __init__(self, follower_name):
        self.follower_name = follower_name
    
    def update(self, celebrity_name, tweet):
        print(self.follower_name, "has received", celebrity_name + "'s tweet ::", tweet)
    
    def __str__(self):
        return self.follower_name

# Client code
if __name__ == "__main__":
    jhon_snow = Celebrity("Jhon Snow")
    selena_gomez = Celebrity("Selena Gomez")
    
    amar = Follower("Amar")
    juhi = Follower("Juhi")
    urja = Follower("Urja")
    malay = Follower("Malay")
    ankit = Follower("Ankit")
    harsh = Follower("Harsh")
    
    jhon_snow.register(amar)
    jhon_snow.register(juhi)
    jhon_snow.register(urja)
    
    selena_gomez.register(malay)
    selena_gomez.register(ankit)
    selena_gomez.register(harsh)
    
    jhon_snow.tweet("Hey guys, came across this interesting trailer, check it out.")
    selena_gomez.tweet("Good Morning..!!")
    
    jhon_snow.unregister(juhi)
    
    jhon_snow.tweet("Teaser of Secret Superstar has been released..!!")
