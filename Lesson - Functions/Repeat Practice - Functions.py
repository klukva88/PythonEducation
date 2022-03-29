'''Задача 1
Создать функцию, которая принимает в себя в качестве параметра трехзначное
число, а затем выводит их в обратном порядке'''


def reverse(number):
    number = str(number)
    return int(number[::-1])


print(reverse(123))

'''Задача 2
Создать функцию, которая принимает в качестве параметра неопределенное
количество параметров и умножает каждую из них на 3'''


def multiplyPerThree(*args):
    multiply = [item * 3 for item in args]
    return multiply


print(multiplyPerThree(10, 20, 30, 50))

'''Задача 3
Создать функцию, которая принимает в себя в качестве параметра три целых
числа, функция должна вывести количество положительных и количество
отрицательных чисел'''


def countPositivesAndNegatives(num1, num2, num3):
    listOfNumbers = [num1, num2, num3]
    positives = len([positive for positive in listOfNumbers if positive > 0])
    negatives = 3 - positives
    return print(f'Положительных - {positives}, отрицательных {negatives}')


countPositivesAndNegatives(1, -2, -6)

'''Задача 4
Ваша задача написать функцию, которая узнает сколько остается дней до
определенной даты. Для вызова этой функции вам необходимо передать дату,
после которой вам должно вернутся значение в днях сколько остается времени
до этой самой даты'''
from datetime import *


def daysToDate(usersDate):
    howManyDays = (usersDate - datetime.today()).days
    if howManyDays > 0:
        return howManyDays
    else:
        return print('Дата в прошлом')


userDate = datetime(year=2022, month=12, day=31)
print(daysToDate(userDate))

'''Задача 5
Написать лямбду выражение, которое принимает в себя два аргумента num1 и
num2 и возвращает результат деления num2 на num1'''

devidefunc = lambda num1, num2: num2 / num1
print(devidefunc(2, 4))

'''Задача 6
Необходимо создать функцию, которая, принимая в себя какое-нибудь число
возвращает ответ «Четное» или «Не четное» значение. Далее на основе этой
функции необходимо проверить данный список [12,33,45 ,4,54,1,32,11 ,67,88]
используя ранее созданную функцию на «Четность» или «Не четность»
используя map. У вас должен вернуться следующий новый список:'''

# checkOdds = lambda number: 'Четный' if number % 2 == 0 else ('Нечетный')

listToCheck = [12, 33, 45, 4, 54, 1, 32, 11, 67, 88]
# result = [checkOdds(item) for item in listToCheck]
result = list(map(lambda number: 'Четный' if number % 2 == 0 else ('Нечетный'), listToCheck))
print(result)

'''Задча 7
Есть следующий список:
[‘HELLO’,’HOW ARE YOU’, ‘I AM FINE’, ‘THANK YOU’]
Используя map и лямбду выражения создайте новый список, в котором
содержится этот же список, но в нижнем регистре'''
wordList = ['HELLO', 'HOW ARE YOU', 'I AM FINE', 'THANK YOU']
newList = list(map(lambda word: str.lower(word), wordList))
print(newList)