"""
🔹 What is Inheritance?

Inheritance is an OOP concept where a class (child/derived class) can reuse properties and methods of another class (parent/base class).

It promotes code reusability, extensibility, and modularity.

📌 Real-world example:

A Car is a type of Vehicle.

Car inherits generic features from Vehicle (wheels, engine) but adds specific ones (airbags, music system).

🔹 Types of Inheritance in Python

Single Inheritance – One child inherits from one parent.

Multiple Inheritance – One child inherits from multiple parents.

Multilevel Inheritance – A child inherits from a parent, and another child inherits from it (a chain).

Hierarchical Inheritance – Multiple children inherit from the same parent.

Hybrid Inheritance – Combination of multiple inheritance types.
"""

"""
🔹 Example 1: Single Inheritance
"""
class Parent:
    def show(self):
        print("This is the Parent class")

class Child(Parent):
    def display(self):
        print("This is the Child class")

c = Child()
c.show()      # Inherited from Parent
c.display()   # Defined in Child


"""
🔹 Example 2: Multiple Inheritance
"""
class Father:
    def skill(self):
        print("Father's skill: Driving")

class Mother:
    def skill(self):
        print("Mother's skill: Cooking")

class Child(Father, Mother):
    def hobby(self):
        print("Child's hobby: Painting")

c = Child()
c.skill()   # Prints "Father's skill: Driving" (Method Resolution Order - MRO)
c.hobby()


"""
🔹 Example 3: Multilevel Inheritance
"""
class Grandparent:
    def house(self):
        print("Grandparent's house")

class Parent(Grandparent):
    def car(self):
        print("Parent's car")

class Child(Parent):
    def bike(self):
        print("Child's bike")

c = Child()
c.house()  # Inherited from Grandparent
c.car()    # Inherited from Parent
c.bike()   # Defined in Child


"""
🔹 Example 4: Hierarchical Inheritance
"""
class Parent:
    def property(self):
        print("Parent's property")

class Child1(Parent):
    def car(self):
        print("Child1's car")

class Child2(Parent):
    def bike(self):
        print("Child2's bike")

c1 = Child1()
c2 = Child2()

c1.property()
c2.property()


"""
🔹 Example 5: Hybrid Inheritance
"""
class A:
    def feature1(self):
        print("Feature 1 from A")

class B(A):
    def feature2(self):
        print("Feature 2 from B")

class C(A):
    def feature3(self):
        print("Feature 3 from C")

class D(B, C):  # Hybrid (Multiple + Multilevel)
    def feature4(self):
        print("Feature 4 from D")

d = D()
d.feature1()
d.feature2()
d.feature3()
d.feature4()


"""
🔹 Using super() in Inheritance

super() is used to call parent class methods inside a child class.
"""
class Parent:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"Parent: {self.name}")

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Calls Parent constructor
        self.age = age

    def show(self):
        super().show()  # Calls Parent method
        print(f"Child: {self.name}, Age: {self.age}")

c = Child("John", 20)
c.show()
