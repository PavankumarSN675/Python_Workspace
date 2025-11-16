"""
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