# NPR = float(input("Enter The Currency in Nepali : "))

# currency_rate = {
#     'USD': 0.0075,
#     'JPY': 1.19,
#     'AUD' :0.011,
#     'EUR': 0.007
# }

# target_currency = input("Enter the Target Currency (USD,JPY,AUD,EUR): ").upper()

# if target_currency in currency_rate:
#     converted_amount = NPR * currency_rate[target_currency]
#     print(f"The converted amount in {target_currency} is {converted_amount: .2f}")
# else:
#     print(f" The Conversion rate for {target_currency} is not available")

Base_currency = input("Enter The Currency USD,NPR,AUD,JPY,EUR:  ").upper()
amount = float(input(f"Enter the amount in {Base_currency}: "))

currency_rate = {
        'NPR': {'USD': 0.0075, 'JPY': 1.19, 'AUD': 0.011, 'EUR': 0.007},
        'USD': {'NPR': 133.33, 'JPY': 133.17, 'AUD': 1.45, 'EUR': 0.93},
        'JPY': {'NPR': 0.84, 'USD': 0.0075, 'AUD': 0.011, 'EUR': 0.0069},
        'AUD': {'NPR': 91.13, 'USD': 0.69, 'JPY': 88.91, 'EUR': 0.64},
        'EUR': {'NPR': 142.86, 'USD': 1.08, 'JPY': 145.55, 'AUD': 1.57}
    }

target_currency = input("Enter the Target Currency (USD,JPY,AUD,EUR,NPR): ").upper()

if Base_currency in currency_rate and target_currency:
    converted_amount = amount * currency_rate[Base_currency][target_currency]
    print(f"The converted amount in {target_currency} is {converted_amount: .2f}")
    print(f"Thanks for using our currency converter !")
else:
    print(f" The Conversion rate for {target_currency} is not available")
    
