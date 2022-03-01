name = input('Имя: ')
age = input('Возраст: ')
gender = input('Пол: ')
company = input('Компания: ')
family = input('Семейное положение: ')
address = input('Адрес проживания: ')

print('Длина имени - ' + str(len(name)) + ' символа')
if (company.find('a')) > 0 : # проверка на букву а в названии компании
    print ('Есть буква а')
else:
    print('Нет буквы а')
print('Второй индекс в адресе проживания: ' + address[2])
print('Имя со второй буквы: ' + name[1:])
print('Имя компании наоборот: ' + company[::-1])
