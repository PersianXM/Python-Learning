x = int(input('Enter weight in kilogram: '))
y = x * 1000
print(f"every {x} kilogram, is equal to {y} gram")

# --------------------------------------------------

x = int(input('Enter the length of triangle: '))
y = int(input('Enter the base of the triangle: '))
area = x * y * 0.5
print(f"\x1b[6;30;42m The area of the triangle is: \x1b[0m {area}")

from colorist import Color
print(f"Only {Color.CYAN}this part{Color.OFF} is in colour")

from colorist import ColorRGB, BgColorRGB
dusty_pink = ColorRGB(194, 145, 164)
bg_steel_blue = BgColorRGB(70, 130, 180)
print(f"I want to use {dusty_pink}dusty pink{dusty_pink.OFF} and {bg_steel_blue}steel blue{bg_steel_blue.OFF} colors inside this paragraph")
