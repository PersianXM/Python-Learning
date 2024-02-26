s = "Hello Word!, how are you? How are you? How are you?"
print(f" total letters of, '{s}' is {len(s)}")

# ----------------------------------

s = "This is my sample Text!"
c = input(f" the sample text is '{s}' What are you looking for?!")
print(f" total letters of, '{c}' in this Template is {s.count(c)}")

# ----------------------------------

x = input("Enter a character: ")
print(f"total letters are: {len(x)} ,and total letter of 'r' is {x.count('r')}")

# ----------------------------------

s = input("Enter a character: ")
s = s.rstrip()
i = s.rfind(" ")
print(i)

# ----------------------------------

s = input("Enter a character: ")
s = s.rstrip()
i = s.rfind(" ")
print(s[i:])

# ----------------------------------

s = input("Enter a character: ")
s = s.rstrip()
i = s.rfind(" ")
print(s[i+1:])
