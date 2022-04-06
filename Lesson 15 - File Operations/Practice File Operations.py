'''Задача 1
Аскарбек Алмазбекович, [05.04.2022 20:53]
1. Примите от пользователя название файла

2. Создать файл с указанным названием от пользователя  и записать туда

Принятую от пользователя: информацию.
Имя
Возраст
Адрес
Зарплату

Аскарбек Алмазбекович, [05.04.2022 20:53]
3. Прочесть данный файл
'''

fileName = input('Введите имя файла:')
with open(fileName, 'w') as userFile:
    userName = input('Введите Имя: ')
    userAge = input('Введите Возраст: ')
    userAddress = input('Введите адрес: ')
    userSalary = input('Введите зарплату: ')
    userFile.write(f'{userName} - {userAge} лет, проживает по адресу {userAddress} и получает {userSalary}')

with open(fileName, 'r') as theFile:
    print(theFile.read())

'''Задача 2
Запишите данный текст в файл как «lorem.txt» и прочитайте данный 
текст:
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem 
Ipsum has been the industry's standard dummy text ever since the 1500s, when an 
unknown printer took a galley of type and scrambled it to make a type specimen 
book. It has survived not only five centuries, but also the leap into electronic 
typesetting, remaining essentially unchanged. It was popularised in the 1960s with 
the release of Letraset sheets containing Lorem Ipsum passages, and more recently 
with desktop publishing software like Aldus PageMaker including versions of Lorem 
Ipsum.
• Строка за строкой 
• Текст целиком
• Текст в виде списка'''

with open('lorem.txt', 'w') as loremFile:
    loremFile.write('''
    Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem 
Ipsum has been the industry's standard dummy text ever since the 1500s, when an 
unknown printer took a galley of type and scrambled it to make a type specimen 
book. It has survived not only five centuries, but also the leap into electronic 
typesetting, remaining essentially unchanged. It was popularised in the 1960s with 
the release of Letraset sheets containing Lorem Ipsum passages, and more recently 
with desktop publishing software like Aldus PageMaker including versions of Lorem 
Ipsum.''')
with open('lorem.txt', 'r') as newFile:
    counter = 1
    for line in newFile:
        print(f' Строка {counter} : {newFile.readline()}',end='')
        counter +=1

with open('lorem.txt', 'r') as wholeText:
    wholeText = wholeText.read()
    print(wholeText)

with open('lorem.txt', 'r') as listLine:
    listLines = [line for line in listLine]
    print(listLines)

'''Задача 3
Прочтите текст из задания 1 в обратном порядке'''

with open('lorem.txt', 'r') as reverseText:
    reverseText = reverseText.read()
    print(reverseText[::-1])

'''Здадча 4
Создайте программу, в котором будет записывать введенный 
пользователем массив строк (Линию строк) и считывать его обратно 
из файла на консоль.'''



textlines = []
userInput = input('Введите строку:')
while userInput != 'exit':
    textlines.append(userInput)
    userInput = input('Введите строку: ')
with open('textLines.txt', 'w') as userText:
    userText.writelines(textlines)
with open('textLines.txt', 'r') as text:

    print(text.readline())

