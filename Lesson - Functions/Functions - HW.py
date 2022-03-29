'''Задача 1
Создать функцию, которая принимает в себя в качестве параметра трехзначное
число, а затем выводит их в обратном порядке'''
import datetime


def reverseNumber(number):
    number = str(number)  # Коневертирую int в строку т.е. в список
    return int(number[::-1])  # Возвращаю перевернутый список и конвертирую обратно в int


print(type(reverseNumber(123)))

'''Задача 2
Создать функцию, которая принимает в качестве параметра неопределенное
количество параметров, а затем находит среднее их значение'''


def avgFunc(*params):
    return print(sum(params) / len(params))


avgFunc(5, 5, 5, 9)

'''Задача 3
 Напишите функцию Python, которая принимает список и возвращает новый
список с уникальными элементами переданного в качестве параметра списка.'''


def uniqueList(*list):  # Принимаем неограниченное количество аргументов
    list = set(list)  # Конверируем в множество, чтобы исключить повторы
    return list


print(uniqueList(1, 2, 3, 'Вася', 'Вася', 1, 16))

'''Задача 4
Создать функцию, которая принимает в себя в качестве параметра три целых
числа, функция должна вывести количество положительных и количество
отрицательных чисел.'''

print('Задача 4 Вариант 2')

def countNumbers(num1, num2, num3):
    positive = []
    positive = 0
    if num1 > 0:
        positive += 1
    elif num2 > 0:
        positive += 1
    elif num3 > 0:
        positive += 1
    negative = 3 - positive
    return print(f' Отрицательных значений {negative}, Положительных {positive}')

print(countNumbers(1, -2, -3))

print('Задача 4 - Вариант 2 \n')
def countNumbers2(num1, num2, num3):
    listNumbers = [num1, num2, num3]
    positives = 0
    for number in listNumbers:
        if number > 0:
            positives += 1
    negatives = 3 - positives

    return print(f' Отрицательных значений {negatives}, Положительных {positives}')


print(countNumbers2(1, 2, -3))
print('Задача 4 - Вариант 3 \n')
def countNumbers3(*numbers):
    positives = len([num for num in numbers if num > 0])
    negatives = len(numbers) - positives
    return print(f' Отрицательных значений {negatives}, Положительных {positives}')

print(countNumbers2(-1, -2, -3))

'''Задача 5
Создать функцию, которая принимает в качестве параметра двузначное число,
необходимо найти сумму и произведение его цифр.'''

def sumAndMultuply(number):
    number = str(number)
    convertedNumber = [int(num) for num in number]
    numbersSum = sum(convertedNumber)
    numbersMultiply = convertedNumber[0] * convertedNumber[1]
    return print(f' Сумма цифр в числе {numbersSum}, Произведение цифр {numbersMultiply}')

sumAndMultuply(45)

'''Задача 6
У вас есть дата = «22/05/2023». Ваша задача написать функцию, которая узнает 
сколько остается дней до этой даты.'''

from datetime import *
setDate = datetime(day=22, month=5, year=2023)
def distanceToDate():
    distance = setDate - datetime.today()
    return distance.days

print(f' от сегодня до «22/05/2023» осталось {distanceToDate()} дней')

'''Задача 7
Создайте функцию, которая возвращает только нечетные значения из 
переданного списка'''

def onlyOdds(list):
    odds = [item for item in list if item%2 != 0]
    return print(f' Спиоск нечетный значений: {odds} ')

onlyOdds([1, 4, 7, 12, 22, 23, -1, -6])

'''Задача 8
Переделайте эту программу в качестве функции:
Транспортная компания использует следующий тариф для расчета стоимости (в 
долларах) доставки на основе веса посылки (в килограммах). В качестве 
передаваемого параметра используйте вес. В качестве возвращаемого результата 
вам необходимо вернуть стоимость доставки после проверки через if-else.
• Если вес находится в промежутке между 0 и 2 кг - то расчет за кг идет по тарифу 
3.5$ за кг.
• Если вес находится в промежутке между 3 и 5 кг - то расчет за кг идет по тарифу 
5.5$ за кг.
• Если вес находится в промежутке между 6 и 10 кг - то расчет за кг идет по 
тарифу 7$ за кг.
• Если вес до 50кг расчет за кг идет по тарифу 10$ за кг.
Если вес больше 50 кг, вернуть сообщение «посылка не может быть отправлена».'''


def checkParcell():
    parcelWeight = int(input('Введите вес посылки : '))
    if parcelWeight <= 2 and parcelWeight > 0:
        return print('Тариф $3.5 за кг')
    elif parcelWeight <= 5 and parcelWeight > 2:
        return print('Тариф $5.5 за кг')
    elif parcelWeight <= 10 and parcelWeight > 5:
        return print('Тариф $7 за кг')
    elif parcelWeight <= 50 and parcelWeight > 10:
        return print('Тариф $10 за кг')
    else:
        return print('Посылка не может быть принята')

checkParcell()



