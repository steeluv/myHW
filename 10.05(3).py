class Rectangle:
    def __int__(self, lenght, widht):
        self.lenght = lenght
        self.widht = widht
    def print_info(self):
        print('Дан прямоугольник с длиной ', self.lenght, 'и шириной', self.widht)
    def ret_p(self):
        return (self.widht + self.lenght) * 2
    def ret_s(self):
        return self.widht * self.lenght

rest1 = Rectangle(5,10)
rest2 = Rectangle(6,8)
rest1.print_info()
rest2.print_info()
print(rest1.ret_s())

