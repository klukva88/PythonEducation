#Задача 1
class Teacher:
    #СОздаем контсруктор главного класса
    def __init__(self, fullName, experience, subject, studentsNumber):
        self.fullName = fullName
        self.experience = experience
        self.subject = subject
        self.studentsNumber = studentsNumber

    def displayInfo(self):
        print(f' ФИО: {self.fullName}')
        print(f' Стаж: {self.experience}')
        print(f' Предмет: {self.subject}')
        print(f' Количество студентов: {self.studentsNumber}')

class GeographyTeacher(Teacher):
    def __init__(self, fullName, experience, subject, studentsNumber, country):
        super().__init__(fullName, experience, studentsNumber, subject)
        self.country = country

    def findCapital(self):
        if self.country == 'Россия':
            return 'Москва'
        elif self.country == 'Кыргызстан':
            return 'Бишкек'
        elif self.country == 'Германия':
            return 'Берлин'
        else:
            pass

    def displayInfo(self):
        super().displayInfo()
        print(self.country)

class DrawingTeacher(Teacher):
    def __init__(self, fullName, experience, subject, studentsNumber, figure):
        super().__init__(fullName, experience, subject, studentsNumber)
        self.figure = figure
    def findSimilarObject(self):
        if self.figure == 'Треугольник':
            return 'Пирамида похожа на треугольник'
        elif self.figure == 'Круг':
            return 'Солнце похоже на круг'
        elif self.figure == 'Прямоугольник':
            return 'Дом похож на прямоугольник'
        else:
            pass
    def displayInfo(self):
        super().displayInfo()
        print(self.figure)


class MathTeacher(Teacher):
    def __init__(self, fullName, experience, subject, studentsNumber, num1, num2, num3):
        super().__init__(fullName, experience, subject, studentsNumber)
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    def findAverage(self):
        avg = (self.num1 + self.num2 + self.num3)/3
        return avg
    def displayInfo(self):
        super().displayInfo()
        print(f'Число 1 {self.findAverage()}')


#Задача 2
class MathGeographyTeacher(GeographyTeacher, MathTeacher):
    def __init__(self, fullName, experience, subject, studentsNumber, num1, num2, num3, country):
        Teacher.__init__(self,fullName, experience, subject, studentsNumber)
        GeographyTeacher.__init__(self, studentsNumber, country)
        MathTeacher.__init__(self, num1, num2, num3)

    def introducing(self):
        print(f'Меня зовут {self.fullName} - я веду Математику и Географию')


teacher = MathTeacher('Василий', 12, 'Math', 20, 2, 2, 2)
teacher.displayInfo()
teacher.findAverage()
teacher2 = MathGeographyTeacher('Ганс', 5, 'Math and Geo', 20, 1, 1, 2, 'Германия')
teacher2.introducing()
#print(teacher.findCapital())