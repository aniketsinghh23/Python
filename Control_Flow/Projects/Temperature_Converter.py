print("Temperature Converter")

# Ask the user for the temperature value
temperature = float(input("Enter the temperature: "))

# Ask which conversion to perform
choice = input("Convert to (C)elsius or (F)ahrenheit? ").upper()

# Convert the temperature based on the choice
if choice == "C":
	converted = (temperature - 32) * 5 / 9
	print("Temperature in Celsius:", converted)
elif choice == "F":
	converted = (temperature * 9 / 5) + 32
	print("Temperature in Fahrenheit:", converted)
else:
	print("Invalid choice. Please enter C or F.")
