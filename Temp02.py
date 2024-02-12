x = 53
y = 53

print(x is y)
print(x is not y)

x = [1, 5, 3, 0]
print(id(x))

y = [1, 5, 3, 0]
print(id(y))

print(x == y)   # True
print(x is y)   # False
print(x is not y)   # True

x = [1, 2]
y = [1, 2]
x = y
print(x is y)   # True

