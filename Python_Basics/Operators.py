"""
Python Operators
----------------
Operators are symbols used to perform operations on values and variables.
"""

print("=== Python Operators Example ===")

# -------------------------------------------------
# 1) Arithmetic Operators
# Used for basic math calculations.
# -------------------------------------------------
a = 10
b = 3

print("\nArithmetic Operators")
print("a + b =", a + b)  # Addition
print("a - b =", a - b)  # Subtraction
print("a * b =", a * b)  # Multiplication
print("a / b =", a / b)  # Division (returns float)
print("a // b =", a // b)  # Floor division (whole number part)
print("a % b =", a % b)  # Modulus (remainder)
print("a ** b =", a ** b)  # Exponent (power)

# -------------------------------------------------
# 2) Comparison Operators
# Used to compare two values; result is True or False.
# -------------------------------------------------
print("\nComparison Operators")
print("a == b:", a == b)  # Equal to
print("a != b:", a != b)  # Not equal to
print("a > b:", a > b)  # Greater than
print("a < b:", a < b)  # Less than
print("a >= b:", a >= b)  # Greater than or equal to
print("a <= b:", a <= b)  # Less than or equal to

# -------------------------------------------------
# 3) Assignment Operators
# Used to assign and update variable values.
# -------------------------------------------------
print("\nAssignment Operators")
x = 5
print("x =", x)

x += 2  # Same as x = x + 2
print("x += 2 ->", x)

x *= 3  # Same as x = x * 3
print("x *= 3 ->", x)

x -= 4  # Same as x = x - 4
print("x -= 4 ->", x)

# -------------------------------------------------
# 4) Logical Operators
# Used with boolean values.
# -------------------------------------------------
print("\nLogical Operators")
p = True
q = False

print("p and q:", p and q)  # True only if both are True
print("p or q:", p or q)  # True if at least one is True
print("not p:", not p)  # Opposite value

# -------------------------------------------------
# 5) Membership Operators
# Check if a value is inside a sequence.
# -------------------------------------------------
print("\nMembership Operators")
numbers = [1, 2, 3, 4]

print("2 in numbers:", 2 in numbers)  # True if present
print("9 not in numbers:", 9 not in numbers)  # True if absent

# -------------------------------------------------
# 6) Identity Operators
# Check if two variables refer to the same object in memory.
# -------------------------------------------------
print("\nIdentity Operators")
list1 = [1, 2]
list2 = [1, 2]
list3 = list1

print("list1 is list2:", list1 is list2)  # Usually False (different objects)
print("list1 is list3:", list1 is list3)  # True (same object)
print("list1 is not list2:", list1 is not list2)
