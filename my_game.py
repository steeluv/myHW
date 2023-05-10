class Hero:
    def __init__(self,name,health,armor,power,weapon):
        self.name = name
        self.health = health
        self.armor = armor
        self.power = power
        self.weapon = weapon

    def print_into(self):
        print('Поприветствуйте героя ->', self.name)
        print('Уровень здоровья', self.health)
        print('Уровень брони', self.armor)
        print('Уровень сила', self.power)
        print('Вооружен ->', self.weapon)
    def strike(self, enemy):
        print(f"{self.name} ударяет {enemy.name} с помощью {self.weapon} а наносит удар в размере {self.power}")
        if enemy.armor <= 0:
            enemy.health += (self.power - self.power)
            enemy.armor = 0
        else:
            enemy -= self.power
        print('У врага осталось', enemy.health, 'здоровья')
    def fight(self, enemy):
        while self.health > 0 and enemy.health > 0:
            self.strike(enemy)
            enemy.strike(self)
        if self.health <0 and enemy.health <0:
            print('Ничья')
        elif self.health <0:
            print(self.name, 'проиграл')
        elif enemy.health < 0:
            print(self.name, 'выиграл')

name1 = input('Введите имя героя:')
first_hero = Hero(name1,500,50,100,'Меч')
first_hero.print_into()
name2 = input('Введите имя героя:')
second_hero = Hero(name2,323,90,290,'Катана')
second_hero.print_into()