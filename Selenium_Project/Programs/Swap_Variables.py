# Approach 1
a = 10
b = 20
temp = a
a = b
b = temp
print(a)
print(b)

# Approach 2
a = 10
b = 20
a, b = b, a
print(a)
print(b)

# Approach 3
a = 10
b = 20
a = a + b
b = a - b
a = a - b
print(a)
print(b)