import datetime
import datetime_nepali
year = int(input(f"Enter the year: "))
month = int(input(f"Enter the month: "))
day = int(input(f"Enter the day: "))
nepali_date = datetime_nepali.date.from_datetime_date(datetime.date(year, month, day))
print(f"Nepali date: {nepali_date}")



