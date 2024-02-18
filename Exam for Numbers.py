import math
import statistics
from math import pow

radius = float(input("Enter radius of circle: "))

area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

print(f"area of circle with {radius} is {area}, and the circumference is {circumference}")

# --------------------------------------------

x = int(input("Enter a number: "))

power2 = math.pow(x, 2)
power3 = math.pow(x, 3)

print(f"The power of {x} is {power2}, and the power3, is {power3}")

# --------------------------------------------

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

power = math.pow(x, y)

print(f"power of {x} bace on {y} is {power}")

# --------------------------------------------

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

mean = statistics.mean((x, y, z))
print(f"The mean of {x}, {y} and {z} is {mean}")
