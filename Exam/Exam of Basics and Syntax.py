# Question 01
x = 5
y = 4

x, y = y, x

print(x, y)

# Question 02

x = int(input("Enter width: "))
y = int(input("Enter height: "))

print("The area is: ", (x * y))

# Question 03

celsius = int(input('Enter the Temperature in Celsius: '))
fahrenheit = (celsius * (9 / 5) + 32)
print("The temperature is:", fahrenheit, end=" Fahrenheit")

# Question 04

r = int(input("Please enter a number: "))

pi = 3.14

# Circumference calculation
C = 2 * pi * r

# Area calculation
A = pi * r**2  # Assuming you meant to square the radius

print("The circumference of the circle is:", C)
print("The area of the circle is:", A)

# Question 05

number1 = int(input("Please, enter the first number: "))
number2 = int(input("Please, enter the second number: "))

numbers_sum = number1 + number2
numbers_subtraction = number1 - number2
numbers_multiplication = number1 * number2
square1 = number1**2
square2 = number2**2

print(f"The sum of {number1} and {number2} is: {numbers_sum}")
print(f"The difference of {number1} and {number2} is: {numbers_subtraction}")
print(f"The multiplication of {number1} and {number2} is: {numbers_multiplication}")
print(f"The square of {number1} is: {square1}")
print(f"The square of {number2} is: {square2}")

# Question 06
# Calculates the average of three numbers.

number1 = int(input("Please, enter the first number:"))
number2 = int(input("Please, enter the second number:"))
number3 = int(input("Please, enter the third number:"))

Average = ((number1 + number2 + number3) / 3)

print(f"The average of {number1}, {number2} and {number3} is {Average}")

# Question 07
base = int(input("Please, enter the base number:"))
height = int(input("Please, enter the height:"))

area = 0.5 * base * height

print(f"The area of triangle is {area}")

# Question 08
age = int(input("Please enter you age:"))
year_of_100th_birthday = 2024 + (100 - age)
print(f"Your age is {age} and in {year_of_100th_birthday}, you will become 100 years old.")

# Question 09
num1 = 42
num2 = 13
result = num1 + num2
print(result)
