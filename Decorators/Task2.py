"""
Напишите программу добавляющую в рецепт бутерброда ингридиенты "Салат" и "Ананасы" с помощью декораторов.
"""
# -*- coding: utf-8 -*-
def decorate(func):
    def vreper():
        print('салатик')
        func()
        print('ананансы')
        return vreper
@decorate
def burger():
    print('хлебушек' , 'колбаска', 'сырок')
burger()
