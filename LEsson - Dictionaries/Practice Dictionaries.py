'''1. Создайте программу, в которой пользователь будет указывать размер словаря,
после чего устанавливать ключи и значения с клавиатуры, например:'''

#Вариант 1
mydict = {}
dictUpdate = {}
dictSize = int(input('Введите размер словаря: '))
while dictSize > 0:
    dictUpdate = {
        input('Введите Ключ: '):
        input('Введите Значение Ключа: ')
    }
    mydict.update(dictUpdate)
    dictSize -=1

for key, value in mydict.items():
    print(f' Ключ: {key} \n Значение: {value} ')
print(mydict)

#Вариант 2

mydict = {}
dictSize = int(input('Введите размер словаря: '))
while dictSize > 0:
    key = input('Введите Ключ: ')
    mydict[key] = input('Введите значение: ')
    dictSize -= 1
for key, value in mydict.items():
    print(f' Ключ: {key} \n Значение: {value} ')


'''Задача 2
Создайте словарь из чисел. Выполните над ним операции:
• удалите элемент по его ключу;
• удалите какой-либо элемент по его ключу с 
использованием del;
• удалите все элементы словаря;
• удалите сам словарь.'''

numberDict = {1: 'Один', 2: 'Два', 3: 'Три'}
numberDict.pop(2) #Удаление по ключу
del numberDict[1] #Удаление по ключу с помощью del
numberDict.clear() #очищение словаря
numberDict = None #Удаление словаря - не уверен что сделал правильно


'''Задача 3
Создайте два цикла:
• В первом цикле for выведите только все значения этого словаря;
• Во втором цикле выведите значения и ключи словаря
'''
theDict = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
for value in theDict.values():
    print(f'значение: {value}' , end='\n')
for key, value in theDict.items():
    print(f'Ключ: {key} => Значение: {value}', end='\n')

'''Задача 4
При помощи цикла for сгенерируйте словарь из квадратов чисел от 1 
до 7
'''
squareDict = {}
for number in range(1, 10):
    squareDict[number] = number*number

print(squareDict)

'''Задача 4
Выполните операции:
Cделайте копию словаря
удалите оригинал,
из копии удалите ключ
«Три» вместе с его значением, добавьте новый элемент в конец 
словаря: "Новое" -> "Kotli'''

d = {"Один" : "Питон", "Два" : "C++", "Три" : "Java", "Четыре" : "C#"}
dCopy = d.copy()
d.clear()
dCopy.pop("Три")
dCopy['Новое'] = 'Kotlin'
print(dCopy)


