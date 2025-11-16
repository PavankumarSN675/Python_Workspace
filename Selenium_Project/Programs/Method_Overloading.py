
class MathOperations:
    def add(self, x, y=None, z=None):
        if y != None and z != None:
            return x + y + z
        elif y != None:
            return x + y
        else:
            return x

# Example Usage
math_obj = MathOperations()
result1 = math_obj.add(x=5)
result2 = math_obj.add(x=5, y=10)
result3 = math_obj.add(x=5, y=10, z=15)

# Output
print(result1)
print(result2)
print(result3)