
#Задача 1
def bold(text_function):
    def wrapper():
        print('<b>')
        text_function()
        print('</b>')
    return wrapper

def italic(text_function):
    def wrapper():
        print('<i>')
        text_function()
        print('</i>')
    return wrapper

def underline(text_function):
    def wrapper():
        print('<u>')
        text_function()
        print('</u>')
    return wrapper

@bold
@underline
def theText():
    print("Какой нибудь текст")

theText()

#Задача 2

def avgValue(decoratedFunction):
    def wrapper(myList):
        decoratedFunction(myList)
        print(f'Среднее значение {sum(myList)/len(myList)}')
    return wrapper

@avgValue
def listFunction(myList):
    for item in myList:
        print(item)


listFunction([1, 3, 4])

#Задача 3
def saveTextFile(decoratedFunction):
    def wrapper(list):
        decoratedFunction(list)
        with open('resultsList.txt', 'w', encoding='utf-8') as resultsList:
            resultsList.writelines('Все элементы списка:\n')
            for number in list:
                resultsList.writelines(str(number)+'\n')
            resultsList.writelines(f'Сумма всех значений в списке:\n'
                                    f'{sum(list)}')

    return wrapper

@saveTextFile
def show_list(list):
    return list

show_list([2, 25, 34])


class Decorator:
    def __init__(self, function_to_decorate):
        self.function_to_decorate = function_to_decorate

    def __call__(self, list):

        with open('resultsList2.txt', 'w', encoding='utf-8') as resultsList:
            resultsList.writelines('Все элементы списка:\n')
            for number in list:
                resultsList.writelines(str(number) + '\n')
            resultsList.writelines(f'Сумма всех значений в списке:\n'
                                   f'{sum(list)}')


@Decorator
def show_list(list):
    return list

show_list([2, 25, 22])

import openpyxl
class Decorator2:
    def __init__(self, function_to_decorate):
        self.function_to_decorate = function_to_decorate

    def __call__(self, lst):
        #self.function_to_decorate(lst)
        wb = openpyxl.Workbook()
        sheet = wb.active

        data = (
            ('Количество элементов', 'Среднее значение', 'Сумма элементов'),
            (len(lst), sum(lst)/len(lst), sum(lst))
        )
        for row in data:
            sheet.append(row)

        wb.save('calcList.xlsx')


@Decorator2
def my_list_fun(lst):
    return lst

my_list_fun([34,54,3,54,65,7,11])