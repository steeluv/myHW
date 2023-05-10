class Animal:
    def __init__(self, voice , type):
        self.type = type
        self.voice = voice
    def make_voice(self):
        print(self.voice)
    def fight(self, other):
        print(self.type, 'аттакует', other.type)
dog = Animal('гав-гав', 'доберман')
dog.make_voice()
print(dog.type)

cat = Animal('мяуу', 'чеширский кот')
cat.make_voice()
dog.fight(cat)

