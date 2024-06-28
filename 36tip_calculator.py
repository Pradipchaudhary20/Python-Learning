#tip calculator
#Write a script that calculates the tip amount based on the bill total and desired tip percentage entered by the user.

bill_amount = float(input(f"Enter the total bill amount:  "))
desired_tip = float(input(f"Enter the desired tip amount in percentage:  "))
tip_amount = bill_amount * (desired_tip/100)
total_amount = tip_amount + bill_amount

print(f"The tip amount of Rs {bill_amount} is Rs{tip_amount: .2f}")
print(f"The total amount to pay is {total_amount: .2f}")

