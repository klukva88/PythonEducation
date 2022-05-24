from math import pow

class Car:
    def __init__(self, modelName, petrolConsumption, yearModel):
        self.__modelName = modelName
        self.petrolConsumption = petrolConsumption
        self.yearModel = yearModel

    def carConsumption(self):
        print(f'This {self.__modelName}  needs {self.petrolConsumption} every 100 km!')

    # def __str__(self):
    #     return f'{self.__modelName}'

    def __del__(self):
        return f'Авто {self.__modelName} было удалено!'

    def __add__(self, other):
        if isinstance(other, Car):
            return self.petrolConsumption + other.petrolConsumption
        elif isinstance(other, (int,float)):
            return self.petrolConsumption + other
        #return self.petrolConsumption + other

    def __radd__(self, other):
        if isinstance(other, Car):
            return self.petrolConsumption + other.petrolConsumption
        elif isinstance(other, (int, float)):
            return self.petrolConsumption + other

    def __sub__(self, other):
        if isinstance(other, Car):
            return self.petrolConsumption - other.petrolConsumption
        elif isinstance(other, (int, float)):
            return self.petrolConsumption - other
        # return self.petrolConsumption + other

    def __rsub__(self, other):
        if isinstance(other, Car):
            return self.petrolConsumption - other.petrolConsumption
        elif isinstance(other, (int, float)):
            return self.petrolConsumption - other
        # return self.petrolConsumption + other

    def __mul__(self, other):
        return other * self.petrolConsumption

    def __rmul__(self, other):
        return other * self.petrolConsumption

    #division
    def __truediv__(self, other):
        if isinstance(other, Car):
            return self.petrolConsumption / other.petrolConsumption
        elif isinstance(other, (int, float)):
            return self.petrolConsumption / other

    def __rtruediv__(self, other):
        if isinstance(other, Car):
            return self.petrolConsumption / other.petrolConsumption
        elif isinstance(other, (int, float)):
            return self.petrolConsumption / other

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

    #Post incrementation, post decrementation
    #Post mult, post div

    def __iadd__(self, other):
        if isinstance(other, Car):
            self.petrolConsumption += other.petrolConsumption

        elif isinstance(other, (int,float)):
            self.petrolConsumption = self + other

        #self.petrolConsumption = self + other

        return self.petrolConsumption
        #return self.petrolConsumption

    def __isub__(self, other):
        if isinstance(other, Car):
            self.petrolConsumption -= other.petrolConsumption

        elif isinstance(other, (int,float)):
            self.petrolConsumption = self - other

        #self.petrolConsumption = self + other

        return self.petrolConsumption

    def __imul__(self, other):
        if isinstance(other, Car):
            self.petrolConsumption *= other.petrolConsumption

        elif isinstance(other, (int,float)):
            self.petrolConsumption = self * other

        return self.petrolConsumption

    def __itruediv__(self, other):
        if isinstance(other, Car):
            self.petrolConsumption /= other.petrolConsumption

        elif isinstance(other, (int,float)):
            self.petrolConsumption = self / other

        return self.petrolConsumption

    # def __pow__(self, power, modulo=None):
    #     return pow(self.petrolConsumption, power)

    # def __lshift__(self, other):
    #     pass
    #
    # def __rshift__(self, other):
    #     pass

    def __mod__(self, other):
        return self.petrolConsumption % other


    def __rmod__(self, other):
        return self.petrolConsumption % other

    def __imod__(self, other):
        if isinstance(other, Car):
            self.petrolConsumption %= other.petrolConsumption

        elif isinstance(other, (int,float)):
            self.petrolConsumption = self % other

        return self.petrolConsumption

def main():
    car1 = Car('BMW 525', 15, 1995)
    car2 = Car('BMW 7', 5, 1998)
    car3 = Car('BMW X5', 17, 2010)

    #addition
    print(car1 + car2) #30
    print(car1 + 30.25)  # 30
    print(10 + car1)  # 25

    #substruction
    print(10 - car1)  # 25

    #division
    print(car1 / car2)
    print(car1 / 3)
    print(3 / car1)

    car1 += 1 #car1 = car1 + 1
    print(type(car1))

    car1 -= 1  # car1 = car1 + 1
    print(car1)

    car2 *= 2
    print(car2)
    #print()

    #print(pow(car3,3))

    print(car3 % 3)
    print(car3)

if __name__ == '__main__':
    main()