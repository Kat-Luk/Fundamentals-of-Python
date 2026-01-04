try:
    f_number = int(input("Enter the first number:"))
    s_number = int(input("Enter the second number:"))
    result = round(f_number/s_number,2)
    print(f"The result is {result}")
except ValueError:
    print("Error: both inputs should be numbers.")
except ZeroDivisionError:
    print(f"Error: {f_number} cannot be divided by 0.")
