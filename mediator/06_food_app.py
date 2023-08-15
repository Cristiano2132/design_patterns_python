# https://dev.to/jemaloqiu/design-pattern-in-python-6-mediator-pattern-b7d

import difflib
from abc import ABCMeta, abstractmethod
from typing import List

class IBasketInfo(metaclass=ABCMeta):
    @abstractmethod
    def get_location(self):
        pass

    @abstractmethod
    def get_address(self):
        pass

    @abstractmethod
    def get_shop_name(self):
        pass

    @abstractmethod
    def show_info(self, show_shop=True):
        pass

class IBasketShop(metaclass=ABCMeta):
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def set_basket_info(self, address, location, price):
        pass

    @abstractmethod
    def publish_basket_info(self, app):
        pass

class ICustomer(metaclass=ABCMeta):
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def find_basket(self, description, app):
        pass

    @abstractmethod
    def view_basket(self, basket_infos):
        pass

    @abstractmethod
    def buy_basket(self, basket_info, app):
        pass

class IMediator(metaclass=ABCMeta):
    @abstractmethod
    def add_basket_info(self, basket_info):
        pass

    @abstractmethod
    def remove_basket_info(self, basket_info):
        pass

    @abstractmethod
    def get_search_condition(self, description):
        pass

    @abstractmethod
    def get_match_infos(self, search_condition):
        pass

    @abstractmethod
    def add_basket(self, basket_info):
        pass

    @abstractmethod
    def add_baskets(self):
        pass

class BasketInfo(IBasketInfo):
    def __init__(self, location: str, price: float, address: str, shop: IBasketShop):
        self.__location = location
        self.__price = price
        self.__address = address
        self.__shop = shop

    def get_location(self):
        return self.__location

    def get_address(self):
        return self.__address

    def get_shop_name(self):
        return self.__shop.get_name()

    def show_info(self, show_shop=True):
        print(" ++ Location:", self.__location)
        print(" ++ Price:", str(self.__price) + " euros")
        print(" ++ Address:", self.__address)
        print(" ++ Shop:", self.get_shop_name() if show_shop else "")
        print()

def get_equal_rate(str1, str2):
    return difflib.SequenceMatcher(None, str1, str2).quick_ratio()

class BasketPlatformApp(IMediator):
    def __init__(self, name: str):
        self.__basket_infos: List[IBasketInfo] = []
        self.__name = name

    def get_name(self):
        return self.__name

    def add_basket_info(self, basket_info: IBasketInfo):
        self.__basket_infos.append(basket_info)

    def remove_basket_info(self, basket_info: IBasketInfo):
        self.__basket_infos.remove(basket_info)

    def get_search_condition(self, description: str):
        return description

    def get_match_infos(self, search_condition: str):
        print(self.get_name(), "shows suitable baskets for you:")
        suitables = []
        for info in self.__basket_infos:
            if get_equal_rate(search_condition, info.get_location()) > 0.9:
                info.show_info(False)
                suitables.append(info)
        return suitables

    def add_basket(self, basket_info: IBasketInfo):
        print(self.get_name(), "has a new available Basket\n -- Provided by", basket_info.get_shop_name(), "\n -- Located at:", basket_info.get_address())

    def add_baskets(self):
        for info in self.__basket_infos:
            self.add_basket(info)

class BasketShop(IBasketShop):
    def __init__(self, name: str):
        self.__name = name
        self.__basket_info: IBasketInfo = None

    def get_name(self):
        return self.__name

    def set_basket_info(self, address: str, location: str, price: float):
        self.__basket_info = BasketInfo(location, price, address, self)

    def publish_basket_info(self, app: IMediator):
        app.add_basket_info(self.__basket_info)
        print(self.get_name() + " pushes a Basket on", app.get_name() + ":")
        self.__basket_info.show_info()

class Customer(ICustomer):
    def __init__(self, name: str):
        self.__name = name

    def get_name(self):
        return self.__name

    def find_basket(self, description: str, app: IMediator):
        print("User", self.get_name() + ", searching a basket with info:", description)
        print()
        return app.get_match_infos(app.get_search_condition(description))

    def view_basket(self, basket_infos: List[IBasketInfo]):
        size = len(basket_infos)
        return basket_infos[size - 1]

    def buy_basket(self, basket_info: IBasketInfo, app: IMediator):
        print(self.get_name(), "made a new command on", app.get_name(), "for a basket in", basket_info.get_shop_name())

if __name__ == "__main__":
    print('# Food shops push available baskets to APP platform:')
    my_app = BasketPlatformApp("Too Good To Go")
    paul = BasketShop("Paul")
    paul.set_basket_info("La Defense Parvis 15, 92000, Haut-Seine", "4 temps commercial center", 3.99)
    paul.publish_basket_info(my_app)
    auchan = BasketShop("Auchan")
    auchan.set_basket_info("22 Rue Alma, 92240, Courbevoie", "Supermarket A2Pas", 4.0)
    auchan.publish_basket_info(my_app)
    sushi = BasketShop("Sushi Shop")
    sushi.set_basket_info("La Defense Parvis 15, 92000, Haut-Seine", "4 temps commercial center", 6.99)
    sushi.publish_basket_info(my_app)
    print('\n\n# Too good to Go updates its available baskets:')
    my_app.add_baskets()
    print('\n\n# A Too good to Go user searches and buys a food basket:')
    jemaloq = Customer("jemaloq")
    basket_infos = jemaloq.find_basket("4 temps commercial center", my_app)
    print("Searching available baskets for you…")
    appropriate_basket = jemaloq.view_basket(basket_infos)
    jemaloq.buy_basket(appropriate_basket, my_app)
