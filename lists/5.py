number = input()
number = [int(a) for a in number.split()]

if len(number) == 1:
    print('Нет')
elif sorted(number) == number:
    print('Да')
else:
    print('Нет')