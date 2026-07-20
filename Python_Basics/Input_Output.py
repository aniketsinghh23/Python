"""

f is called an f-string, which means:
"Formatted String Literal"
Let's break that down:
Formatted → Python will replace variables inside {} with their values.
String → It's text.
Literal → The string is written directly in your code.

example code :
age = 23
print(f"Age-->{age}")

"""
number = {1,2,3,3,4,5} #This is a set 
print("Number-->",number)
# ------- OR --------
print(f"Number-->{number}")


age = 23
print("Age-->",age)
#-------OR--------
print(f"Age-->{age}")

#Taking Input from User

a = int(input("Give me a number-->"))
b = int(input("Give me a second number-->"))
#Giving Output to a user
print(f"Addition--> {a+b}")
