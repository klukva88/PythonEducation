#Кортежи

#Задача 1
myTuple = (10, 20, 30, 40)
myTuple = str(myTuple)
print(type(myTuple))

#Задача 2
typle2 = (10, 20, 30, 40)
print(len(typle2))

#Задача 3

aTuple = (3.4, 56, "Some", "Hi", 7, 3.8, 44)
print(f' Кортеж, начиная с третьего элетмента с конца: {aTuple[-3]}, \n '
      f'Каждый второй элемент, начиная с третьего: {aTuple[2::2]}')

#Задача 4 - Сконвертируйте из списка numList = [213,43,5,6,86] в кортежи.

numList = [213,43,5,6,86]
numTuple = tuple(numList)
print(type(numTuple))

# Задача  5
'''
Создайте кортеж состоящий из:
• 2 чисел
• строки
• числа с точкой
Выведите его через цикл while
'''

myTuple = [11, 122, 'Коля', 36.6]
index = 0
while index < len(myTuple):
    print(myTuple[index])
    index += 1







