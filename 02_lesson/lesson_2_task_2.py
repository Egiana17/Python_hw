def is_year_leap(year):
    return "True" if year % 4 == 0 else False


year = int(input('введите год для проверки: '))

print(f"Год{year}-{is_year_leap(year)}")
