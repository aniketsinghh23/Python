"""
Variables in Python
-------------------
A variable is a name used to store a value.
You can change the value of a variable later in the program.
"""

print("=== Variables Example ===")

# 1) Creating variables
name = "Anika"
age = 18
height = 5.4

print("Name:", name)
print("Age:", age)
print("Height:", height)

# 2) Updating (reassigning) a variable
age = 19
print("Updated Age:", age)

# 3) Multiple assignment in one line
x, y, z = 10, 20, 30
print("x:", x, "y:", y, "z:", z)

# 4) Same value to multiple variables
a = b = c = 100
print("a:", a, "b:", b, "c:", c)

# 5) Variable naming examples
student_name = "Ravi"   # Valid: uses underscore
marks1 = 95              # Valid: can include numbers (not at start)

print("Student Name:", student_name)
print("Marks:", marks1)

# Note:
# Invalid names look like: 1name, student-name, class (keyword)
