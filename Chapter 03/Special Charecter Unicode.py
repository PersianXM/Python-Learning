print("Hello \" World!")

print("Hello \' World!")

print("Hello \t World!")

print("Hello \\ World!")

# ASCII
# UNICODE

print(ord("A"))
print(ord('a'))
print(ord('+'))

print(chr(98))
print(chr(97))
print(chr(65))

print("Char: \u0489")   # 16bit
print("Char: \u0450")   # 16bit

print("Char: \U00002DBB")   # 32bit
print("Char: \U00002DCB")   # 32bit

print("Char: \x2a")     # 16bit

print("Hello \u000A World!")    # Next Line unicode
print("Hello \x0a World!")      # Next Line hex
print("Hello \n World!")

print("Hello\b World!")  # Backspace
print("Hello Worl\rd!")    # start from next line

print(r"Hello \t \r \m \x0 World!")  # start from next line
