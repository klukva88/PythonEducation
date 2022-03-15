#Создание словаря

listMy = list()
listMy = []


myDict = {}
print(myDict)
print(type(myDict))

myDict2 = dict()
print(myDict2)
print(type(myDict2))

#Создание словарей с заданными значениями

myContacts = {'Mama': '+996 509 314355', 'Otec': '+996 555 123456', 'Tilek': '+112321132323423', 'Jena': '+996 700 342354'}
print(myContacts)

myNumber = [234,54,566,7]
print(myNumber[2]) #566
myNumber[2] = 45
print(myNumber[2]) #45


print(myContacts['Otec'])
print(myContacts['Tilek'])

myContacts['Otec'] = '+71231243424'
myContacts['Tilek'] = '+996 500 123 435'

print(myContacts['Otec'])
print(myContacts['Tilek'])

numbersEnglish = {'One': 1, 'Two':2, 'Three': 3, 4: 'Four', 'isNumber': False}


print(numbersEnglish)
print(numbersEnglish[4])
print(numbersEnglish['isNumber'])

#Конвертация со списка в словарь
populationCountriesList = [
    ['China', 1.5],
    ['India', 1.4],
    ['USA', 0.2],
    ['Indonesia', 0.3],
    ['Kyrgyzstan',0.006],
    ['USA', 0.45]
]

populationDict = dict(populationCountriesList)

print(populationCountriesList)
print(populationDict)

#numbersEnglish = {'One': 1, 'Two':2, 'Three': 3, 4: 'Four', 'isNumber': False, 'SomNumber':1}
#print(numbersEnglish)

#Конвертация с кортежей в словарь

htmlColorCodesTuple = (
    ('Green', '#03fc5e'),
    ('Red', '#fc0317'),
    ('Blue', '#030ffc'),
    ('Black', '#000000'),
    ('Whiter', '#ffffff')
)

colorsDict = dict(htmlColorCodesTuple)

print(htmlColorCodesTuple)
print(colorsDict)

fatherContact = myContacts['Otec']
print(fatherContact)

#print(myContacts['David']) #KeyError: 'David'

#Функции словаря in, not in

print('David' in myContacts)

if 'David' not in myContacts:
    print('Нет такого контакта')
else:
    print('Да, такой контакт есть')

dftMessage = 'Unknown number'
nameSearch = 'Otec'
nameSearch2 = 'David'

print(myContacts[nameSearch])
print(myContacts.get(nameSearch))
print(myContacts.get(nameSearch, dftMessage))
print(myContacts.get(nameSearch2, dftMessage))
#print(myContacts[nameSearch2])

#Удаление элементов с пом-ью del и pop

myContacts = {'Mama': '+996 509 314355', 'Otec': '+996 555 123456', 'Tilek': '+112321132323423', 'Jena': '+996 700 342354'}
print(myContacts['Tilek'])

del myContacts['Tilek']
#print(myContacts['Tilek'])

myContacts.pop('Mama')
print(myContacts)

myContacts = {'Mama': '+996 509 314355', 'Otec': '+996 555 123456', 'Tilek': '+112321132323423', 'Jena': '+996 700 342354'}

myContacts.pop('Tilek')
print(myContacts)

messageDel = 'This contact cannot be found'
myContacts.pop('Tilek', messageDel)
print(myContacts)

myContacts['Otec'] = None
print(myContacts)

#Очищение словаря с пом-ью del clear
myContacts.clear()
print(myContacts)


myContacts = {'Mama': '+996 509 314355', 'Otec': '+996 555 123456', 'Tilek': '+112321132323423', 'Jena': '+996 700 342354'}
print(myContacts)

#del myContacts
#print(myContacts)


myContacts2 = {'Aselya': '+996 5555 1234 354', 'Sergei': '+996 501 435435', 'Samat': '+77232132134'}

#Добавление новых элементов в Словарь
myContacts.update(myContacts2)
print(myContacts)

myContacts.update({'Oleg': '+7777324234234', 'Sergei2':'+77771232134'})
print(myContacts)

myContacts['Timur'] = '+991 32423423423'
myContacts['Alison'] = '+112321342423'

print(myContacts)
print(type(myContacts['Oleg']))

name = 'Askar'
print(name)

# Операция перебора значений и ключей внутри Словарь
#Записать все ключи в опр коллекцию
myContactsName = myContacts.keys()

myContactsName2 = list(myContacts.keys())
print(myContactsName2)
print(myContactsName2[1])

#Записать все значения в опр. коллекцию
myContactsNumber = myContacts.values()
print(myContactsNumber)

myContactsNumberTuple = tuple(myContacts.values())
print(type(myContactsNumberTuple))
print(myContactsNumberTuple)

#Записать все ключи и значния в опр. коллекцию
myCollectionNumber = myContacts.items()
print(myCollectionNumber)

myCollectionNumberList = list(myContacts.items())
print(myCollectionNumberList)
myFirstContactList= list(myCollectionNumberList[0])
print(myFirstContactList)

print(myContacts)
#Перебору данных с пом-ью

# Отображение лишь значений
for number in myContacts.values():
    print(number, end=", ")

print('\n')
# Отображение лишь ключи
for nameContact in myContacts.keys():
    print(nameContact, end=",")

print('\n')

#myContacts = {'Mama': '+996 509 314355', 'Otec': '+996 555 123456', 'Tilek': '+112321132323423', 'Jena': '+996 700 342354'}
# Отображение лишь ключи и значения
for contactName, numb in myContacts.items():
    print(f'Имя контакта: {contactName} - Номер телефона: {numb}')

    #if numb == '+112321342423':
       # print(contactName)

print(len(myContacts))

listNumber = [
    [123,43],
    [324,54,5465]
]

companyWorker = {
    'worker 1':
        {
            'name': 'Asylzhan Tilekov',
            'age': 32,
            'address': 'Lev Tolstoy 7',
            'salary': 25000
        },

    'worker 2':
        {
            'name': 'Aselya Timofeeva',
            'age': 23,
            'address': 'Mira 10',
            'salary': 28000
        },

    'worker 3':
        {
            'name': 'Murat Ormonov',
            'age': 41,
            'address': 'Belinka 77',
            'salary': 45000
        }
}

print(companyWorker['worker 2']['address'])
print(companyWorker['worker 1']['salary'])

companyWorker.update({'worker 4': {
            'name': 'Olga Stepanova',
            'age': 34,
            'address': 'Sorokina 123',
            'salary': 54000
        }})

print(companyWorker)

# companyWorker['worker 5'] = {}
# print(companyWorker)

companyWorker['worker 5'] = {'name': 'Samat Abdrakhmanov', 'age': 35}
print(companyWorker)

companyWorker['worker 5']['address'] = 'Toktogula 55'
print(companyWorker)


# Перебор значений сложных словарей -  nested dictionary
counter = 1
for worker, workerDict in companyWorker.items():
    print(f'Работник {counter}: {worker}')
    for workerInfo, workerData  in workerDict.items():
        print(f'Тип Инфо:{workerInfo}: {workerData}')
    print('===============')
    counter += 1

