"""
What is Encapsulation?

Encapsulation is one of the core OOPs (Object-Oriented Programming) concepts.

It means wrapping data (variables) and methods (functions) into a single unit (class).

It also provides data hiding → controlling access to variables and methods.

In Python, we achieve encapsulation mainly using access modifiers:

Public members → accessible everywhere.

Protected members (_var) → should not be accessed directly (but still can be).

Private members (__var) → name-mangled, cannot be accessed directly outside the class.
"""
"""
Example 1: Basic Encapsulation with Public Members
"""
class Car:
    def __init__(self, brand, model):
        self.brand = brand        # public variable
        self.model = model

    def display_info(self):
        print(f"Car: {self.brand} {self.model}")


car1 = Car("Tesla", "Model S")
car1.display_info()       # ✅ Accessible
print(car1.brand)         # ✅ Accessible (public)


"""
Example 2: Encapsulation with Protected Members
"""
class Employee:
    def __init__(self, name, salary):
        self._name = name         # protected variable
        self._salary = salary     # protected variable

    def show_details(self):
        print(f"Employee: {self._name}, Salary: {self._salary}")


emp = Employee("John", 50000)
emp.show_details()
print(emp._salary)   # ⚠️ Accessible, but not recommended (by convention)


"""
Example 3: Encapsulation with Private Members
"""
class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number   # private variable
        self.__balance = balance                 # private variable

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited: {amount}, New Balance: {self.__balance}")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: {amount}, Remaining Balance: {self.__balance}")
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance


account = BankAccount("123456789", 1000)
account.deposit(500)
print(account.get_balance())     # ✅ Correct way

# ❌ Direct access will fail
# print(account.__balance)       # AttributeError

# ✅ But Python allows name mangling (_ClassName__var)
print(account._BankAccount__balance)  # Not recommended
