'''Дан список чисел myList = [23,43,54,34,54,56].
Используя функцию enumerate() в заголовке цикла for ,
выполнить умножение каждого элемента на 10 и деление на 2
.'''

class Myclass:
    def __init__(self, myList):
        self.myList = myList

    def myFunction(self):
        for index, value in enumerate(self.myList):
            print(f'Результат деления индекса {index} - {value/2}\nРезультат умножения индекса {index} - {value*10}')

myCalc = Myclass([23, 43, 54, 34, 54, 56])
myCalc.myFunction()

