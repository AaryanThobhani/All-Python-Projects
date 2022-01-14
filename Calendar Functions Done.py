import calendar

print("All the weekheaders are printed out.")
print(calendar.weekheader(3))
print()

print("The first weekday number is printed out.")
print(calendar.firstweekday())
print()

print("The whole month is printed out.")
print(calendar.month(2020, 12))
print()

print("The month is printed out in matrix form.")
print(calendar.monthcalendar(2020, 12))
print()

print("The whole calendar is printed out.")
print(calendar.calendar(2020))
print()

print("This is to check how many leap days there are in between these years.")
print(calendar.leapdays(2000, 2020))
print()

print("This is to check if the year is a leap year or not.")
print(calendar.isleap(2020))
print()

print("This prints out all the days of the week")
for day in calendar.day_name:
	print(day)


print("This prints out all the months of the year.")
for month in calendar.month_name:
	print(month)
