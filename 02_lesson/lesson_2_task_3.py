import math


def ceil_square(a):
    return math.ceil(a*a)


a = int(input('Введите значение стороны квадрата: '))
print(f'площадь квадрата - {ceil_square(a)}')
