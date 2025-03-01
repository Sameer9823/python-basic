import math


def circle(radius):
    # two precision
    a = round(math.pi * radius ** 2, 2)
    b = round(2 * math.pi * radius, 2)
    return a, b

a, c = circle(5)
print("Area: ", a)
print("Circumference: ", c)