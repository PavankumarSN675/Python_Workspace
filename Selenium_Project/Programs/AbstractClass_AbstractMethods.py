from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def add(self):
        pass

class B(A):
    def add(self):
        print("A")

obj = B()
obj.add()