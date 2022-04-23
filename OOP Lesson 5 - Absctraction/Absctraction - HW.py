'''Создайте абстрактный класс Bank с абстрактным методом getBalance. 100, 150 и
200 долларов ложатся в банках A, B и C соответственно. «BankA», «BankB» и
«BankC» являются подклассами класса «Bank», каждый из которых имеет метод
с именем «getBalance». Вызовите этот метод, создав объект каждого из трех
классов.'''

from abc import ABC, abstractmethod
class Bank(ABC):
    @abstractmethod
    def getBalace(self):
        pass

class BankA(Bank):
    def getBalace(self, balance):
        print(f'Баланс в Банке А состовляет ${balance}')

class BankB(Bank):
    def getBalace(self, balance):
        print(f'Баланс в Банке B состовляет ${balance}')
class BankC(Bank):
    def getBalace(self, balance):
        print(f'Баланс в Банке C состовляет ${balance}')

user1 = BankA()
user2 = BankB()
user3 = BankC()
user1.getBalace(100)
user2.getBalace(150)
user3.getBalace(200)

'''Задача 2
Есть некий Абстрактный класс Car у которого есть приватные поля:
• model;
• color;
• maxSpeed;
и также есть абстрактный методы brake(), gas(), которых требуется 
переопределить в классах наследниках.
Реализуйте и переопределите вышеописанные методы в классах наследниках 
Sedan, SportCar, FamilyCar.'''

class Car(ABC):
    def __init__(self, model, color, maxSpeed):
        self.__model = model
        self.__color = color
        self.__maxSpeed = maxSpeed

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        self.__model = model

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color

    @property
    def maxSpeed(self):
        return self.__maxSpeed

    @maxSpeed.setter
    def maxSpeed(self, maxSpeed):
        self.__maxSpeed = maxSpeed

    @abstractmethod
    def brake(self):
        pass
    @abstractmethod
    def gas(self):
        pass

class Sedan(Car):

    def brake(self):
        print(f'{self.color} седан {self.model} тормозит с {self.maxSpeed} км/ч до 0 за 5 секунд')
    def gas(self):
        print(f'{self.color} седан {self.model} разгоняется с 0 до {self.maxSpeed} км/ч за 20 секунд\n')


class SportCar(Car):

    def brake(self):
        print(f'{self.color} спорткар {self.model} тормозит с {self.maxSpeed} км/ч до 0 за 3 секунды')

    def gas(self):
        print(f'{self.color} спорткар {self.model} разгоняется с 0 до {self.maxSpeed} км/ч за 10 секунд\n')

class FamilyCar(Car):

    def brake(self):
        print(f'{self.color} семейный авто {self.model} тормозит с {self.maxSpeed} км/ч до 0 за 15 секунд')

    def gas(self):
        print(f'{self.color} семейный авто {self.model} разгоняется с 0 до {self.maxSpeed} км/ч за 30 секунд\n')



car1 = Sedan('Toyota Camry', 'Белая', 220)
car1.brake()
car1.gas()

car2 = SportCar('Nissan GTX', 'Красный', 280)
car2.brake()
car2.gas()

car3 = FamilyCar('Volvo XC70', 'Черная', 200)
car3.brake()
car3.gas()
