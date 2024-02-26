import datetime

x = 5
y = 4.3695
print(f"The value of x is {x} \n The value of y is {y} \n The value of z is {5**2}")

x = "Ali"
y = 4.3695
print(f"The value of x is {x!r} \n The value of y is {y:.2f} \n The value of z is {5**2}")

x = 3.2564
print(f"The value of x is {{x}}")


print(f"The value of x is {{{x}}}")

x = 3.2564
print(f"The value of x is {{{{x}}}}")

x = "ali rashedi"
print(f"convert all a to dash, {x.replace('a', '-')}")

name = "Ali"
age = 22

msg = (

    f"name: {name}\n"
    f"age: {age}\n"

)
print(msg)


print(datetime.datetime.now())
print(datetime.datetime.today())

today = datetime.datetime.today()
print(today)

print(f"{today:%y}")
print(f"{today:%Y}")
print(f"{today:%H}")
print(f"{today:%p}")
print(f"{today:%M}")
print(f"{today:%S}")

print(f"{today:%y / %M / %S}")

print(f"{today: %Y-%m-%d %H:%M:%S}")
print(f"{today: %Y / %m*****%B}")

x = 5
print(f"{x: <15}*")
