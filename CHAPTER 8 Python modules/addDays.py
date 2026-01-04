# Write a program that asks the user to enter a date string with a format of dd.mm.yyyy, and a number of days. Store the input date to a variable called input_date and the number of days to add_day. The program then converts the input_date string to a datetime object, and calculates the future date by adding the add_day. Finally, convert the new date into a readable string, and store it to a variable called new_date.

# Example run:

# Enter a date:
# 20.10.2025
# Enter a number of days:
# 20
# The new date is: 09.11.2025

from datetime import timedelta, date, datetime
input_date = input("Enter a date: ")
add_day = int(input("Enter a number of days: "))
format = "%d.%m.%Y"
date = datetime.strptime(input_date, format)
future_date = date + timedelta(days=add_day)
new_date = future_date.strftime(format)
print(f"The new date is: {new_date}")