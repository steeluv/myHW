teachers = []

a = input('Добавить информацию о новом наставнике(да/нет)').lower()

while a !='нет':
    teacher = []
    if a =='да':
        teacher.append(input('Фамилия,Имя наставника:'))
        teacher.append(input('Должность: '))
        teacher.append(input('Количество студентов во всех группах:'))
        teachers.append(teacher)
    print(teachers)
    a = input('Записать нового наставника?(да/нет)').lower()