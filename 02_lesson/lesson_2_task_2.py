def is_year_leap(year):
Args:
year(int): Год для проверки
returns:
bool: True если год високосный,
False если нет
if year %4 == 0:
return True
else: 
return False
