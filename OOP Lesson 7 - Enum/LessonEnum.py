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

        counter = 1
        for name in self.ownerList:
            print(f'{counter}.{name}', end="\n")
            counter+=1

        print('*'*10)

        for indexnum, name in enumerate(self.ownerList, 1):
            print(f'{indexnum}.{name}', end="\n")

        print('*' * 10)
    
        for indexnum, name in enumerate(self.ownerList):
            print(f'{indexnum + 1}.{name}', end="\n")

        print('*' * 10)

        for elem in enumerate(self.ownerList , 1):
            print(f'{elem[0]}.{elem[1]}', end="\n")

    def changeList(self):
        for indexnum, name in enumerate(self.ownerList):
            self.ownerList[indexnum] = f'{indexnum + 1} ый владелец {name}'


def main():
    car1 = Car('Audi 100', 15, 2010, ['Adilet Toktosunov', 'Sergei Dovlatov', 'Aisuulu Buranova',
                                    'Arstan Bolotov', 'Tamara Sergeeva'])

    car1.display()

    name = 'Adilet'

    for indexNum, letter in enumerate(name):
        print(f'{indexNum+1} ая буква в имени человека -- {letter}')

    car1.changeList()
    print(car1.ownerList)
    #car1.display()

if __name__ == '__main__':
    main()