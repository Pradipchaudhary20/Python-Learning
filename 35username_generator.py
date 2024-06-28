# username generator
import random
first_name = input(f"Enter your  firstname: ")
last_name = input(f"Enter your  lastname: ")
fav_number = input(f"Enter your favorite Number: ")

username = first_name + last_name + fav_number
random_number = random.randint(100, 999)
unique_username = username + str(random_number)
print(f"The generated username is: {unique_username}")