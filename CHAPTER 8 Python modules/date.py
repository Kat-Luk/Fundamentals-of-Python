#Write a program that uses datetime module to print out the current date and time in the same format as the example output below.
#Example output:
#The current date and time is 25-07-2025 14:38
from datetime import datetime
today = datetime.today()
format = today.strftime("%d-%m-%Y %H:%M")
print(f"The current date and time is {format} ")