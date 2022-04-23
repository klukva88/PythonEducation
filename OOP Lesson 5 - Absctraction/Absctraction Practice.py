from abc import ABC, abstractmethod
class Person(ABC):
    def __init__(self, whereEats, whereEarns, whereSpends):
        self.whereEats = whereEats
        self.whereEarns = whereEarns
        self.whereSpends = whereSpends
    @abstractmethod
    def calculateMyExpanses(self):
        pass

    @abstractmethod
    def whereToEat(self):
        pass

    @abstractmethod
    def earnMoney(self):
        pass

class Student(Person):

    def calculateMyExpanses(self):
        print(f'Студент тратит деньги в {self.whereSpends}')
    def whereToEat(self):
        print(f'Студент питается в {self.whereEats}')
    def earnMoney(self):
        print(f'Студент зарабатывает там же, где и питается в {self.whereEats}')

class Doctor(Person):

    def calculateMyExpanses(self):
        print(f'Доктор тратит деньги {self.whereSpends}')
    def whereToEat(self):
        print(f'Доктор питается в {self.whereEats}')
    def earnMoney(self):
        print(f'Доктор зарабатывает в {self.whereEarns}')

class BankEmployee(Person):

    def calculateMyExpanses(self):
        print(f'Банковский работник тратит деньги {self.whereSpends}')
    def whereToEat(self):
        print(f'Банковский работник питается в {self.whereEats}')
    def earnMoney(self):
        print(f'Банковский работник зарабатывает {self.whereEarns}')



student = Student('Кафе', 'Кафе', 'Зоопарк')
doc = Doctor('Столовка', 'Больница', 'Кино')
bankEmployee = BankEmployee('Ресторане', 'В Банке', 'на семью')
student.calculateMyExpanses()
student.whereToEat()
student.earnMoney()
doc.calculateMyExpanses()
doc.whereToEat()
doc.earnMoney()
bankEmployee.calculateMyExpanses()
bankEmployee.whereToEat()
bankEmployee.earnMoney()