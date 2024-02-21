s = "Hello World!"

print(len(s))
print(s[4:len(s)])

s = s.upper()  # upper method
print(s)

s = s.lower()
print(s)

s = s.count("l")
print(s)

x = "Hello World!"
x = x.count('ll')
print(x)

x = "Hello World!"
print(x.endswith("a"))
print(x.startswith("Hell"))

x = "Hello World!"
print(x.find("H"))
print(x.find("o"))  # will find from the first
print(x.rfind("o"))  # will find from the end

x = "Hello World!"
print(x.isalnum())
print(x.isalpha())
print(x.isdigit())
print(x.isspace())

x = "123456789"
print(x.isnumeric())

s = "-"
l = ["A", "B", "C"]
print(s.join(l))

x = "Ali Rashedi"
print(x.split(" , "))
print(x.split(" "))

print(x.replace("a","***"))

x = "     Ali Ra  shedi    "
print(x.strip())

x = "+++ Ali Rashedi +++"
print(x.lstrip("+"))
print(x.rstrip("+"))


