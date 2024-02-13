#   string.replace(oldvalue, newvalue)
#   df['column'].apply(function_name)

#   def function_name(arguments):
#       function body
#
#       return

# def greet():
#     print("Hello World!")
#
#
# print(greet())


def add_numbers(num1, num2):
    sum = num1 + num2
    return sum


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("sum of numbers: ", add_numbers(num1, num2))


def add_numbers(num1, num2):
    sum = num1 + num2
    print("sum: ", sum)


def subtract_numbers(num1, num2):
    result = num1 - num2
    print("result: ", result)
    return result
