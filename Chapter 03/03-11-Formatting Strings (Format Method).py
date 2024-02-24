x = 5
y = 2.6879554

print("x is {} \n y is {} \n z is {}".format(5, y, 5+7))

print("x is {0} \n y is {1} \n z is {2}".format(5, y, 5))
print("x is {1} \n y is {1} \n z is {2}".format(5, y, 5))
print("x is {2} \n y is {1} \n z is {0}".format(5, y, 5))

dic = {"x": 5, "y": 8, "z": 2.336}
print("x is {x} \n y is {y} \n z is {z}".format(**dic))
print("x is {z} \n y is {y} \n z is {z}".format(**dic))
print("x is {z} \n y is {z} \n z is {z}".format(**dic))

print("x is {1} \n y is {2} \n z is {0}".format(*"Ali"))
print("x is {1} \n y is {2} \n z is {0}".format(*[1, 5, 7]))

print("x is {0}".format(5))
print("x is {0!s}".format("Ali"))
print("x is {0!r}".format("Ali"))
print("x is {0!a}".format("123456"))

print("x is {0:.2}".format(5.123456789))
print("x is {0:c}".format(110))
print("x is {0:d}".format(110))
print("x is {0:f}".format(5.123456789))

print("x is {0:%}".format(1.5))
print("x is {0:%}".format(1/2))
print("x is {0:%}".format(1/3))

print("x is {0:.2f}".format(4.36589))

print("x is {0:,.2f}".format(4000036589))
print("x is {0:.2f}".format(4000036589))

print("x is {0:15.2f}".format(44568))
print("x is {0:015.2f}".format(44568))

print("x is {0:b}".format(44568))
print("x is {0:#b}".format(44568))
print("x is {0:#0}".format(44568))
print("x is {0:#x}".format(44568))

print("x is {0:}".format(44))
print("x is {0:+}".format(44))
print("x is {0: }".format(44))

print("x is {0:<15}".format(45))
print("x is {0:<15}".format(45), "*", sep="")
print("x is {0:>15}".format(45), "*", sep="")
print("x is {0:^15}".format(45), "*", sep="")
print("x is {0:+^15}".format(45), "*", sep="")
print("x is {0:+^15}".format(45))

print("x is {0:{align}10}".format(45, align="<"))
print("x is {0:{align}10}".format(45, align=">"))
print("x is {0:{align}10}".format(45, align="^"))

print("x is {0:{align}15}".format(45, align="<"))
print("x is {0:{align}15}".format(45, align="^"))

print("x is {0:{align}{sign}15}".format(45, align="^", sign="+"))
print("x is {0:{align}{sign}{width}5}".format(45, align="^", sign="+", width="2"))

x = input("Sign: ")
print("x is {0:{align}{sign}{width}}".format(45, align="^", sign=x, width="10"))

x = input("align: ")
print("x is {0:{align}{sign}{width}}".format(45, align=x, sign="+", width="10"))
