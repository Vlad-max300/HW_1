import math


def square(side):
    return math.ceil(side * side)

side = 10
result = square(side)


print(f"Площадь квадрата со сторой {side}: {result}")