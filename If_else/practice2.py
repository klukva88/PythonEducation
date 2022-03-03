operationType = int(input('"Введите номер операции: 1.Сложение 2.Вычитание 3.Умножение" : '))

if operationType == 1 :
    print('Сложение')
elif operationType == 2:
    print('Вычитание')
elif operationType == 3:
    print('Умножение')
else:
    print('Такой операции не существует')