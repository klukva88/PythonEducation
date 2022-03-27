'''Задача 1
Создать функцию, которая принимает в себя в качестве параметра трехзначное
число, а затем выводит их в обратном порядке'''


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
