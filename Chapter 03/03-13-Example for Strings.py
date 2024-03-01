# s = "Hello Word!, how are you? How are you? How are you?"
# print(f" total letters of, '{s}' is {len(s)}")
#
# # ----------------------------------
#
# s = "This is my sample Text!"
# c = input(f" the sample text is '{s}' What are you looking for?!")
# print(f" total letters of, '{c}' is {s.count(c)}")
#
# # ----------------------------------
#
# x = input("Enter a character: ")
# print(f"total letters are: {len(x)} ,and total letter of 'r' is {x.count('r')}")
#
# # ----------------------------------
#
# s = input("Enter a character for stripping: ")
# s = s.rstrip()
# print(f"striped text is: {s}")
#
# # ----------------------------------
#
# s = input("Find Space: ")
# s = s.rstrip()
# i = s.rfind(" ")     # find first space from right
# print(i)
#
# # -----------------------------------
#
# s = input("Find last character in Text: ")
# s = s.rstrip()
# i = s.rfind(" ")    # find first space from right
# print(s[i+1:])      # from next one to space
#
#
# # -----------------------------------
#
# s1 = input("Please, Enter fist character: ")
# s2 = input("Pleas, Enter second character: ")
#
# print(s2 in s1)
#
# # -----------------------------------
#
# s = input("Please, Enter a character: ")
# print(s.replace(" ", ",").replace("\t",""))

# -----------------------------------

s = input("Please, Enter phone number: ")
print(s.lstrip("0"))
