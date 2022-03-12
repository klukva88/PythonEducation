# Задача №1
# Создайте список чисел в промежутке между 15-100 с шагом 5
numberList = list(range(15,101,5))
print(numberList)

#Задача 2
'''
Пробежитесь по списку, которая была создано в задании 1 с помощью while, for.
Отобразите их в одном ряду
'''
for number in numberList:
    print(number, end=' ')
print('\n')

counter = 0
while counter < len(numberList):
    print(f'{numberList[counter]}',  end=' ')
    counter += 1
print('\n')
# Задача 3
'''
Создайте список городов ['Moscow’, 'Bishkek’, 'NY, 'Tashkent’, 'Almaty’,
'Talas’, 'NY’, 'Moscow’]
'''
cityList = ['Moscow', 'Bishkek', 'NY', 'Tashkent', 'Almaty',
'Talas', 'NY', 'Moscow']

for city in cityList:
    while cityList.count(city) > 1:
       cityList.remove(city)
print(cityList, '\n')

'''
Задача 4
Найдите среднеарифметическое значение внутри данного списка
[34, 31, 5, 53,1,34, 5] не используя функцию sum(). Найдите сумму используя
цикл'''

numbers = [34, 31, 5, 53, 1, 34, 5]
counter = 0
summ = 0
while counter < len(numbers):
    summ = summ + numbers[counter]
    counter += 1
else:
    print(f' Среднее = {summ/counter}')

print(f' Проверка = {sum(numbers)/len(numbers)} ') #Проверка через методы sum и len

'''
Задача 5
Есть список рабочих ['Елена', 'Степан', 'Мурат', 'Асан', 'Айсулуу'], где каждый
сотрудник получает одинаковые заработные платы в 50 тыс. рублей, кроме
Степана. Заработная плата у Степана составляет 70 тыс. рублей.
Как мы можем отобразить на консоли так, чтобы заработная плата Степана
отображалась как 70 тыс. рублей, а у остальных 50 тыс. рублей?'''

employeeList = ['Елена', 'Степан', 'Мурат', 'Асан', 'Айсулуу']

for employee in employeeList:
    if employee != 'Степан':
        print(f'{employee} получает - 50000р')
    else:
        print(f'{employee} получает - 70000р')

'''
Задача 6
Создайте программу, которая удаляет имена рабочих до тех пор, пока
пользователь не пожелает остановиться. До тех пор, пока пользователь не
напишет ‘нет’ с данного списка рабочих ['Елена', 'Степан', 'Мурат', 'Асан',
'Айсулуу'] должны удаляться имена.'''

print(employeeList)
while len(employeeList) != 0:
    who = input('Кого хотите удалить?:').capitalize()
    if who not in employeeList:
        print('Такого рабочего нет!')
        continue
    employeeList.remove(who)
    print(f'Теперь список такой: {employeeList}')
    wannaContinue = input('Хотите продолжить?: ').capitalize()
    if wannaContinue == 'Нет':
        print('Вы вышли из программы')
        break
print('Все рабочие закончились!')

