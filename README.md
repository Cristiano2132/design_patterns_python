<h1 align="center">Design Patterns</h1>

### 🏠 [Homepage](https://cristiano2132.github.io/)

## Prerequisites
* Python 3.10.10


## Cloning the repository

Open the terminal, go to the directory where you want to download the repository and clone it:

```bash
git clone git@github.com:Cristiano2132/design_patterns_python.git
```

## Virtual environment

Create a virtual environment

``` bash
python3.10 -m venv .venv
```


Active the virtual environment
``` bash
source .venv/bin/activate 
```



## Install the dependencies
``` bash
pip3 install -r requirements.txt
```

Certainly! Let's delve deeper into each of the three categories of design patterns: Creational Patterns, Structural Patterns, and Behavioral Patterns.

## Introduction to Design Patterns

Design patterns are reusable solutions to common software design problems. They provide a framework for solving specific issues that developers face while designing applications. Patterns capture design principles and best practices, enabling developers to create robust, maintainable, and flexible code.

## Types of Design Patterns

### Creational Patterns

Creational patterns focus on the process of object creation. They provide ways to control object instantiation and make it more flexible, efficient, and controlled.

- **Factory Method:** This pattern defines an interface for creating objects, but subclasses decide which class to instantiate. It allows for dynamic object creation while keeping the client code decoupled from the actual object creation logic.

- **Abstract Factory:** The abstract factory pattern provides an interface for creating families of related or dependent objects. It allows the creation of objects without specifying their concrete classes, supporting variations in the product families.

- **Singleton:** The singleton pattern ensures that a class has only one instance and provides a global point of access to that instance. It's commonly used for scenarios where a single instance needs to control actions across the system.

- **Builder:** The builder pattern separates the construction of complex objects from their representation, enabling the same construction process to create different representations. It's useful when dealing with objects that have many optional components.

### Structural Patterns

Structural patterns deal with how objects are composed to form larger structures. They focus on class composition and object relationships to achieve more flexible and efficient structures.

- **Adapter:** The adapter pattern allows objects with incompatible interfaces to work together by providing a wrapper that converts one interface into another. It enables collaboration between classes that wouldn't normally be compatible.

- **Decorator:** Decorator adds behavior or responsibilities to objects dynamically without affecting their structure. It allows for adding functionality to objects at runtime, offering a more flexible alternative to subclassing.

- **Facade:** The facade pattern provides a simplified interface to a complex system of classes, making it easier for clients to interact with the subsystem. It promotes loose coupling between clients and subsystems.

- **Proxy:** The proxy pattern provides a surrogate or placeholder for another object to control its access or add additional functionalities. It's often used to control access to sensitive or resource-intensive objects.

### Behavioral Patterns

Behavioral patterns focus on how objects communicate and interact with each other. They define communication patterns between objects and responsibilities distribution.

- **Observer:** The observer pattern defines a one-to-many dependency between objects. When one object changes state, all its dependents are notified and updated automatically. It's commonly used for event handling and notifications.

- **Strategy:** The strategy pattern defines a family of interchangeable algorithms and allows them to be selected and used dynamically at runtime. It enables easy substitution of algorithms without changing the client code.

- **Command:** The command pattern encapsulates a request as an object, allowing for parameterization of clients with different requests, queuing of requests, and logging of their execution.

- **Mediator:** The mediator pattern defines an object that encapsulates how a set of objects interact. It promotes loose coupling by centralizing communication between objects, thus reducing direct dependencies.

## Patterns in the Repository

Here's the list of design patterns covered in your repository, categorized by type:

### Creational Patterns:
- Factory Method
- Abstract Factory
- [Singleton](singleton/singleton.md)
- Builder

### Structural Patterns:
- Decorator
- [Adapter](adapter/adapter.md)

### Behavioral Patterns:
- [Observer](observer/observer.md)
- [Strategy](strategy/strategy.md)
- [Command](command/command.md)
- [Mediator](mediator/mediator.md)

Each pattern comes with an explanation and example files, helping developers understand and implement these design solutions effectively. Explore the individual pattern directories for more in-depth information and practical code examples.

## 🤝 Authors 

👤 [Cristiano Ferrreira de Oliveir](https://cristiano2132.github.io/)
