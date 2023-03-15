"""
Напишите программу считающую и обрабатывающую индекс массы тела.
В одной функции программа должна считать ИМТ. В другой обрабатывать, если ИМТ ниже 18.5 печатать "Недостаточный вес",
от 18.5 до 25 "ИМТ в норме", больше 25 "Избыточный вес".
Формула определения ИМТ: index = weight / (height * height)
"""
def IMB(weight, height):
    return weight / (height * height)
def IMBnorm(n):
    if 18.5 <= n <= 25:
        return('ИМТ в норме')
    elif n < 18.5:
        return('Недостаточный вес')
    else:
        return('Избыточный вес')
weight, height = map(float,input().split())
print(IMBnorm(IMB(weight, height)))

