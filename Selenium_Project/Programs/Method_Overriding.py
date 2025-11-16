
class A:
    def __init__(self):
        pass

    def show(self):
        print("Hello A show")

class B(A):
    def __init__(self):
        super().__init__()

    def show(self):
        print("Hello B show")

obj_b = B()
obj_b.show()