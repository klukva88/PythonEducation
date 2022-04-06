import random
from random import *
'''Задача 1
У вас есть список из 8 людей:
listNames = ['Esen', 'Timur', 'Burul', 'Adik', 'Bermet', 'Asan', 'Elena', 'Murat' ]
Они все желают поехать в горы.
Вам необходимо создать программу, которая случайным образом удалит 4-х
людей со списка, так как в легковую машину поместятся только 4 человека (не
включая водителя).
Пример исполнения программы:
Полный список желающих поехать на поход:
['Esen', 'Timur', 'Burul', 'Adik', 'Bermet', 'Asan', 'Elena', 'Murat']
Со списка людей удалили: Elena
Со списка людей удалили: Timur
Со списка людей удалили: Murat
Со списка людей удалили: Adik
Список тех кто поедут на поход:
['Esen', 'Burul', 'Bermet', 'Asan']'''


listNames = ['Esen', 'Timur', 'Burul', 'Adik', 'Bermet', 'Asan', 'Elena', 'Murat' ]
def removePersons(persons):
    for i in range(0,4):
        removedPerson = choice(persons)
        persons.remove(removedPerson)
        print(f'Со списка удалили: {removedPerson}')
    print(f'Спиоск тех кто поедет в поход: {listNames}')

removePersons(listNames)

'''Задача 2
Создайте программу, которая составляет список людей со случайной длиной в 
промежутке от 1-го до 15-ти'''
def randomNameList():
    listRange = randint(1, 5)
    print(f'Случайная длина для вашего списка людей - {listRange}')
    nameList = []
    for i in range(0, listRange):
        print(f'Введите имя {i+1} человека: ', end='')
        newName = input(' ')
        nameList.append(newName)
    print(f'Случайный списко из {listRange} людей: {nameList}')
randomNameList()

