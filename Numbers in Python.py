x = 10
print(bin(x))
print(oct(x))
print(hex(x))

x = 1
x = x + 0.3
print(x)
print(type(x))

x = 1
x = float(x)
print(x)
print(type(x))

x = 1.12345
x = int(x)
print(x)
print(type(x))

x = 1
x = complex(x)
print(x)
print(type(x))

x = "1"
x = int(x)
print(x)
print(type(x))

x = "123.564"
x = str(x)
print(x)
print(type(x))

f = "0.1 + 0.2"
print(f)

f = 0.1 + 0.2
print(f)

f = 2
print(f)

from decimal import Decimal

print(Decimal('0.1') + Decimal('0.2'))

x = (Decimal('0.1') + Decimal('0.2'))

print(x)
print(type(x))

x = float(Decimal('0.1') + Decimal('0.2'))
print(x == 0.3)
print(type(x))

import fractions
print(fractions.Fraction(1.5))
print(fractions.Fraction(0.75))

x = 10_000_000_000
print(x)

f = 1_000_000_000_000.0
print(f)
print(type(f))

f = 1e3 # 1 * 10 ** 3
print(f)
print(type(f))

f = 1e-3 # 1 * 10 ** -3
print(f)
print(type(f))

f = 2e+300
print(f)

f = 2e+400  # inf error
print(f)
print(type(f))

c = 1 + 3j
d = 2 - 3j
print(c)
print(type(c))
print(c.real)
print(c.imag)
print(c.conjugate())
print(c * d)

