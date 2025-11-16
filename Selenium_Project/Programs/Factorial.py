
# Using recursive method to find the factorial of an input number
def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number-1)

print(factorial(5))

# Using for loop to find the factorial of an input number
num = 5
fact = 1
for i in range(1, num+1):
    fact = fact * i

print(fact)