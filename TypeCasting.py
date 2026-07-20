"""
Type Casting in Python
----------------------
Type casting means converting one data type into another data type.

Example:
- Convert "25" (string) to 25 (integer) using int().
- Convert 10 (integer) to 10.0 (float) using float().
"""

print("=== Type Casting Example ===")

# String to int
age_text = "25"
age_number = int(age_text)
print("String to int:", age_text, "->", age_number, "| type:", type(age_number))

# Int to float
count = 10
count_float = float(count)
print("Int to float:", count, "->", count_float, "| type:", type(count_float))

# Float to int (decimal part is removed, not rounded)
price = 99.75
price_int = int(price)
print("Float to int:", price, "->", price_int, "| type:", type(price_int))

# Int to string
year = 2026
year_text = str(year)
print("Int to string:", year, "->", year_text, "| type:", type(year_text))

# Boolean casting
print("bool(0):", bool(0))
print("bool(1):", bool(1))
print("bool(''):", bool(""))
print("bool('Python'):", bool("Python"))
