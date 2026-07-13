"""

Python Data Types
-----------------
Data types tell Python what kind of value a variable is storing.

Common built-in data types:
1. int      -> Whole numbers (e.g., 10, -3)
2. float    -> Decimal numbers (e.g., 3.14, -0.5)
3. str      -> Text (e.g., "Hello")
4. bool     -> True or False
5. list     -> Ordered, changeable collection [1, 2, 3]
6. tuple    -> Ordered, unchangeable collection (1, 2, 3)
7. set      -> Unordered collection of unique values {1, 2, 3}
8. dict     -> Key-value pairs {"name": "Anika", "age": 20}
9. NoneType -> No value (None)

"""

print("=== Python Data Types Example ===")

# int: whole numbers
age = 18
print("int:", age, "| type:", type(age))

# float: decimal numbers
price = 99.99
print("float:", price, "| type:", type(price))

# str: text
name = "Anika"
print("str:", name, "| type:", type(name))

# bool: true or false
is_student = True
print("bool:", is_student, "| type:", type(is_student))

# list: ordered and changeable
marks = [85, 90, 88]
print("list:", marks, "| type:", type(marks))

# tuple: ordered and unchangeable
coordinates = (10, 20)
print("tuple:", coordinates, "| type:", type(coordinates))

# set: unordered and unique values only
unique_numbers = {1, 2, 2, 3, 4}
print("set:", unique_numbers, "| type:", type(unique_numbers))

# dict: key-value pairs
student_info = {"name": "Anika", "age": 18, "course": "Python"}
print("dict:", student_info, "| type:", type(student_info))

# NoneType: no value
middle_name = None
print("NoneType:", middle_name, "| type:", type(middle_name))

