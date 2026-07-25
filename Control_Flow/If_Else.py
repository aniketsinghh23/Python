print("If Else Example")

# Ask the user for their age
age = int(input("Enter your age: "))

# if runs when the condition is true
if age >= 18:
	print("You are an adult.")

# elif checks another condition if the first one is false
elif age >= 13:
	print("You are a teenager.")

# else runs when none of the above conditions are true
else:
	print("You are a child.")
