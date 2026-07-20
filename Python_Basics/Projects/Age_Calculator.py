"""
Project: Age Calculator

Statement Question:
Create a Python program (without using a function) that asks the user for their birth year
and calculates their current age.

What you have to do:
1. Ask the user to enter their name.
2. Ask the user to enter their birth year.
3. Store the current year in a variable (example: 2026).
4. Calculate age using:
	age = current_year - birth_year
5. Print a clear message with the user's name and age.

Extra challenge (optional):
- Also ask if the user has had their birthday this year (yes/no).
- If no, subtract 1 from age.

Sample Input:
Name: Anika
Birth year: 2008

Sample Output:
Hello Anika, you are 18 years old.
"""

print("------Hello User-------")
name = input("Tell me your name : ")
birth_year = int(input("Whats your birth year(Birth should be less than 2026) ? :"))
current_year = 2026
if birth_year > current_year or birth_year <= 0:
    print("Input is invalid")
else :
    print("------Guessing your age------")
    age = current_year - birth_year
    print(f"Hello {name}, you are {age} years old")
    validation = input("Is the shown age correct? : ")
    if validation == "yes" or validation == "Yes":
        print("Thanks for the validation")
    if validation == "no" or validation == "No" :
        age -= 1
        print(f"This should be correct : {age}")





