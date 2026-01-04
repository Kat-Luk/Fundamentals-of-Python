from datetime import datetime
try:
    input_date = input("Enter a date in format DD/MM/YYYY:\n")
    format = "%d/%m/%Y"
    checked = datetime.strptime(input_date,format)
    print("The date is valid.")
except ValueError:
    print("Error: The date is invalid.")
