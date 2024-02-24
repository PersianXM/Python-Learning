# AND   set each bit to 1 if both bits are 1
# OR    Sets each bit to 1 if one of two bits is 1
# XOR   Set each bit to 1 if only one of two bits is 1
# NOT   inverts all the bits
# Zero fill left shift.  shift left by pushing zeros in from the right and left the leftmost bits
# Signed right shift

x = 0b00001011
print(x)

x = 5
print(bin(x))

x = 7
y = 5
print(x & y)
print(x | y)
print(x ^ y)

x = 5
print(5 >> 1)  # x // 2 ** 1
print(5 >> 2)  # x // 2 ** 2

x = 12
print(12 << 1)  # x * 2 ** 1
print(12 << 2)  # x * 2 ** 2

x = 3
print(~x)   # -x-1
y = 5
print(~y)

#  9 -> 00001001
# -9 -> 10001001
# -9 -> 11110110
# -9 -> 11110111

x = 3
x &= 2  # x = x & 2
print(x)

