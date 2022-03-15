'''Задача 1
Необходимо объединить заданные словари в одну словарь'''
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict1.update(dict2)
print(dict1)

'''Задача 2
Выведите на экран значения ключа history:
'''
sampleDict = {
    "class":
        {
            "student":
                {
                    "name": "Mike",
                    "marks":
                        {
                            "physics": 70,
                            "history": 80
                        }
                }
        }
}
print(sampleDict["class"]["student"]["marks"]["history"])

'''Задача 3
Создать функцию проверки людей на допуск людей участвовать в 
голосовании в зависимости от возраста.
Вывод функции должен выглядеть следующим образом:
Вас зовут Denis, вам 32 года и вы можете голосовать
….
Вас зовут Timur, вам 17 лет и вы НЕ можете участвовать 
в голосовании, потому что вы слишком молоды!
'''
votersDict = {'Denis': 32, 'Sergei': 21, 'Elena': 18, 'Timur': 17,
              'Oleg': 27}
for key, value in votersDict.items():

    if value >= 18:
        print(f' Вас зовут {key}, Вам {value} года и вы можете участвовать в голосовании!')
    else:
        print(
            f' Вас зовут {key}, Вам {value} лет и вы  Не можете участвовать в голосовании, потому что вы слишком молоды!')

'''Задача 4
Есть следующий словарь жителей из разных городов:

Ваша задача попросить ввести имя человека и в зависимости от его 
имени удалить от этого словаря'''

studentList = {'Oleg': 'Moscow', 'Stepan': 'Novosibirsk', 'Olga':
    'Ekaterenburg', 'Murat': 'Bishkek', 'David': 'New Yourk'}

studentName = input('Введите имя студента: ')
errorMessage = 'Нет такого студента'
studentList.pop(studentName, errorMessage)
print(studentList)

