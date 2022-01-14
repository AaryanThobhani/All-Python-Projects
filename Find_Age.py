import calendar
from datetime import date

birth_year = 2009
today = date.today()

age = today.year - birth_year
print(age)