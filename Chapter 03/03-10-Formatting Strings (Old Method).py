x = 1.256
y = 8
print("x: ", x, "y: ", y)
print("x: ", x, "\ny: ", y)
print("x: ",round(x, 1), "\ny: ", y)

# %

x = 2
y = 3.6
print("x is: %i\ny is: %i"%(x, y))
print("x is: %i\ny is: %i\nz is: %i" % (x, y, 5+2))

# [(key)] [flag] [w] [.p] type

print("%i" % 2.2558)
print("%c" % "R")
print("%c" % 48)

print("Ali: %s" % "Rashedi")
print("Ali: %s %i" % ("Rashedi", 54))

print(("%i" % 54))
print(("%d" % 54.5546))
print(("%o" % 5024))    # 8

print(("%x" % 5024))    # 16
print(("%X" % 5024))    # 16

print(("%e" % 5024))
print(("%E" % 5024))

print(("%f" % 5024.12))
print(("%f" % 5024.123456789))

print(("%f" % 2e+400))
print(("%F" % 2e+400))

print("%r" % "ali")

y = 3.123456789
print("%f" % y)     # show 6 figure and will round the number
print("%.2f" % y)   # show 2 figure

print("%9.2f" % y)   # tole meydan

y = 3.673214569
print("%+9.2f" % y)
y = -3.673214569
print("%9.2f" % y)

y = 3.673214569
print("%08.2f" % y, "*", sep=" ")

d = {"a": 2, "b": 7}
print("%(a)f \n %(b)i" % d)
print("%(a)i \n %(b)i" % d)

y = 3.65477889971
print("%8.3f" % y)
print("%8.*f" % (2, y))


y = 3.65477889971
p = int(input("Enter p and its type: "))
print("%8.*f" % (p, y))

y = 3.65477889971
p = int(input("Enter p and its type: "))
z = int(input("Enter z and its type: "))
print("%*.*f" % (z, p, y))

