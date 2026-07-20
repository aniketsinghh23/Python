"""
Ask the user for their weight and height, then calculate BMI using:
bmi = weight / (height * height)
Print the BMI value clearly.
"""

weight = float(input("What is your weight : "))
height = float(input("What is your height in meters : "))

bmi = weight / (height**2)
print(f"Your Bmi is {bmi:.2f}")

if bmi < 18.5:
    print("underweight")
elif bmi <= 25:
    print("healthy weight")
elif bmi < 29.5:
    print("overweight")
else:
    print("Obesity")