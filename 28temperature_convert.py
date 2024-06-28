# converting the temperature

Unit_Temperature = input(f"Enter the Unit Name (Celsius , Fahrenheit and Kelvin): ").capitalize()
Temperature = float(input(f"Enter the temparature in {Unit_Temperature}: "))

# Celsius_to_fahrenheit = Temperature * 9/5 +32
# fahrenheit_to_celsius = (Temperature-32)*5/9
# celsius_to_kelvin = Temperature +273.2
# kelvin_to_celsius= Temperature - 273.2
# Fahrenheit_to_Kelvin = (Temperature - 32) *5/9 +27315
# kelvin_to_fahrenheit = (Temperature-273.15) *9/5 + 32


if Unit_Temperature == 'Celsius':
    celsius_to_fahrenheit = Temperature * 9/5 + 32
    celsius_to_kelvin = Temperature + 273.15
    print(f"{Temperature} degrees Celsius is {celsius_to_fahrenheit} degrees Fahrenheit.")
    print(f"{Temperature} degrees Celsius is {celsius_to_kelvin} Kelvin.")
elif Unit_Temperature == 'Fahrenheit':
    fahrenheit_to_celsius = (Temperature - 32) * 5/9
    fahrenheit_to_kelvin = (Temperature - 32) * 5/9 + 273.15
    print(f"{Temperature} degrees Fahrenheit is {fahrenheit_to_celsius} degrees Celsius.")
    print(f"{Temperature} degrees Fahrenheit is {fahrenheit_to_kelvin} Kelvin.")
elif Unit_Temperature == 'Kelvin':
    kelvin_to_celsius = Temperature - 273.15
    kelvin_to_fahrenheit = (Temperature - 273.15) * 9/5 + 32
    print(f"{Temperature} Kelvin is {kelvin_to_celsius} degrees Celsius.")
    print(f"{Temperature} Kelvin is {kelvin_to_fahrenheit} degrees Fahrenheit.")
else:
    print("Invalid unit name. Please enter Celsius, Fahrenheit, or Kelvin.")


