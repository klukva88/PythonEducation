class CoffeeMachine:
    #__modelName = 'Beko'
    def __init__(self, namemodel, quantOfMilk, quantofwater, quantCoffee):
        self.__modelName = namemodel
        self.__qMilk = quantOfMilk
        self.__qWater = quantofwater
        self.__qCoffee = quantCoffee

    def get_modelname(self):
        return self.__modelName

    def set_modelName(self, newModelname):
        if newModelname.isnumeric():
            pass
        else:
            self.__modelName = newModelname

    def get_milk(self):
        return self.__qMilk

    def set_milk(self, newQuantMilk):
        if newQuantMilk > 0:
            self.__qMilk = newQuantMilk
        else:
            pass

    # def get_water(self):
    #     return self.__qWater

    def set_water(self, newQuantWater):
        if newQuantWater > 0:
            self.__qWater = newQuantWater
        else:
            pass

    def get_coffee(self):
        return self.__qCoffee

    # def set_coffee(self, newQuantCoffee):
    #     # if newQuantCoffee > 0:
    #     #     self.__qCoffee = newQuantCoffee
    #     # else:
    #     #     pass
    #
    #     self.__qCoffee = newQuantCoffee


    def makeLatte(self):
        milkQuantlatte = 200
        waterqantLatte = 250
        coffelatte = 2
        if self.__qMilk <= 0 or self.__qWater <= 0 or self.__qCoffee <=0:
            print(f'Добавьте пожалуйста ингридиенты! '
                  f'Кол-во воды, кофе или молока не достаточно!')

            print('Не удалось приготовить Латте!')
        else:
            self.__qMilk = self.__qMilk - milkQuantlatte
            self.__qWater -= waterqantLatte
            self.__qCoffee -= coffelatte

            print('Ваше Латте готово!')

    def makeCappucino(self):
        milkQuantCappucino = 100
        waterqantCappucino = 300
        coffeCappucino = 4

        if self.__qMilk <= 0 or self.__qWater <= 0 or self.__qCoffee <=0:
            print(f'Добавьте пожалуйста ингридиенты! '
                  f'Кол-во воды, кофе или молока не достаточно!')

            print('Не удалось приготовить Каппучино!')
        else:
            self.__qMilk = self.__qMilk - milkQuantCappucino
            self.__qWater -= waterqantCappucino
            self.__qCoffee -= coffeCappucino

            print('Ваше Каппучино готово!')

    def displayInfo(self):
        print(f'Model Name: {self.__modelName}'
              f'\nMilk :{self.__qMilk}'
              f'\nWater: {self.__qWater}'
              f'\nCoffe: {self.__qCoffee}')

    def addIngridients(self, newquantMilk, newquantWater, newquantCoffee):
        if newquantMilk <= 0 or newquantWater <= 0 or newquantCoffee <=0:
            print(f'Ингридиенты не могут быть отрицательными значениями! ')
        else:
            self.__qMilk = self.__qMilk + newquantMilk
            self.__qWater += newquantWater
            self.__qCoffee += newquantCoffee

        print('Новое количество: ')
        self.displayInfo()

coffeMachine1 = CoffeeMachine('Samsung', 1000, 1000, 10)
#print(coffeMachine1.__modelName)
#coffeMachine1.__modelName = 'Beko'

coffeMachine1.displayInfo()
print(coffeMachine1.get_modelname())
coffeMachine1.set_modelName('LG')

print(coffeMachine1.get_modelname())
coffeMachine1.displayInfo()

print(coffeMachine1.get_modelname())

#coffeMachine1.setModelName('Beko')
coffeMachine1.displayInfo()
coffeMachine1.set_milk(-100)
coffeMachine1.set_water(-100)
#coffeMachine1.addIngridients(-100, -200, 10)

coffeMachine1.displayInfo()

coffeMachine1.addIngridients(100, 200, 10)

print(coffeMachine1.get_coffee())

#print(coffeMachine1.get)
coffeMachine1.set_water(10000)
coffeMachine1.displayInfo()
