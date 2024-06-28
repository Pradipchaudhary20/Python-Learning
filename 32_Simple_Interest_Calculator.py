# Simple interest calculator

Principal = int(input(f"Enter the Principal Amount: "))
Time = float(input(f"Enter the Time Period: "))
Rate = float(input(f"Enter the rate: "))

Interest =  (Principal * Time * Rate)/100

print(f"The Interest Amount is {Interest}  ")

