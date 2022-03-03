#Задача 1
import copy

num = [123,4,45,6,7]
print(max(num))
print(min(num))
#Задача 2

numList = [21,43,54,6,76,8,34]
print('сумма', sum(numList))
print('Среднее Арифметическое: ', sum(numList)/len(numList))
#Задача 3

alphabetList = ['a', 's', 'd', 't']

print(sorted(alphabetList))
alphabetList.reverse()
print(alphabetList)

#Задача 4
#Добавить цифры в конец списка
num2 = [45, 61]
num.extend(num2)

#Удалить последние 2 элемента списка
print(num)
numList.pop()
numList.pop()
print(numList)

#Вставить цифру в самом начале списка
numList2 = [23,434,61,76,2]
numList2.insert(0, 45)
print(numList2)

#Задача 5
#Поверхностное копирование
someList = [12, 454, 65, 76, 1, [10]]
superficialCopy = copy.copy(someList)
superficialCopy[5].append(100)
print('Исходный массив: ', someList, '  Поверхностно скопированный: ', superficialCopy)

#Глубокое копирование
someList2 = [12, 454, 65, 76, 1, [11]]
deepCopy = copy.deepcopy(someList2)
deepCopy[5].append(101)
print('Исходный массив: ', someList2, '  Глубоко скопированный: ', deepCopy)


