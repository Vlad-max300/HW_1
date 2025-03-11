from address import Address
from mailing import Mailing


from_addr = Address("123456", "Москва", "Ленина", "10", "5")
to_addr = Address("654321", "Санкт-Петербург", "Невский", "25", "12")


mail = Mailing(to_addr, from_addr, 500, "AB123456789RU")


print(mail.get_info())