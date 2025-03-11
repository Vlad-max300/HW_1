from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 13", "+79123456789"),
    Smartphone("Samsung", "Galaxy A54", "+79234567890"),
    Smartphone("Xiaomi", "Redmi Note 11", "+79345678901"),
    Smartphone("Google", "Pixel 7", "+79456789012"),
    Smartphone("OnePlus", "9 Pro", "+79567890123")
]


for phone in catalog:
    print(phone.get_info())