import math

radius = float(input("Enter radius of circle: "))

area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

print(f"area of circle with {radius} is {area}, and the circumference is {circumference}")

x = int(input("Enter a number: "))
power2 = math.pow(x, 2)
power3 = math.pow(x, 3)
print(f"The power of 2 {x} is {power2}, and the power of 3 {x} is {power3}")
