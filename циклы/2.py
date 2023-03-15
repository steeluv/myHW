if input() == "game":
    a = 1
    b = input()
    while b != "off":
        if int(b) == 5 and a <= 3:
            print("Вы выиграли билет на концерт!")
            a = 0
        if a >= 3:
            a = 0
            print("Вы проиграли:(")
        a += 1
        b = input()
    print("Игра окончена!")