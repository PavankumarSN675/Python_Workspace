# Program 1: Read entire file
# Reading entire file content
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)

# Program 2: Read file line by line
# Reading file line by line
with open("sample.txt", "r") as file:
    for line in file:
        print(line.strip())

# Program 3: Read file into a list of lines
with open("sample.txt", "r") as file:
    lines = file.readlines()
    print(lines)

"""
Explanation

open("sample.txt", "r") → Opens the file in read mode.

with → Automatically closes the file after use.

file.read() → Reads whole content.

file.readlines() → Returns a list of lines.

for line in file → Iterates line by line efficiently.
"""