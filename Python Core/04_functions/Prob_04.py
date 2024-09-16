import math
def circle_stats(radius):
    area = (radius ** 2) * math.pi
    circumference = 2 * math.pi * radius
    return area, circumference

num = int(input("Enter radius of Circle : "))

a, c = circle_stats(num)

print(f"For current radius Area is {round(a, 2)} and circumference is {round(c, 2)}")
