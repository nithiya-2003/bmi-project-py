# Get weight from user
weight = float(input("Enter your weight (in kg): "))

# Get height from user
height = float(input("Enter your height (in m): "))

# Calculate BMI
bmiw = weight / (height ** 2)

# Round BMI to one decimal place
bmiw = round(bmiw, 1)

# Print BMI
print(f"Your BMI is {bmiw}!")

# Determine weight category
if bmiw < 18.0:
    print(f"You are underweight. Your BMI is {bmiw}.")
elif 18.0 <= bmiw <= 24.9:
    print(f"You are healthy. Your BMI is {bmiw}.")
elif 25.0 <= bmiw <= 29.9:
    print(f"You are overweight. Your BMI is {bmiw}.")
else:
    print(f"You are obese. Your BMI is {bmiw}.")
