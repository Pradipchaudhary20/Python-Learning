# Birth date finder
from datetime import datetime
birth_year = int(input(f"Enter your  Birth year:  "))
current_year = datetime.now().year
age_find = current_year- birth_year
print(f"Your age is {age_find}")