#__str__ = Возвращает результат в строковом представлении при вызове имени объекта
#__del__
# __add__ __sub__
# __mul__
#

class Car:
    def __init__(self, modelName, petrolConsumption, yearModel):
        self.__modelName = modelName
        self.petrolConsumption = petrolConsumption
        self.yearModel = yearModel

    def carConsumption(self):
        print(f'This {self.__modelName}  needs {self.petrolConsumption} every 100 km!')

    def __str__(self):
        return f'Имя авто: {self.__modelName}'

    def __del__(self):
        return f'Авто {self.__modelName} было удалено!'

    def __add__(self, other):
        return other + self.petrolConsumption

    def __sub__(self, other):
        return other - self.petrolConsumption

    def __mul__(self, other):
        return other * self.petrolConsumption

    # def __div__(self, other):
    #     return self.petrolConsumption/other.petrolConsumption

    # def __divmod__(self, other):
    #     return other/self.petrolConsumption

    # def __idiv__(self, other):
    #     return other / self.petrolConsumption

    def __eq__(self, other):
        if self.petrolConsumption == other.petrolConsumption:
            return f'Первый объект равен второму'
        else:
            return f'Они не равны'

    def __gt__(self, other):
        if self.petrolConsumption > other.petrolConsumption:
            return f'Первый объект больше второго'
        else:
            return f'Второй объект больше первого'

    def __lt__(self, other):
        if self.petrolConsumption < other.petrolConsumption:
            return f'Второй объект больше первого'
        else:
            return f'Первый объект больше второго'

    def __ge__(self, other):
        if self.petrolConsumption >= other.petrolConsumption:
            return f'Расход топливо первой машины больше либо равен расходу второго'
        else:
            return 'Расход первой машины меньше чем у второй'

    def __le__(self, other):
        if self.petrolConsumption <= other.petrolConsumption:
            return f'Расход топливо первой машины меньше либо равен расходу второго'
        else:
            return 'Расход второй машины больше чем у первой'

    def __copy__(self, other):
        self.petrolConsumption = other.petrolConsumption

    def __len__(self):
        return len(self.__modelName)

def main():
    car1 = Car('BMW 525', 15, 1995)
    car1.carConsumption()

    print(car1)

    #del car1

    #print(car1)

    car2 = Car('BMW 7', 15, 1998)
    car2.carConsumption()

    #Суммирования двух объектов и
    #вычитание двух объектов
    print(car1 + car2)

    print(car2 - car1)
    print(car1 - car2)

    print(car1 + 20)

    print(car2 - 30)
    print(car1 - 40)

    # Умножение двух объектов и
    # деление двух объектов
    print(car1 * car2)
    print(car1 * 12)

    print(car2 * car1)
    print(car2 * 12)

    #Маг метод сравнения
    print(car1 >= car2)

    print(car1 <= car2)

    print(car1==car2)

    print(len(car1))

 #print(20 + car1)

if __name__ == '__main__':
    main()