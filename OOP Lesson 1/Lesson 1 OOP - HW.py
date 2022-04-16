class Animal:
    def __init__(self, type_animal, sound):
        self.type_animal = type_animal
        self.sound = sound
    def makeNoise(self):
        print(f'{self.type_animal} говорит {self.sound}')

dog = Animal('Dog', 'Гав-Гав!') #Создаю экземпляр класса Animal() и передаю параметры
#dog.type_animal = 'Dog'
#dog.sound = 'Гав-Гав!'
duck = Animal('Уточка', 'Кря-Кря!')
dog.makeNoise()
duck.makeNoise()
cow = Animal('Корова', 'Му-му!')
cow.makeNoise()