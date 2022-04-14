'''Задача 1
Напишите программу на Python для чтения последних n строк
файла. Количество последних строк принять от пользователя.'''
lastLines = int(input('Веедите количество послдених строк для отображения: '))
with open('lesson15files_task1.txt', 'r') as taskOneText:
    linesArray = taskOneText.readlines()
    for line in linesArray[-lastLines:]:
        print(f'Строка {linesArray.index(line) + 1} - {line}')

'''Задача 2
Напишите программу на Python для подсчета количества строк в 
текстовом файле.'''

with open('lesson15files_task1.txt', 'r') as taskTwoText:
    linesArray = taskTwoText.readlines()
    print(f' Количество строк в файле:{len(linesArray)}')

'''Задача 3
Напишите программу на Python для чтения случайной строки из 
файла.'''
from random import choice
with open('lesson15files_task1.txt', 'r') as taskThreeText:
    linesArray = taskThreeText.readlines()
    print(f' Случайная строка из файла {choice(linesArray)}')

'''Задача 4
Примите от пользователя список из 10 работников. Запишите 
данный список в отдельный файл как workers.txt. Имена каждого из 
сотрудников должно быть в отдельной строке.'''

workerlist = [input('Имя работника:') + '\n' for worker in range(1)]
print(workerlist)
with open('workers.txt', 'w', encoding='utf-8') as workersFile:
    workersFile.writelines(workerlist)

'''Задача 5
Документ «article.txt» содержит текст:
Требуется реализовать функцию longest_words(file), которая 
выводит слово, имеющее максимальную длину (или список слов, 
если таковых несколько).'''

def longestLines(file):
    with open(file, 'r', encoding='utf-8') as articleFile:
        articleLines = articleFile.readlines()
        print(sorted(articleLines, key=lambda item: len(item))[-1])

longestLines('article.txt')

