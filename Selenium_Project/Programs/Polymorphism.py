"""
🔹 What is Polymorphism?

Polymorphism means “many forms”.

In OOP, it allows the same function/method/operator to behave differently based on the object or data type.

📌 Real-world example:

The word “run” has many meanings:

You can run a program,

run a race,

run a company.

Same word → different behaviors depending on the context.

🔹 Types of Polymorphism in Python

Function Polymorphism → Same built-in function works differently for different data types.

Operator Overloading → Same operator (+, *, etc.) works differently for different objects.

Method Overriding (Runtime Polymorphism) → Subclass provides a specific implementation of a method defined in the parent class.

Method Overloading (Compile-time Polymorphism) → Not directly supported in Python, but can be achieved with default arguments or *args.
"""

"""
🔹 Example 1: Function Polymorphism
📌 The same function len() works differently for string, list, and dictionary.
"""
print(len("Python"))     # String → 6
print(len([1, 2, 3, 4])) # List → 4
print(len({"a": 1, "b": 2})) # Dictionary → 2


"""
🔹 Example 2: Operator Overloading
"""
# '+' works differently based on data type
print(10 + 5)        # Addition → 15
print("Hello " + "World")  # Concatenation → Hello World
print([1, 2] + [3, 4])     # List merge → [1, 2, 3, 4]


"""
🔹 Example 3: Method Overriding (Runtime Polymorphism)
📌 Output:

Bark
Meow
Some generic sound

Same method sound() behaves differently depending on the object.
"""
class Animal:
    def sound(self):
        return "Some generic sound"

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

animals = [Dog(), Cat(), Animal()]
for a in animals:
    print(a.sound())


"""
🔹 Example 4: Method Overloading (Simulated in Python)
Python does not support traditional method overloading (same method name, different parameters).
But we can simulate it using default arguments or *args.
📌 Here, add() works with different numbers of arguments → simulating overloading.
"""
class MathOps:
    def add(self, a=0, b=0, c=0):
        return a + b + c

m = MathOps()
print(m.add(5, 10))        # 15
print(m.add(1, 2, 3))      # 6
print(m.add())             # 0
