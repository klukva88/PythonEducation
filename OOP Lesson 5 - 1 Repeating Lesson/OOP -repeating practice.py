class Xerocopy:
    def __init__(self, nameModel, nameDoc, copyQuantity, copyLimit=100):
        self.__nameModel = nameModel
        self.nameDoc = nameDoc
        self.copyQuantity = copyQuantity
        self.copyLimit = copyLimit

        @property
        def nameModel(self):
            return self.nameModel
        @nameModel.setter
        def nameModel(self, nameModel):
            self.__nameModel = nameModel
#Печатать через for цикл, пока не кончится бумага

    def copy(self):
        if self.copyLimit > self.copyQuantity:
            self.copyLimit = self.copyLimit - self.copyQuantity
            print(f' Модель {self.__nameModel} cкопировало документ {self.nameDoc} в количестве {self.copyQuantity}\n'
                  f'Осталось {self.copyLimit} шт')
        else:
            print(f'Не осталось листов в копировальном аппарате!')

    def addList(self, extraLists):

        print(f'У вас на копировальном аппарате было {self.copyLimit} листов, после пополнения стало {self.copyLimit + extraLists} листов')
        self.copyLimit = self.copyLimit+extraLists

class LGTech(Xerocopy):
    pass



def main():
    machine = LGTech('LG123', 'Паспорт.pdf', 101)
    machine.copy()
    machine.addList(20)
    machine.copy()

if __name__ == '__main__':
    main()