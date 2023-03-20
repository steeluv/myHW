"""
Представьте, что сумма за пользование услугами такси складывается из
базового тарифа в размере $4,00 плюс $0,25 за каждые 140 м поездки.
Напишите функцию, принимающую в качестве единственного параметра
расстояние поездки в километрах и возвращающую итоговую сумму опла-
ты такси.
"""

def taxi(distance):
    price = 4
    add = 0.25
    if distance < 0.14:
        return('Стоимость поездки: ' + str(price) + '$')
    else:
        return('Стоимость поездки: ' + str(price + add * (distance * 1000 // 140)) + '$')
distance = float(input("Введите расстояние: "))
print(taxi(distance))

