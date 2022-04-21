#Создание класса Родителя
class Animal:
    def __init__(self, typeanimal, livingarea, typefood):
        self.animalType = typeanimal
        self.areaLiving = livingarea
        self.foodtype = typefood

    def display(self):
        print(f'Animal type: {self.animalType}'
              f'\nArea living: {self.areaLiving}'
              f'\nFood type: {self.foodtype}')

    def sleep(self):
        print(f'{self.animalType} is sleeping')

class Mind:
    def __init__(self, words ='Hello there!'):
        self.words = words
        #print(f'This animal can speak! ')

    def can_speak(self):
        print(f'This animal can speak! ')


class Predator(Animal):
    def __init__(self, typeanimal, livingarea, typefood, quantTeeth):
        Animal.__init__(self, typeanimal, livingarea, typefood)
        self.teethQuant = quantTeeth

    def hunting(self):
        print(f'This predator {self.animalType} and he eats {self.foodtype} by hunting'
              f' in {self.areaLiving} and {self.animalType} has {self.teethQuant} teeth')

    def display(self):
        super().display()
        print(f'Quant teeth: {self.teethQuant}')
        print('******************************')

class Monkey(Animal):
    def __init__(self, lenHand, lentail, typeanimal, livingarea, typefood):
        super().__init__(typeanimal, livingarea, typefood)
        self.handLength = lenHand
        self.tailLength = lentail

    def canClimbTree(self):
        print(f'This is monkey {self.animalType} and he eats {self.foodtype} and he can jump '
              f'from one tree to other tree in {self.areaLiving}'
              f'\n{self.animalType} has length tail {self.tailLength} sm and hand is {self.handLength} sm')

    def display(self):
        #super().display()
        print(f'Type of Monkey: {self.animalType }')
        print(f'Length hand: {self.handLength}')
        print(f'Length tail: {self.tailLength}')
        print('******************************')

class Parrot(Animal, Mind):
    def __init__(self, typeanimal, livingarea, typefood, words):
        Animal.__init__(self,typeanimal, livingarea, typefood)
        Mind.__init__(self,words)
        #super().can_speak()

    def display(self):
        super().display()
        print(f'This animal can fly!'
              f'\nAnd {self.animalType} says {self.words}')


def main():
    a1 = Animal('Cow', 'Farm', 'grass')
    a2 = Predator('Lion', 'Savanna', 'Meat',60)
    a3 = Monkey(55, 70, 'Gorilla', 'Jungle', 'Bananas')

    a1.display()
    print('**********************')
    a2.display()
    a3.display()

    a2.hunting()
    a3.canClimbTree()

    parrot1 = Parrot('Ara','Jungle','Corn','Vovka durak')
    parrot1.display()


    print(parrot1.areaLiving)
    print(parrot1.words)

    a2.sleep()
    a3.sleep()

    parrot1.sleep()

    # def sum(n1 = 1,n2 = 2):
    #     return n1+n2
    # print(sum())

    parrot2 =Parrot('Ara2','Jungle','Corn','Vovka durak')

if __name__=='__main__':
    main()




