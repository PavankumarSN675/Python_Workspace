"""
🔹 What is Abstraction?

Abstraction is an OOP concept where we hide implementation details and expose only the essential features to the user.

It helps to focus on what an object does instead of how it does it.

📌 Example in real life:

When you drive a car, you only use the steering, accelerator, brakes.

You don’t need to know how the engine, fuel injection, or transmission works internally → that’s abstraction.

🔹 Abstraction in Python

In Python, abstraction is mainly implemented using Abstract Classes and Abstract Methods, which are provided by the abc module.

Abstract Class → A class that cannot be instantiated (you cannot create objects directly).

Abstract Method → A method declared but not defined (must be implemented in child class).
"""

"""
🔹 Example 1: Abstract Class with Abstract Method
"""
from abc import ABC, abstractmethod

class Animal(ABC):  # Abstract Class
    @abstractmethod
    def sound(self):   # Abstract Method
        pass

class Dog(Animal):   # Subclass
    def sound(self):
        return "Bark"

class Cat(Animal):   # Subclass
    def sound(self):
        return "Meow"


# animal = Animal()  # ❌ Error: Can't instantiate abstract class
dog = Dog()
cat = Cat()

print(dog.sound())  # ✅ Bark
print(cat.sound())  # ✅ Meow


"""
🔹 Example 2: Abstraction with Multiple Methods
"""
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        return "Car engine started"

    def stop_engine(self):
        return "Car engine stopped"

class Bike(Vehicle):
    def start_engine(self):
        return "Bike engine started"

    def stop_engine(self):
        return "Bike engine stopped"


car = Car()
bike = Bike()

print(car.start_engine())  # Car engine started
print(bike.stop_engine())  # Bike engine stopped


"""
🔹 Example 3: Partial Abstraction
"""
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    def description(self):
        return "This is a shape"

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


rect = Rectangle(5, 3)
print(rect.description())  # ✅ Normal method from abstract class
print(rect.area())         # ✅ Implemented method → 15
