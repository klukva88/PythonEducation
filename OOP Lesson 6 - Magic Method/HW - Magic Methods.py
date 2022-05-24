'''Задача 1
1. Создайте класс Person примите в качестве аргумента name, age,
salary.
Создать объекты person1, person2 задать к ним необходимые
значения.
• Вам необходимо измерить длину имени человека каждого из
объектов с помощью магического метода __len__
• Отобразить сумму заработной платы между двумя объектами с
помощью магического метода __add__
• Отобразить разность заработной платы между двумя
объектами с помощью магического метода __sub__
• При обращении к объекту необходимо вывести имя человека с
помощью магического метода __str__'''
class Person:
    def __init__(self, name, age, salary):
        self.__name = name
        self.__age = age
        self.__salary = salary

    def __len__(self):
        return len(self.__name)
    def __add__(self, other):
        if isinstance(other, Person):
            return other.__salary + self.__salary
        elif isinstance(other, (int, float)):
            return other + self.__salary

    def __radd__(self, other):
        if isinstance(other, Person):
            return other.__salary + self.__salary
        elif isinstance(other, (int, float)):
            return other + self.__salary

    def __sub__(self, other):
        if isinstance(other, Person):
            return other.__salary - self.__salary
        elif isinstance(other, (int, float)):
            return self.__salary - other
    def __rsub__(self, other):
        if isinstance(other, Person):
            return other.__salary - self.__salary
        elif isinstance(other, (int, float)):
            return self.__salary - other

    def __mul__(self, other):
        if isinstance(other, Person):
            return other.__salary * self.__salary
        elif isinstance(other, (int, float)):
            return other * self.__salary

    def __rmul__(self, other):
        if isinstance(other, Person):
            return other.__salary * self.__salary
        elif isinstance(other, (int, float)):
            return other * self.__salary

    def __truediv__(self, other):
        if isinstance(other, Person):
            return other.__salary / self.__salary
        elif isinstance(other, (int, float)):
            return other / self.__salary
    def __rtruediv__(self, other):
        if isinstance(other, Person):
            return other.__salary / self.__salary
        elif isinstance(other, (int, float)):
            return other / self.__salary

    def __str__(self):
        return self.__name


person1 = Person('Nick', 33, 10000)
person2 = Person('Ann', 30, 15000)
print(f' Name length of {person1} is {len(person1)} letters')
print(f' Name length of {person2} is {len(person2)} letters')

print(f'Salary total of {person1} and {person2} equals {person1 + person2}')
print(f'Salary difference between {person1} и {person2} equals {abs(person1 - 100)}')
print(f'Salary difference between {person1} и {person2} equals {abs(1000 - person2)}')
print(f' Person 2 name is {person2}')

'''Задача 2
Необходимо создать класс Area (площадь), принять от конструктора 
два аргумента height, width. Ваша задача создать магические методы 
для магических сравнений __lt__, __gt__, __eq__, __le__, __ge__
Сравнить:
• Между двумя созданными объектами
• Между объектом и каким либо числом
Важно! Формула площади это height * width. Учтите этот момент 
при создании магических методов'''

class Area:
    def __init__(self, dimension):
        self.__dimension = dimension

    def figureArea(self):
        return self.__dimension[0] * self.__dimension[1]

    def __lt__(self, other):
        if isinstance(other, Area):
            if self.figureArea() < other.figureArea():
                return f'Figure 1 is less then Figure 2'
            elif isinstance(self, (int, float)) and other.figureArea() < self:
                return f'Figure 2 is less then {self}'
            else:
                return f'Figure 1 is greater then Figure 2'
        elif isinstance(other, (int, float)):
            if self.figureArea() < other:
                return f'Figure 1 is less then {other}'
            else:
                return f'Figure 1 is greater then {other}'

    def __delitem__(self, key):
        del self.__dimension[key]
    def __getitem__(self, item):
        return self.__dimension[item]
    def __contains__(self, item):
        if item in self.__dimension:
            return True




    # def __lt__(self, other):
    #     # Делаю проверку через try except на случай если в магический метод передадут число вместо 2й фигуры
    #     # Сделал именно через try потому что показалось что так будет менее громоздко
    #     try:
    #         if self.figureArea() < other.figureArea():
    #             print(f'Figure 1 is less then Figure 2')
    #         else:
    #             print(f'Figure 1 is greater then Figure 2')
    #     except AttributeError:
    #         if self.figureArea() < other:
    #             print(f'Figure 1 is less then {other}')
    #         else:
    #             print(f'Figure 1 is greater then {other}')
    #     return '' #Если не сделать return то функция возвращает None
    #
    # def __gt__(self, other):
    #     try:
    #         if self.figureArea() > other.figureArea():
    #             print(f'Figure 1 is greater then Figure 2')
    #         else:
    #             print(f'Figure 1 is less then Figure 2')
    #     except AttributeError:
    #         if self.figureArea() > other:
    #             print(f'Figure 1 is greater then {other}')
    #         else:
    #             print(f'Figure 1 is less then {other}')
    #     return ''
    #
    # def __eq__(self, other):
    #     try:
    #         if self.figureArea() == other.figureArea():
    #             print(f'Figure 1 is equal to Figure 2')
    #         else:
    #             print(f'Figure 1 is NOT equal Figure 2')
    #     except AttributeError:
    #         if self.figureArea() == other:
    #             print(f'Figure 1 is equal to {other}')
    #         else:
    #             print(f'Figure 1 is NOT equal {other}')
    #     return ''
    #
    # def __ge__(self, other):
    #     try:
    #         if self.figureArea() >= other.figureArea():
    #             print(f'Figure 1 is greater or equal then Figure 2')
    #         else:
    #             print(f'Figure 1 is less then Figure 2')
    #     except AttributeError:
    #         if self.figureArea() >= other:
    #             print(f'Figure 1 is greater or equal then {other}')
    #         else:
    #             print(f'Figure 1 is less then {other}')
    #     return ''
    #
    # def __le__(self, other):
    #     try:
    #         if self.figureArea() <= other.figureArea():
    #             print(f'Figure 1 is less or equal then Figure 2')
    #         else:
    #             print(f'Figure 1 is greater then Figure 2')
    #     except AttributeError:
    #         if self.figureArea() <= other:
    #             print(f'Figure 1 is less or equal then Figure 2')
    #         else:
    #             print(f'Figure 1 is greater then {other}')
    #     return ''

figure1 = Area([10, 20])
figure2 = Area([10, 30])

print(figure1 < 20)
print(figure1 < figure2)
#print(20 < figure2)
print(figure2 < 20)
print(10 in figure1)
print(10 in figure2)
print(15 in figure2)
del figure2[0]
print(f'Width of Figure 1 is {figure1[1]}')
# print(figure1 > 20)
# print(figure1 > figure2)
# print(figure1 == 20)
# print(figure1 == figure2)
# print(figure1 <= 20)
# print(figure1 <= figure2)
# print(figure1 >= 20)
# print(figure1 >= figure2)


