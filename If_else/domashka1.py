# Задача 1

checkNumber = int(input('Введите число: '))
if checkNumber <9 and checkNumber >2:
    print('число больше двух, но меньше 9')
else:
    print('неизвестное число')

print('число больше двух, но меньше 9' if checkNumber <9 and checkNumber >2 else 'неизвестное число' )

'''
Задача 2
Стоимость доставки) Транспортная компания использует
следующий тариф для расчета стоимости (в долларах) доставки на
основе веса посылки (в килограммах).
• Если вес находится в промежутке между
0 и 2 кг - то расчет за кг идет по тарифу 3.5$ за кг.
• Если вес находится в промежутке между
3 и 5 кг - то расчет за кг идет по тарифу 5.5$ за кг.
• Если вес находится в промежутке между
6 и 10 кг - то расчет за кг идет по тарифу 7$ за кг.
• Если вес до 50кг расчет за кг идет по тарифу 10$ за кг.
'''

parcelWeight = int(input('Введите вес посылки : '))

if parcelWeight <= 2 and parcelWeight > 0:
    print('Тариф $3.5 за кг')
elif parcelWeight <= 5 and parcelWeight > 2:
    print('Тариф $5.5 за кг')
elif parcelWeight <= 10 and parcelWeight > 5:
    print('Тариф $7 за кг')
elif parcelWeight <= 50 and parcelWeight > 10:
    print('Тариф $10 за кг')
else: print('Посылка не может быть принята')

'''
Задача 3
Примите число от пользователя и проверьте является ли данное число
нечетным числом. Если оно нечетное, то необходимо вывести
сообщение, что оно нечетное иначе попросить пользователя
перезапустить программу заново
'''
checkNumber = int(input('Введите число: '))


if checkNumber % 2 > 0 :
    print('«Это число нечетное!»')

else:
    print('«перезапустите программу»')