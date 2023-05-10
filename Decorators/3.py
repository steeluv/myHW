# -*- coding: utf-8 -*-
def decorate(func):
    def wrapper(val1,val2):
        print(f'Данная функция выводит все числа между {val1} и {val2}')
        func(val1,val2)
    return wrapper()
@decorate
def func(val1, val2):
    [print(i) for i in range(val1, val2) if i % 3 == 0]

func(1,7)