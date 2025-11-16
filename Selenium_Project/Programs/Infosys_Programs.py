"""
1) Print the below pattern
*********
 ********
  *******
   ******
    *****
     ****
      ***
       **
        *
"""
n = 10
for i in range(n):
    for k in range(i):
        print(" ", end="")
    for j in range(i+1, n):
        print("*", end="")
    print("\n")

"""
2) Write a program to print Fabinocci series numbers
"""
n = 10
num1 = 0
num2 = 1
print(num1,num2, end=" ")
for i in range(2, n):
    num3 = num1 + num2
    print(num3, end=" ")
    num1 = num2
    num2 = num3