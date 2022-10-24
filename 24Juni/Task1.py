area = 3.14 * 10 ** 2
print(area)
# Сумма заказа == 1000 (EURO)
# К оплате == 600 (EURO)
#
# Вывести:
# - размер скидки (в процентах)
# - размер скидки (в EURO)
price = 1000
cena = 600
skidka = price - cena
proz= skidka / (price / 100)
print("ваша скидка составила", skidka, "(", proz, "%)")

students = [
    {'name': 'Petr Petrov', 'age': 27, 'country': 'Germany'},
    {'name': 'Ivan Ivanov', 'age': 25, 'country': 'Germany'},
]
print(students[1]['country'])

# НЕОБХ. ОПИСАТЬ СТРУКТУРУ ОБЪЕКТА "АВТОМОБИЛЬ" В ВИДЕ СЛОВАРЯ
# укажите 5 полей
# важно использовать английский язык в именовании полей

auto = [
    {'speed': '200',
     'brand': 'Toyota',
     'model':  'c4',
     'farbe': 'schwarz',
     'price': 200000
    }
]

