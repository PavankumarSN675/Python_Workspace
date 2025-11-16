"""
1) Occurrences of each value
"""
list = [1, 2, 2, 2, 4, 3, 4, 3, 5, 6, 7]
tuple = (1, 2, 2, 2, 4, 3, 4, 3, 5, 6, 7)
print(tuple)
for i in list:
    counter = 0
    for j in list:
        if i == j:
            counter = counter + 1
    print(f"{i} repeated: {counter} times")

"""
2) Page Object Model Design

Project:
    Configs:
        config.ini
    PagePackages:
        login_page.py
          launch()
          enter_uname()
          enter_password()
          click_ok()
    features:
        step_definition:
            login_steps.py
        login.feature
"""

"""
3) Find the pairs whose sum is input sum(target)
"""
list = [2, 6, 4, 7, 10]
target = 10

for i in list:
    for j in list:
        if i + j == target:
            print(f"Pair present {i} and {j} in the list whose sum is {target}")


"""
4) Swap variable without using external variable
"""
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



