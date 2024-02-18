x = input('Enter a 3 digit number: ')
print(x[0])
print(x[1])
print(x[2])

y = int(input('Enter a 3 digit number: '))
temp = y % 10
print(temp)
y = y // 10
temp = y % 10
print(temp)
y = y // 10
temp = y % 10
print(temp)
