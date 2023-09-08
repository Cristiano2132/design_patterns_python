# Decorator Pattern

The **Decorator Pattern** is a structural design pattern that allows you to dynamically add behaviors or responsibilities to objects without altering their code. This pattern is a part of the Gang of Four (GoF) design patterns and is particularly useful when you need to extend the functionality of a class in a flexible and reusable way.

## Definition

At its core, the Decorator Pattern involves the use of decorators, which are classes that wrap around existing classes or objects, adding new functionality to them. These decorators implement the same interface as the objects they decorate, ensuring that they can be used interchangeably.

## When to Use

You should consider using the Decorator Pattern when:

1. **You want to add responsibilities to objects dynamically**: If you have a set of core functionalities, but you want to add optional features to them without modifying their source code, the Decorator Pattern can help.

2. **You want to avoid a class explosion**: Instead of creating a multitude of subclasses to accommodate all possible combinations of features, you can use decorators to mix and match functionalities as needed.

3. **You need to support both composition and inheritance**: The Decorator Pattern allows you to compose objects with various behaviors at runtime while avoiding the complexities of multiple inheritance.

## SOLID Principles

The Decorator Pattern adheres to several SOLID principles:

1. **Single Responsibility Principle (SRP)**: Each decorator class has a single responsibility, which is to add one specific feature to the object. This keeps classes focused on a single task.

2. **Open/Closed Principle (OCP)**: The pattern is open for extension but closed for modification. You can add new decorators to introduce new functionality without altering existing code.

## Similar Patterns and Differences

- **Adapter Pattern**: While the Decorator Pattern focuses on adding new functionalities to objects, the Adapter Pattern allows two incompatible interfaces to work together.

- **Composite Pattern**: The Composite Pattern also involves composing objects, but it's used to create tree-like structures where individual objects and compositions of objects are treated uniformly.

## Examples

Let's explore three examples of applying the Decorator Pattern in Python:

### [Example 1: Text Formatting](01_text_formatting.py)

**Context**: You have a text processing system that can format plain text. However, you want to enhance it with the ability to add features like bold, italic, and underline formatting.


### [Example 2: Coffee Shop](02_coffee_shop.py)
**Context:**

In this example, we are simulating a coffee shop application where customers can order various types of coffee with optional condiments. The objective is to use the Decorator Design Pattern to model and implement this system in Python.

**Problem Description:**

The coffee shop offers different types of coffee (e.g., plain coffee) and allows customers to add condiments like sugar, milk, or vanilla to their coffee orders. Each condiment has an associated cost, and the coffee shop needs to calculate the total cost of a coffee order, including any added condiments. Additionally, the coffee shop needs to calculate the sales tax on each order.

**Objective:**

1. Create a flexible and extensible system where customers can customize their coffee orders with various condiments.
2. Calculate the total cost of a coffee order, considering the base cost of the coffee and the cost of added condiments.
3. Calculate the sales tax on each order, which is 10% of the total cost.


### [Example 3: Value Operations](03_value_operations.py)

**Context**

In this example, we are designing a system for performing basic value operations like addition and subtraction using the Decorator Design Pattern. We have a custom class called Value that can hold a numerical value. We want to extend this class to support operations such as addition and subtraction using decorators.

**Problem Description**

We need to create a flexible and extensible system for performing value operations on numbers. The system should allow us to add or subtract values, and these operations can be applied to integers, custom Value objects, or other Add and Sub decorators. The goal is to create a modular and recursive system for value operations.

**Objective**

1. Create a custom Value class that can hold a numerical value.
2. Implement decorators for addition (Add) and subtraction (Sub) operations on values.
3. Ensure that the Add and Sub decorators can accept integers directly, custom Value objects, or other Add and Sub decorators.
4. Implement value operations recursively, allowing complex expressions like (A + B) - (C + D), where A, B, C, and D can be integers, custom Value objects, or other value expressions.
5. Provide a way to obtain the final result of a value expression as a string.

