'''Задача 1
Напишите программу с классом Student, в котором есть три атрибута: name, groupNumber и age. По умолчанию name = Ivan,
 age = 18, groupNumber = 10A. Необходимо создать пять методов: getName, getAge, getGroupNumber,
setNameAge, setGroupNumber. Метод getName нужен для получения данных об имени конкретного студента,
метод getAge нужен для получения данных о возрасте конкретного студента, vетод setGroupNumberнужен для получения данных о номере группы
конкретного студента. Метод SetNameAge позволяет изменить данные атрибутов установленных по умолчанию, метод setGroupNumber позволяет
изменить номер группы установленный по умолчанию. В программе необходимо создать пять экземпляров класса Student, установить
им разные имена, возраст и номер группы'''


class Student:
    def __init__(self, name='Ivan', age=18, groupNumber='10A'):
        self.__name = name
        self.__age = age
        self.__groupNumber = groupNumber

    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age

    def getGroupNumber(self):
        return self.__groupNumber

    def setNameAge(self, newName, newAge):
        self.__name = newName
        self.__age = newAge

    def setGroupNumber(self, newGroupNumber):
        self.__groupNumber = newGroupNumber


sudent1 = Student()
sudent2 = Student()
sudent3 = Student()
sudent4 = Student()
sudent5 = Student()

print(sudent1.getName())
print(sudent1.getAge())
print(sudent1.getGroupNumber())
sudent5.setNameAge('Masha', 16)
sudent5.setGroupNumber('11B')
print(sudent5.getName())
print(sudent5.getAge())
print(sudent5.getGroupNumber())

'''Задача 2
Напишите программу с классом Math. Создайте два атрибута — a и b. 
Напишите методы addition — сложение, multiplication — умножение, division —
деление, subtraction — вычитание. При передаче в методы параметров a и b с 
ними нужно производить соответствующие действия и печатать ответ.'''


class Math:
    def __init__(self, a=None, b=None):
        self.a = a
        self.b = b

    def addition(self, a, b):
        return print(f' Результат сложения {a} и {b} равен {a + b}')

    def multiplication(self, a, b):
        return print(f' Результат умножения {a} на {b} равен {a * b}')

    def division(self, a, b):
        try:
            return print(f' Результат деления {a} на {b} равен {int(a / b)}')
        except ZeroDivisionError:
            print('Делить на 0 нельзя!')
            self.division(a, int(input('Введите другой делитель, не равный 0: ')))

    def substraction(self, a, b):
        return print(f' Результат вычитания {b} из {a} равен {a - b}')


result = Math()
result.addition(10, 5)
result.division(10, 0)
result.multiplication(10, 5)
result.substraction(10, 5)

'''Задача 3
Напишите программу с классом Car. Создайте конструктор класса Car. Создайте 
атрибуты класса Car — color (цвет), type (тип), year (год). Напишите пять 
методов. 
Первый — запуск автомобиля, при его вызове выводится сообщение 
«Автомобиль заведен». Второй — отключение автомобиля — выводит 
сообщение «Автомобиль заглушен». Третий — присвоение автомобилю года 
выпуска. Четвертый метод — присвоение автомобилю типа. Пятый —
присвоение автомобилю цвета'''


class Car:
    def __init__(self, colour=None, type=None, year=None):
        self.__colour = colour
        self.__type = type
        self.__year = year

    def engineStart(self):
        return print('Автомобиль заведен')

    def engineStop(self):
        return print('Автомобиль заглушен')

    def setColour(self, carColour):
        self.__colour = carColour
        return print(f'Автомобилю присвоен {self.__colour} цвет')

    def setType(self, carType):
        self.__type = carType
        return print(f'Автомобилю присвоен тип {self.__type}')

    def setYear(self, carYear):
        self.__year = carYear
        return print(f'Автомобилю присвоен {self.__year} год')


car1 = Car()
car1.setColour('Red')
car1.setType('Minivan')
car1.setYear(2010)
car1.engineStart()
car1.engineStop()

'''Задача 4
Создайте класс Soda (для определения типа газированной воды), принимающий 
1 аргумент при инициализации (отвечающий за добавку к выбираемому 
лимонаду). В этом классе реализуйте метод show_my_drink(), выводящий на 
печать «Газировка и {ДОБАВКА}» в случае наличия добавки, а иначе 
отобразится следующая фраза: «Обычная газировка».
Пример запуска:
# Тесты
drink1 = Soda()
drink2 = Soda('малина')
drink3 = Soda(5)
drink1.show_my_drink()
drink2.show_my_drink()
drink3.show_my_drink()
Результат:
'''


class Soda:
    def __init__(self, adding=None):
        self.adding = adding

    def show_my_drink(self):
        if self.adding == None or type(self.adding) == int:
            print(f'Обычная газировка :(')
        else:
            print(f'Газировка и {self.adding}!')


drink1 = Soda()
drink2 = Soda('малина')
drink3 = Soda(5)
drink1.show_my_drink()
drink2.show_my_drink()
drink3.show_my_drink()

'''Задча 5
Евгению требуется проверить, возможно ли из представленных отрезков 
условной длины сформировать треугольник. 
Для этого он решил создать класс TriangleChecker, принимающий только 
положительные числа. 
С помощью метода is_triangle() возвращаются следующие значения (в 
зависимости от ситуации):
– Ура, можно построить треугольник!;
– С отрицательными числами ничего не выйдет!;
– Нужно вводить только числа!;
– Жаль, но из этого треугольник не сделать.
Пример запуска:
triangle1 = TriangleChecker([2, 3, 4])
print(triangle1.is_triangle())
triangle2 = TriangleChecker([77, 3, 4])
print(triangle2.is_triangle())
triangle3 = TriangleChecker([77, 3, 'Сторона3'])
print(triangle3.is_triangle())
triangle4 = TriangleChecker([77, -3, 4])
print(triangle4.is_triangle())
Результат выполнения:
Ура, можно построить треугольник!
Жаль, но из этого треугольник не сделать
Нужно вводить только числа!
С отрицательными числами ничего не выйдет!'''


class TriangleChecker:
    def __init__(self, sidesList):
        self.sidesList = sidesList

    def is_triangle(self):
        for side in self.sidesList:
            if type(side) == str:
                return 'Нужно вводить только числа!'
            elif side == 0 or side == None:
                return 'Жаль, но из этого треугольник не сделать'
            elif side < 0:
                return 'С отрицательными числами ничего не выйдет!'
            else:
                pass
        return 'Ура, можно построить треугольник!'


triangle1 = TriangleChecker([2, 3, 4])
print(triangle1.is_triangle())
triangle2 = TriangleChecker([None, 3, 4])
print(triangle2.is_triangle())
triangle3 = TriangleChecker([77, 3, 'Сторона3'])
print(triangle3.is_triangle())
triangle4 = TriangleChecker([77, -3, 4])
print(triangle4.is_triangle())
'''Задача 6
Есть три класса Donkey, Horse, Mul
• Класс Donkey имеет атрибуты name, age, living_area, typeDonkey, метод
display( )
“Осел по имени Spirit живет [место обитания] и он относится к грузовым 
ослам, ему [возраст] лет”
• Класс Horse имеет атрибуты name, age, typeHorse, breed метод horce_race( ) 
где есть следующая реализация:
“Лошадь с именем [имя] и с породой [порода] участвует в забеге ей 
[возраст] лет”
• Класс Mul это смесь лошади с ослом (множественное наследование). Также 
помимо атрибутов, которые были взяты от прародителей, есть свой метод в 
котором происходит объединение двух методов в один метод с родительских 
классов: display( ), race( ), но также классе Mul необходимо создать метод 
eating( ), где есть реализация:
«Мул может кушать много травы»'''


class Donkey:
    def __init__(self, name, age, living_area, typeDonkey):
        self.name = name
        self.age = age
        self.living_area = living_area
        self.typeDonkey = typeDonkey

    def display(self):
        return print(f'{self.typeDonkey} по имени {self.name} живет в {self.living_area}'
                     f' и он относится к грузовым ослам, ему {self.age} лет')


class Horse:
    def __init__(self, name, age, typeHorse, breed):
        self.name = name
        self.age = age
        self.typeHorse = typeHorse
        self.breed = breed

    def horse_race(self):
        print(f'{self.typeHorse} с именем {self.name} и с породой {self.breed} участвует в забеге ей {self.age} лет')


class Mule(Donkey, Horse):
    def __init__(self, name, age, living_area, typeDonkey, typeHorse, breed):
        Donkey.__init__(self, name, age, living_area, typeDonkey)
        Horse.__init__(self, name, age, typeHorse, breed)

    def muleMethod(self):
        return Donkey.display(self), Horse.horse_race(self)
    def eating(self):
        return print(f'{self.typeDonkey} может кушать много травы')


donkey = Donkey('Горбунок', 7, 'Поле', 'Осел')
donkey.display()
horse = Horse('Иа', 6, 'Пони', 'Единорог')
horse.horse_race()
mule = Mule('Горбунок', 5, 'Поле', 'Мул', 'Мул', 'гибрид')
mule.muleMethod()
mule.eating()
