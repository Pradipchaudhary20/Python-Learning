## create function that find square of number

# def square():
#     num = float(input(f'Enter Number: '))
#     result = num * num
#     print(f"The square is {result}")

# square()

import math

# sq_root = math.sqrt(25)
# print(sq_root)

# n3 = math.pow(2,3)
# print(n3)

#create function that round number
## enter number = 2.11
## Round is : 3

def round_nuber(n):
    round_num = round(n)
    print(f"Round number is {round_num}")
ask_input = float(input("Enter the number: "))
round_nuber(ask_input)
