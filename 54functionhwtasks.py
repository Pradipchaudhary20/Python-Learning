#create a function that generate random password
## option: use parameter for no of character in password

import random
alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet_upper = alphabet.upper()
number = '1234567890'
symbols = '!@#$%^&*'

all_combine = alphabet + alphabet_upper + number + symbols
all_combine_to_list = list(all_combine)
# print(all_combine_to_list)

def password_generator(length):
    password = ''.join(random.choice(all_combine_to_list) for i in range(length))
    print(f"Generated Password is: {password}")

password_generator(8)




