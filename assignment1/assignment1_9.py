weight = float(input("enter your weight in kilograms: "))
height = float(input("enter your height in metres: "))

BMI = weight / (height**2)

if BMI < 18.5:
    print("underweight")
if  18.5 < BMI < 24.9:
    print("normal")
if 25 < BMI < 29.9:
    print("overweight")
if 30 < BMI < 34.9:
    print("obese")
if BMI > 35:
    print("extremly obese")
