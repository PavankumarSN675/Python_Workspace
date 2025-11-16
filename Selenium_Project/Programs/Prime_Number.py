
number = 7

for i in range(2,number):
    if number % i == 0:
        print("Given number is not a prime number")
        break

else:
    print("Given number is a prime number")