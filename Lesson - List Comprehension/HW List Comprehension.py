'''Задача 1
Необходимо сгенерировать список, кортеж из чисел, возведенных в
квадрат в промежутке между 1 и 10'''

myTuple = tuple([number * number for number in range(1, 10)])
print(myTuple)
print(type(myTuple))

'''Задача 2
Есть текст со словом “I love programming so much and I would like to
improve my skills”, вам необходимо из части этого текста 
сгенерировать список с буквами следующего вида:'''

theSentence = 'I love programming so much and I would like to improve my skills'
theSentence = [letter for letter in theSentence[0:18]]  # строка принимается как список
print(theSentence)

'''Задача 3
 Примите от пользователя любое слово и сгенерируйте новый 
список, состоящий только из согласных букв принятого от 
пользователя слова.'''

myWord = input('Введите слово: ')
myWord = [letter for letter in myWord if letter not in 'aeyiou']
print(myWord)

''' Задача 4
Есть два списка [2,3,4,5] и [20,41,28,56]. Вам необходимо проверить 
на делимость элементов второго списка на элементы первого списка.'''

list1 = [2, 3, 4, 5]
list2 = [20, 41, 28, 56]
result = [True if number2 % number1 == 0 else False for number1, number2 in zip(list1, list2)]
print(result)
