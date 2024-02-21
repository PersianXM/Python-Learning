x = 1.2
print(isinstance(x, float))
print(isinstance(x, int))

x = "Ali"
print(type(x))

x = "12564"
print(type(x))

x = "#$%^&*"
print(type(x))

x = 'I\'m not a string'
print(x)

x = 'I\'m not \n a string'
print(x)

x = 'C:\Downloads\\new'
print(x)

x = 'C:\Down\tloads\\new\\telegram'
print(x)

x = r'C:\Downloads\new\telegram'
print(x)

x = """I'm
not
a
string"""
print(x)

x = """\
I'm
not
a
string"""
print(x)

x = "Ali"
y = "Rashedi"
print("Ali", "Rashedi")
print("Ali" + "Rashedi")
print("Ali" + " " + "Rashedi")
print("Ali " * 3 + " " + "Rashedi")
