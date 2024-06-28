# Distance Calculator

# Asking the user for the distance parameter and the value to convert
distances = input("Select the parameter you want to convert (Km, M, Mi): ")
dis_convert = float(input(f"Enter the distance in {distances}: "))

# Conversion logic
if distances == 'Km':
    km_to_meter = dis_convert * 1000
    km_to_miles = dis_convert * 0.621371
    print(f"The distance of {dis_convert} Km in meters is {km_to_meter}")
    print(f"The distance of {dis_convert} Km in miles is {km_to_miles}")

elif distances == 'M':
    meter_to_km = dis_convert / 1000
    meter_to_miles = dis_convert / 1609.34
    # Corrected typo "miters" to "meters" and added proper spacing
    print(f"The distance of {dis_convert} meters in Km is {meter_to_km}")
    print(f"The distance of {dis_convert} meters in miles is {meter_to_miles}")

elif distances == 'Mi':
    miles_to_km = dis_convert * 1.60934
    miles_to_meters = dis_convert * 1609.34  # Corrected the conversion formula
    # Corrected spacing and grammar in print statements
    print(f"The distance of {dis_convert} miles in Km is {miles_to_km}")
    print(f"The distance of {dis_convert} miles in meters is {miles_to_meters}")

else:
    print("Please select a proper option (Km, M, Mi)")
