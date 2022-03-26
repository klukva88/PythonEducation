'''Задача 1
Примите от пользователя его имя и отобразите через функции в формате:
‘Привет [имя], добро пожаловать в нашу программу!’'''


def displayName(userInput):
    print(f'Привет {userInput}, добро пожаловать в нашу программу!')


displayName(input('Введите свое имя: '))

'''
Задача 2
Создайте функцию, в которой происходит вычисление суммы двух чисел. В этой
функции необходимо принять от пользователя два числа и произвести сложение
между ними, затем это необходимо отобразить. Вызовите данную функцию.'''


def sumNumbers(number1, number2):
    return print(number1 + number2)


input1 = int(input('Введите 1е число: '))
input2 = int(input('Введите 2е число: '))
sumNumbers(input1, input2)

'''Задача 3
Примите от пользователя 3 числа и передайте ее в качестве параметра в функцию
calcAvg. Функция calcAvg должна найти среднее значения между переданными
3-мя числами. Посчитайте и верните в качестве результата среднее значение'''


def calcAvg(number1, number2, number3):
    avg = (number1 + number2 + number3) / 3
    return avg


num1 = int(input('Введите 1е число: '))
num2 = int(input('Введите 2е число: '))
num3 = int(input('Введите 3е число: '))

print(f' среднее значение: {calcAvg(num1, num2, num3)}')

'''Задача 4
Создайте функцию деления чисел, которая будет принимать три параметра.
Сделайте последний параметр со значением по-умолчанию.
Вызовите функцию два раза:
• с передачей третьего параметра
• без передачи третьего параметра'''


def divisionFunc(param1, param2, param3=3):
    result = param1 / param2 / param3
    return result


print(f'Вызов функции с 3-мя параметрами: {divisionFunc(6, 2, 8)} \n'
      f'Вызов функции с 2-мя параметрами: {divisionFunc(15, 3)}')

'''Задача 5
Создать функцию, которая в качестве промежутков для range будет
принимать 3 параметра — это num1 — для стартовой точки, num2 — для
конечной точки и num3 — для шага. В этой функции необходимо
отобразить все эти значения'''


def rangeFunction(start, stop, step):
    for i in range(start, stop, step):
        print(i)


print(rangeFunction(1, 10, 2))

'''Задача 6
Создайте функцию в параметр принимается список, она должна возвращать
в качестве результата только четные числа из этого списка.'''


def listFunc(list):
    resultList2 = [item for item in list if item % 2 == 0]
    return resultList2

'''resultList = []
    for item in list:
        if item % 2 == 0:
            resultList.append(item)
        else:
            continue
    return resultList'''

list = [10, 3, 4, 15, 13]
print(listFunc(list))
