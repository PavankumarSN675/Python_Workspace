
# Palindrome program for number
num = 123321
original_num = num
reverse_num = 0
while num > 0:
    remainder = num % 10
    reverse_num = reverse_num * 10 + remainder
    num = num // 10

print(reverse_num , original_num)
if original_num == reverse_num:
    print("Given number is Palindrome.")
else:
    print("Given number is not a palindrome.")

# Palindrome program for string
string = "malayalam"
print(string[::-1])
original_string = string
reverse_string = ""
for char in original_string:
    if char != " ":
        reverse_string += char

if original_string == reverse_string:
    print("Given string is Palindrome.")
else:
    print("Given string is not Palindrome.")