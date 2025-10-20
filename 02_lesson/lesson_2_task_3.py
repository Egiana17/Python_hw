def ceil_square(a, b):
    return ceil(a*b)
a = float(input('Введите первый множитель: '))
b = float(input('Введите второй множитель: '))
print(f'Округленная в большую сторону произведение - {ceil_square(a,b)}')
