'''Задача 2
Создать лямбда выражение, которая возводит в квадрат переданное ей число'''

myNumber = int(input('Введите число: '))
square = lambda num1: num1 * num1

print(square(myNumber))

'''Задача 3
 Создать лямбду выражения, которая возвращает среднее значение среди 4 
переданных чисел
'''

average = lambda num1, num2, num3, num4: (num1+num2+num3+num4)/4

print(average(2,7,8,12))

'''Задача 4
 Примите от пользователя сумму для оплаты какого-нибудь товара. 
В зависимости от того сколько платит покупатель, необходимо будет провести 
расчеты через If Else конструкцию.
Необходимо произвести необходимые скидки по следующим критериям:
• Если сумма платы производится в промежутках от 1000 сом и до 1999 
сом - выполнить скидку в 2%
• Если сумма платы производится в промежутках от 2000 сом и до 4999 
сом - выполнить скидку в 5%
• Если сумма платы производится в промежутках от 5000 сом и до 9999 
сом - выполнить скидку в 10%
• Если сумма платы производится в промежутках от 10 000 сом и выше -
выполнить скидку в 20%
Пример вывода результата программы:'''

discount = lambda price, percantage: price * percantage

spendMoney = int(input('Введите сумму: '))
if 1000 <= spendMoney < 2000:
    print(f'Сумма скидки 2% от {spendMoney} -  {discount(spendMoney, 0.02)} ')
elif 2000 <= spendMoney < 5000:
    print(f'Сумма скидки 5% от {spendMoney} -  {discount(spendMoney, 0.05)} ')
elif 5000 <= spendMoney < 10000:
    print(f'Сумма скидки 10% от {spendMoney} -  {discount(spendMoney, 0.1)} ')
else:
    print(f'Сумма скидки 20% от {spendMoney} -  {discount(spendMoney, 0.2)} ')
