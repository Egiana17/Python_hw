from address import Address
from mailing import Mailing

address = Address("197350", "Санкт-Петербург", "пр.Королева", "60", "200")
adress_to = Address("150150", "Баку", "Амираджаны", "22", "34")

mail = Mailing(
    to_address=adress_to,
    from_address=address, 
    cost=1000,
    track="12345678"
)


print(f"отправление {mail.track} из {mail.from_address.index}, "
      f"{mail.from_address.city}," 
      f"{mail.from_address.street}, {mail.from_address.house} - "
      f"{mail.from_address.apartment} в {mail.to_address.index}"
      f"{mail.to_address.city}", 
      f"{mail.to_address.street}", {mail.to_address.house} - "
      f"{mail.to_address.apartment}" 
      f"{mail.cost рублей}")
