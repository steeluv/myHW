"""
Напишите генератор выводящий все числа делящиеся на 11 в диапазоне от 0 до 100
"""

def gen():
    for i in range(11, 101, 11):
        yield i

for num in gen():
    print(num)