number1 = int(input("Enter the number 1: "))
number2 = int(input("Enter the number 2: "))
number3 = int(input("Enter the number 3: "))

if number1 > number2 and number1 > number3:
    print(f"{number1} is great number")
elif number2 > number1 and number2 > number3:
    print(f"{number2} is great number")
elif number3 > number1 and number3 > number1:
    print(f"{number3} is great number")
else:
    print("Something went wrong")





