firstNumber = int(input('Введите первое число: '))
secondNumber = int(input('Введите второе число: '))
operationType = int(input('"Введите номер операции: 1.Сложение 2.Вычитание 3.Умножение" : '))

if operationType == 1 :
    print(firstNumber + secondNumber)
elif operationType == 2:
    print(firstNumber - secondNumber)
elif operationType == 3:
    print(firstNumber * secondNumber)
else:
    print('Такой операции не существует')