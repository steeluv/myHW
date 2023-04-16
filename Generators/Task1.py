"""Напишите генератор выводящий все символы строки на печать, но только в том случае,
если они являются буквами (остальные игнорируются)."""


def findwords_gen(string):
    for i in string:
        if i.isalpha():
            yield i

for s in findwords_gen(string = input()):
    print(s)