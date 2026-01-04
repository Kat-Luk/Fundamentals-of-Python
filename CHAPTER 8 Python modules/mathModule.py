# Write a program that asks the user to enter an integer. Then calculate the square root value (store the result to sqr_result), sin value (store the result to sin_result), and cos value (store the result to cos_result) of that number. Use square root, sin, and cos function provided in math module. Round the result to 2 decimals.

# Example output:

# Enter an integer: 
# 7
# The square root of 7 is 2.65
# The sin of 7 is 0.66
# The cos of 7 is 0.75

from math import cos,sin,sqrt
number = int(input("Enter a integer: "))
sqr_result = round(sqrt(number),2)
sin_result = round(sin(number),2)
cos_result = round(cos(number),2)
print(f"The square root of {number} is {sqr_result}\nThe sin of {number} is {sin_result}\nThe cos of {number} is {cos_result}")

