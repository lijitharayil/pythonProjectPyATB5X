#write a program to calculate area of triangle, Area =pi*r^2

# //step 1//
# figure out input and output
# pi = 3.14987563
# power = radius **2 or pow (radius,2)
import math

pi = 3.14987563
radius = float(input("Enter the radis of a circle"))
# Area = pi*(radius **2)
Area = pi*pow(radius,2)

# power --->** or pow we can use

# print(f"Area of the circle is,{Area}" )
# print(f"Area of the circle is,{Area:2f}" )
print(pi * float(input("Enter the radis of a circle"))**2)
print(math,pi)
