"""
Создайте функцию которая принимает на вход 3 именованных параметра, выведите на печать значения этих параметров,
но только в том случае если они не равны None.
"""
def my_data(name, surname, age):
    print(f"Name: {name} Surname: {surname} Age:{age}")
my_data(name = "Violetta", surname = "Enikeeva", age = 16)