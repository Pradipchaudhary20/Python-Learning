

number1 = float(input(f"Enter the first number: "))
number2 = float(input(f"Enter the second number: "))

arithmetic_operations = input("Enter the Operations you want to perform(add, sub, mul, and div): ")

if arithmetic_operations =='add':
    sum = number1+number2
    print(f"The Sum is {sum}")
elif arithmetic_operations =='sub':
    sub = number1 - number2
    print(f"The sub is {sub}")
elif arithmetic_operations == 'mul':
    mul = number1 * number2
    print(f"The mul is {mul}")
elif arithmetic_operations == 'div':
    div = number1 / number2
    print(f"The divison is {div}")
else:
    print(f"Invalid Operations Selections")
