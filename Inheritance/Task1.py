"""
Добавьте на основании классов из презентации класс Magician который наследует Hero. Со своими методами hello и atack.
"""
class Magician:
    def __int__(self,hello,atack):
        self.hello = hello
        self.atack = atack
class Hero(Magician):
    def __int__(self,hello,atack):
        self.hello = hello
        self.atack = atack
Arnou = Magician("Приветик", "бью в челюсть")
Arnou.Hero()
print(Arnou)

