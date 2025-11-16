n = 10
num1 = 0
num2 = 1
print(num1,num2, end=" ")
for i in range(2, n):
    num3 = num1 + num2
    print(num3, end=" ")
    num1 = num2
    num2 = num3