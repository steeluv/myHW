class Animal:
    def __int__(self, brain):
        self.brain = brain
    def thinking(self):
        print('Я могу думать спокойно', self.brain)
class human(Animal):
    def walk(self):
        print('хожу прямо')
