# ✅ 1. Write to a file (overwrite existing content)
# Writing to a file (this will overwrite the file)
with open("sample.txt", "w") as file:
    file.write("Hello, this is a new file content.\n")
    file.write("This line will also be written.")
# ------------------------------------------------------------------------

# ✅ 2. Append to a file (add new content without deleting old content)
# Appending to a file
with open("sample.txt", "a") as file:
    file.write("\nThis line is appended to the file.")

#--------------------------------------------------------------------------

# ✅ 3. Write multiple lines (using a list)
lines = [
    "First line\n",
    "Second line\n",
    "Third line\n"
]
with open("sample.txt", "w") as file:
    file.writelines(lines)

# ---------------------------------------------------------------------------
# ✅ 4. Write using exception handling
try:
    with open("sample.txt", "w") as file:
        file.write("Writing with exception handling.")
except Exception as e:
    print("Error:", e)