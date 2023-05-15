"""
Создайте класс SpaceObject у которого будут свойство размер.
Создайте 2 класса Star и Planet которые будут наследовать SpaceObject. В классе Star добавьте свойство яркость
и метод светить в котором будет выводится на экран с какой яркостью светит звезда.
Классу Planet добавьте свойства население и прирост за год и метод который будет печатать население через переданное
ему количество лет.
"""
class SpaceObject:
    def __int__(self, size):
        self.size = size
class Star(SpaceObject):
    def __int__(self, size, light):
        super().__int__(light)
        self.light = light
    def show_light(self):
        print(self.light)
class Planet (SpaceObject):
    def __int__(self, size, population,growth):
         super().__int__(size)
         self.population = population
         self.growth = growth
    def calculate (self, years):
        print(self.population + self.growth * years)
Mars = Planet(2000, 100, 25)
Mars.calculate(20)





