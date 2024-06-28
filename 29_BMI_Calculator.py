# BMI calculator 

#formula fo BMI = weight in kg/height in meters * height in meters

age = int(input(f"Enter your age: "))
weight = float(input(f"Enter your weight in kg:  "))
height = float(input(f"Enter your height in meters square:  "))

BMI = weight /(height **2)

if age < 18:
    if BMI < 18.5:
        print(f"Your BMI of {BMI:.2f} indicates underweight for your age.")
    elif 18.5 <= BMI < 25:
        print(f"Your BMI of {BMI:.2f} is within the normal range for your age.")
    elif 25 <= BMI < 30:
        print(f"Your BMI of {BMI:.2f} indicates overweight for your age.")
    else:
        print(f"Your BMI of {BMI:.2f} indicates obesity for your age.")
else:
    if BMI < 18.5:
        print(f"Your BMI of {BMI:.2f} indicates underweight.")
    elif 18.5 <= BMI < 25:
        print(f"Your BMI of {BMI:.2f} is within the normal range.")
    elif 25 <= BMI < 30:
        print(f"Your BMI of {BMI:.2f} indicates overweight.")
    else:
        print(f"Your BMI of {BMI:.2f} indicates obesity.")

