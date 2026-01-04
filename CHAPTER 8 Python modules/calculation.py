# Ask the user to enter a float number called radius. Then calculate the circumference and the area of a circle using that radius, and round the result to 3 decimals. After that, store the result of the circumference in cir_result and the area in area_result. Remember to get the pi value from math module.

# Example run:

# Enter a float number for the radius:
# 5
# The circumference is: 31.416
# The area is: 78.54

from math import pi
radius = float(input("Enter a float number for the radius: "))
cir_result = 2*pi*radius
cir_result = round(cir_result, 3)
area_result = pi*radius**2
area_result = round(area_result, 3)
print(f"The circumference is: {cir_result}\nThe area is: {area_result}")