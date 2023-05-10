class Students:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        self.course = '-'
    def set_course(self, new_course):
        self.course = new_course
        print(self.name, 'установлен курс', self.course)
    def print_if(self):
        if self.marks < 50:
            print(self.name,'на грани отчисления')
        else:
            print(self.name, 'в порядке')

Kaplan = Students('Каплан' , 20)
print(Kaplan.course)
Kaplan.course = 1

Areg = Students('Арег', 100)
Areg.course = 2

Kaplan.print_if()
Areg.print_if()