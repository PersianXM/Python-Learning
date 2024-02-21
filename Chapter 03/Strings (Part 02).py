x = "Ali"
print(x[-1])
print(x[0])
print(x[1])
print(x[-2])

# Slicing
x = "Ali Rashedi"

print(x[1:-1])  # ta yek index ghabl az an
print(x[2:5])
print(x[2:6])
print(x[2:-3])

print(x[:-4])  # az ebteda ta -3
print(x[:5])  # az ebteda ta ghabl az 5

print(x[1:])  # az 1 ta enteha
print(x[0:])  # az 0 ta enteha

print(x[:])  # kole an print mishavad

print(x[0:4] + x[4:])
print(x[0:2] + x[2:])
print(x[0:5] + x[5:])

print(x[0:8:2])
print(x[0:10:3])

print(x[:452])

x = "Ali Rashedi"
print(x[len(x)-2])




