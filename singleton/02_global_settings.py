import random
import threading


class GlobalSettings:
    "GlobalSettings as a Singleton"
    __inited = False
    _instance = None
    _settings = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if type(self).__inited:
            return
        type(self).__inited = True
        self.value = random.randint(1, 100)
        
    def set_setting(self, key, value):
        "A class instance method to set a global setting"
        self._settings[key] = value

    def get_setting(self, key):
        "A class instance method to get a global setting"
        return self._settings.get(key, None)


class Application:
    "An example Application class"

    def __init__(self, name):
        self.name = name

    def configure(self, key, value):
        "Configure a global setting"
        global_settings = GlobalSettings()
        global_settings.set_setting(key, value)
        print(f"{self.name}: Setting '{key}' configured with value '{value}'")

    def run(self):
        "Run the application"
        global_settings = GlobalSettings()
        setting = global_settings.get_setting("theme")
        print(f"{self.name}: Running with theme '{setting}'")
        print(f"{self.name}: Running with language '{global_settings.get_setting('language')}'")
        print(f"{self.name}: Running with value '{global_settings.value}'\n")
       
def create_singleton_instances():
        s = GlobalSettings()
        print(f"Singleton instance created by thread {threading.current_thread().name}: {s} and value: {s.value}\n")


if __name__ == '__main__':
    # The Client
    # Multiple applications share and manage the same global settings because it is a singleton.
    app1 = Application("App1")
    app1.configure("theme", "dark")

    app2 = Application("App2")
    app2.configure("language", "en")

    app3 = Application("App3")
    app3.configure("theme", "light")

    app1.run()
    app2.run()
    app3.run()

    
    threads = []
    for i in range(5):
        t = threading.Thread(target=create_singleton_instances)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()