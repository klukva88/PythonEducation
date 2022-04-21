class Animal:
    def __init__(self, type_animal, sound):
        self.__type_animal = type_animal
        self.__sound = sound

    def makeNoise(self):
        print(f'{self.__type_animal} говорит {self.__sound}')

    def set_type_animal(self, new_animal_type):
        self.__type_animal = new_animal_type

    def set_sound(self, new_sound):
            self.__sound = new_sound.capitalize()

    def get_type_animal(self):
        return self.__type_animal

    def get_sound(self):
        return self.__sound

dog = Animal('Dog', 'Гав-Гав!') #Создаю экземпляр класса Animal() и передаю параметры

duck = Animal('Уточка', 'Кря-Кря!')
duck.makeNoise()
cow = Animal('Корова', 'Му-му!')
cow.makeNoise()
cat = Animal('Кошка', 'Mян-Мяу!')
cat.set_sound('пиу-пиу!')
cat.set_type_animal('Плошка')
cat.makeNoise()
dog.set_sound('гуф-гуф')
dog.makeNoise()
#dog.type_animal = 'Dog'
#dog.sound = 'Гав-Гав!'


'''Задача 2
Создайте класс Person со следующими приватными 
атрибутами:
• name, age, address, can_vote (Можно будет установить 
«да», «нет. По умолчанию для can_vote установлен 
параметр «Да», а для возраста установлен 18)
• В конструктор нужно передавать все атрибуты, кроме 
can_vote. Атрибут can_vote устанавливается в 
зависимости от возраста человека. 
• Создать геттер и геттер для age, name, address
• В сеттере происходит настройка возраста, затем в 
зависимости от возраста can_vote становится “Да”, если 
возраст человека выше либо равно 18-ти, иначе атрибут 
can_vote принимает в себя «Нет». 
• Создайте метод для отображение всех информаций о 
человеке.
Создайте необходимые экземпляры класса и передайте в 
конструктор все соответствующие параметры'''

class Person:
    def __init__(self, name, address, age=18):
        self.__name = name
        self.__age = age
        self.__address = address
        self.can_vote = 'Да'

    def set_name(self, name):
        self.__name = name
    def get_name(self):
        return self.__name

    def set_age(self, age):
        if age < 18:
            self.can_vote = 'Нет'
        else:
            pass
        self.__age = age

    def get_age(self):
        return self.__age

    def set_address(self, address):
        self.__address = address
    def get_address(self):
        return self.__address


man = Person('Коля', 'Омск')
man.set_age(20)
print(man.can_vote)
print(man.get_address())
