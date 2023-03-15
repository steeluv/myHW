a = int(input("Введите цену покупки "))
c = 0
while a != 0:
    c += a
    a = int(input("Введите цену покупки "))
if c % 2 == 0:
    while c % 2 != 1:
        c = c / 2
    print("К оплате ", c)
else:
    print("К оплате ", round(c * 0.85, 2))