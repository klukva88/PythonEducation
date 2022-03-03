# Задача 1

userName = input('введите имя: ')
for i in range(0, 20):
    print(userName)

# Задача 2 используя while

initial = 1
while (initial <= 25):
    print(initial * 5)
    initial = initial + 3

# Задача 2 используя for

for initial in range (1, 26, 3):
    print(initial * 5)

# Задача 3

userInput = 1
while userInput !=0:
    userInput = int(input('Введите число: '))
    print('Результат вычислений = ', userInput+10)
print('Выход из вычисления!')