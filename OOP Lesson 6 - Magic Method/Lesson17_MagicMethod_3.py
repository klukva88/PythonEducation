class Car:
    def __init__(self, modelName, petrolConsumption, yearModel, ownerList):
        self.__modelName = modelName
        self.petrolConsumption = petrolConsumption
        self.yearModel = yearModel
        self.ownerList = ownerList

    def carConsumption(self):
        print(f'This {self.__modelName}  needs {self.petrolConsumption} every 100 km!')

    def __str__(self):
        return f'Имя авто: {self.__modelName}'

    def display(self):
        print(f'Модель машины: {self.__modelName}'
              f'\nРасход топлива: {self.petrolConsumption}'
              f'\nГод выпуска: {self.yearModel}')

        print(f'Текующий и прошлые Владельцы {self.__modelName} авто: ')
        for name in self.ownerList:
            print(f'{name}', end="\n")

    def __add__(self, other):
        return other + self.petrolConsumption

    def __sub__(self, other):
        return other - self.petrolConsumption

    #Использ-ся когда необходимо высвободить память компьютера
    def __del__(self):
        print(f'Объект Авто {self.__modelName} было удалено!')

    def __delitem__(self, key):
        #self.ownerList.remove(key)
        del self.ownerList[key]

    def __getitem__(self, item):
        return self.ownerList[item]

    def __contains__(self, item):
        if item in self.__modelName:
            return True

        return False


def main():
    car1 = Car('Audi 100', 15, 2010, ['Adilet Toktosunov', 'Sergei Dovlatov', 'Aisuulu Buranova',
                                    'Arstan Bolotov', 'Tamara Sergeeva'])

    print(car1 + 20)
    car1.display()
    car1.yearModel = 2012
    #car1.display()

    #del car1['Adilet Toktosunov']
    del car1[1]
    # del car1.yearModel
    #car1.display()

    print(car1[3])

    carname = 'BMW X5'
    print('Audi' in car1)




if __name__ == '__main__':
    main()