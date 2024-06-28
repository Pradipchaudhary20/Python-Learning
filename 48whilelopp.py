atm_pin = '1456'
user_pin = ''
attempt = 0
max_attempts = 5

while atm_pin != user_pin:
    if attempt > 0:
        print(f"Invalid Pin code. Total Attempt {attempt}")
    
    if attempt >= max_attempts:
        print("You are blocked")
        break
    
    user_pin = input("Enter ATM Pin: ")
    attempt += 1
else:
    print("Access Granted. How much do you want to withdraw?")
