"""
Напишите функцию cacluate, которая может принимать любое количество чисел и возвращать кортеж.

Первое значение кортежа - это среднее значение всех параметров, а второе значение - все числа, превышающие среднее значение.
Второе значение оформите в виде списка.
"""
def cacluate (*args):
    sum(args)
    num = sum(args)/len(args)
    list =[]
    for i in args:
        if i > num:
            list.append(i)
    return (num, list)
print(cacluate(8,7,6,5,4,3,2))