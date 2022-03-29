'''Задача 1
Функция, которая переворачивает в обратном направлении переданное имя:
def reverseName(n)
    return n[::-1]
'''

reverseNameLambda = lambda n: n[::-1]
print(reverseNameLambda("Вася"))

'''Задача 2
Функция которая находит сумму двухзначного числа'''

findsum = lambda num1: num1 // 10 + num1 % 10

print(findsum(12))

'''Задача 3
Функция, которая печатает каждую вторую букву:'''

printEverySecondLetter = lambda word: word[::2]

print(printEverySecondLetter('ваорыоваоываывоаыовлаоы'))

'''Задача4
Функция, которая находит среднее значение элементов от списка:'''

findavg = lambda someList: sum(someList) / len(someList)

print(findavg([1,2,3,4,5,6,7]))

'''Задача5
Создайте лямбду выражения, которая принимает в себя 2 числа где 2-ое
переданное является степенью, а 1-ое число — это то число, которую
необходимо возвести в степень'''

powNumbers = lambda number, power: number**power

firstNumber = int(input('Введите 1-e число: '))
secondNumber = int(input('Введите 2-e число:'))
print(f' Число {firstNumber} в степени {secondNumber} - это {powNumbers(firstNumber, secondNumber)}')

'''Задача 6
Создайте программу, которая проверяет делятся ли два числа без остатка. Для
того, чтобы проверить на делимость используйте лямбду выражения с
проверкой результата с помощью if-else конструкции.'''

checkRest = lambda number1, number2: print('Делится без остатка') if number1%number2 == 0 else (print('Делится с остатком'))
numberToCheck1 = int(input('Введите 1-е число: '))
numberToCheck2 = int(input('Введите 2-е число: '))
checkRest(numberToCheck1, numberToCheck2)