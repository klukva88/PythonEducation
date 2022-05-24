'''Задача 1
Создайте класс Student, которая принимает через конструктор
следующие аргументы:
• name - имя студента
• payment - сумма контракта
• marks - словарь с оценками по разным предметам, где
ключами выступают название предметов
• список задолженностей по различным предметам'''

class Student:
    def __init__(self, name, payment, marks, debtList):
        self.name = name
        self.payment = payment
        self.marks = marks
        self.debtList = debtList

    def averageMark(self):
        return sum(self.marks.values()) / len(self.marks)

    def display(self):
        for index, value in enumerate(self.debtList):
            print(f'Debt #{index+1} is {value}')
        for index, value in enumerate(self.marks):
            print(f' #{index+1} {value} mark is {self.marks[value]}')

    def display_using_generator(self):
        for debt in self.debtList:
            yield debt


    '''Внутри данного класса создайте следующие магические методы:
    __str__ - для вызова имени студента'''

    def __str__(self):
        return self.name

    '''__add__ / __radd__ /__iadd__ - для добавления к payment другую 
    сумму контракта, либо для суммирования контрактов двух и более 
    студентов'''

    def __add__(self, other): #Складывание сумм контрактов, если слева экземпляр класса
        if isinstance(other, Student):
            return self.payment + other.payment
        elif isinstance(other, (int, float)):
            return self.payment + other

    def __radd__(self, other):  #Складывание сумм контрактов, если справа экземпляр класса
        if isinstance(other, Student):
            return self.payment + other.payment
        elif isinstance(other, (int, float)):
            return self.payment + other

    def __iadd__(self, other): #Добавление новой суммы в контракт
        if isinstance(other, (int, float)):
            self.payment += other
            return self.payment
        else:
            return 'Введите число!'


    '''__sub__ / __rsub__ /__isub__ - для вычитания контракта одного 
    студента от контракта другого студента
    '''
    def __sub__(self, other): #вычитание величины контракта, если слева экземпляр класса
        if isinstance(other, Student):
            return self.payment - other.payment
        elif isinstance(other, (int, float)):
            return self.payment - other

    def __rsub__(self, other):  #вычитание величины контракта, если справа экземпляр класса
        if isinstance(other, Student):
            return self.payment - other.payment
        elif isinstance(other, (int, float)):
            return self.payment - other

    def __isub__(self, other): #вычитание числа из контракта
        if isinstance(other, (int, float)):
            self.payment -= other
            return self.payment
        else:
            return 'Введите число!'

    '''__truediv__ / __rtruediv__ /__itruediv__- для деления контракта 
    студента на определенное значение'''

    def __truediv__(self, other): #Деление величины контракта, если слева экземпляр класса
        if isinstance(other, Student):
            return self.payment / other.payment
        elif isinstance(other, (int, float)):
            return self.payment / other

    def __rtruediv__(self, other):  #Деление величины контракта, если справа экземпляр класса
        if isinstance(other, Student):
            return self.payment / other.payment
        elif isinstance(other, (int, float)):
            return self.payment / other

    def __itruediv__(self, other): #Деление величины контракта на число с перезаписью переменной
        if isinstance(other, (int, float)):
            self.payment /= other
            return self.payment
        else:
            return 'Введите число!'

    '''__mul__ / __rmul__ /__imul__- для умножение контракта студента на 
    определенное значение'''

    def __mul__(self, other): #Умножение величины контракта, если слева экземпляр класса
        if isinstance(other, Student):
            return self.payment * other.payment
        elif isinstance(other, (int, float)):
            return self.payment / other

    def __rmul__(self, other):  #Умножение величины контракта, если справа экземпляр класса
        if isinstance(other, Student):
            return self.payment * other.payment
        elif isinstance(other, (int, float)):
            return self.payment / other

    def __imul__(self, other): #Умножение величины контракта на число с перезаписью переменной
        if isinstance(other, (int, float)):
            self.payment *= other
            return self.payment
        else:
            return 'Введите число!'

    '''__pow__ / __rpow__ /__ipow__- для увеличения контракта на 
    определенную сумму по степени'''

    def __pow__(self, other):  # Умножение величины контракта, если слева экземпляр класса
        if isinstance(other, Student):
            return self.payment ** other.payment
        elif isinstance(other, (int, float)):
            return self.payment / other

    def __rpow__(self, other):  # Умножение величины контракта, если справа экземпляр класса
        if isinstance(other, Student):
            return self.payment ** other.payment
        elif isinstance(other, (int, float)):
            return self.payment / other

    def __ipow__(self, other):  # Умножение величины контракта на число с перезаписью переменной
        if isinstance(other, (int, float)):
            self.payment **= other
            return self.payment
        else:
            return 'Введите число!'

    '''__getitem__ - для того, чтобы получить оценку для определенного 
    предмета'''

    def __getitem__(self, item):
        return self.marks[item]

    def __lt__(self, other):
        if isinstance(other, Student):
            if self.averageMark() < other.averageMark():
                return f'Average mark of {self.name} is less then average mark of {other.name}'
            else:
                return f'Average mark of {self.name} is higher then average mark of {other.name}'
        elif isinstance(other, (int, float)):
            if self.averageMark() < other:
                return f'Average mark of {self.name} is less then {other}'
            else:
                return f'Average mark of {self.name} is higher then {other}'

    def __gt__(self, other):
        if isinstance(other, Student):
            if self.averageMark() > other.averageMark():
                return f'Average mark of {self.name} is higher then average mark of {other.name}'
            else:
                return f'Average mark of {self.name} is less then average mark of {other.name}'
        elif isinstance(other, (int, float)):
            if self.averageMark() > other:
                return f'Average mark of {self.name} is higher then {other}'
            else:
                return f'Average mark of {self.name} is less then {other}'

    def __le__(self, other):
        if isinstance(other, Student):
            if self.averageMark() <= other.averageMark():
                return f'Average mark of {self.name} is less or equal to the average mark of {other.name}'
            else:
                return f'Average mark of {self.name} is higher then average mark of {other.name}'
        elif isinstance(other, (int, float)):
            if self.averageMark() <= other:
                return f'Average mark of {self.name} is less or equal {other}'
            else:
                return f'Average mark of {self.name} is higher then {other}'

    def __ge__(self, other):
        if isinstance(other, Student):
            if self.averageMark() >= other.averageMark():
                return f'Average mark of {self.name} is higher or equal to the average mark of {other.name}'
            else:
                return f'Average mark of {self.name} is less then average mark of {other.name}'
        elif isinstance(other, (int, float)):
            if self.averageMark() >= other:
                return f'Average mark of {self.name} is higher or equal {other}'
            else:
                return f'Average mark of {self.name} is less then {other}'

    def __eq__(self, other):
        if isinstance(other, Student):
            if self.averageMark() == other.averageMark():
                return f'Average mark of {self.name} is equal to the average mark of {other.name}'
            else:
                return f'Average mark of {self.name} is not equal average mark of {other.name}'
        elif isinstance(other, (int, float)):
            if self.averageMark() == other:
                return f'Average mark of {self.name} is equal to  {other}'
            else:
                return f'Average mark of {self.name} is not equal {other}'

    def __delitem__(self, key):
        del self.marks[key]
        return print(f'{key} mark was deleted!')

    def __len__(self):
        return len(self.debtList)

    def __call__(self, *args, **kwargs):
        return self.averageMark()

    def __contains__(self, item):
        return True

    def __del__(self):
        del self

student1 = Student('Vasya', 10, {'English': 5, 'Math': 4, 'PE': 2, 'Chemistry': 3}, ['PE', 'Chemistry'])
student2 = Student('Kolya', 15, {'English': 2, 'Math': 3, 'PE': 5, 'Chemistry': 5}, ['English', 'Math'])
print(student1 < student2)
print(student2 > student1)
print(f'{student1} has {len(student1)} debts')
print(student1())
print('PE' in student1)
student1.display()
for debt in student2.display_using_generator():
    print(debt)


def myGenerator():
    number = int(input('Введите число до которого вы хотите вычислить сумму: '))
    squaresList = []
    for num in range(0,number+1):
        num = num ** 2
        yield num
        squaresList.append(num)
    print(f'Сумма переданных значений: {sum(squaresList)}')
    print(f'Среднее значение переданных значений: {sum(squaresList)/len(squaresList)}')



for number in myGenerator():
    print(number)
# myNumber()


#del student2['English']
#del student1
# print(student2.marks)
# print(student2<10)
# print(student2 == 10)
#
# print(type(student2))
# print(11 + student2)
# student2 += 11
# print(student2)
# student2 /= 4 #Получается здесь stundent2 - это уже переменная а не экземпляр класса?
#print(type(student2))

#student2 **= 0.5
#print(student2)

#print(student2['English'], student2['Math'])

