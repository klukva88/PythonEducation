myNumbers = list(range(10, 20))
print(myNumbers)

myNumbers2 = list()
for i in myNumbers:
    myNumbers2.append(i * 2)

print(myNumbers2)

myNumbers3 = [i * 2 for i in myNumbers]
print(myNumbers3)

word = 'Hello'

repeating = [word * 3 for i in range(3)]
print(repeating)

"""
myNumbers2 = [i * 2 for i in myNumbers]

listSome = [word * 3  for i in range(10)]
"""

letters = 'aeiuoy'

sometext = 'I am doing well in Bishkek'

newListWord = [i for i in sometext if i.lower() in letters]
# for i in sometext:
#     if i.lower() in letters:
#         newListWord.append(i)

print(newListWord)

listNumbers = [12, 43, 54, 11, 17, 15, 25, 28, 12, 11, 17, 28, 54]

listNotEvenNums = [num if num % 2 != 0 else 'четное число' for num in listNumbers]

listNotEvenNums2 = []

for i in listNumbers:
    if i % 2 != 0:
        listNotEvenNums2.append(i)
    else:
        listNotEvenNums2.append('Четное число')

print(listNotEvenNums)
print(listNotEvenNums2)

tuple = (i for i in range(10))
print(type(tuple))

mySet = {i + 10 for i in listNumbers}
print(mySet)
print(type(mySet))

dictNumbersPowers = {numb1: numb1 * 2 for numb1 in range(10, 30, 2)}
dictNumbersPowers2 = {numb1 * 2: numb1 ** 3 for numb1 in range(10, 30, 2)}
print(dictNumbersPowers)
print(dictNumbersPowers2)

print(type(dictNumbersPowers))

# zip метод и генераторы списка

myList = [12, 3, 10]
myList2 = [2, 3, 5]

num1, num2, num3 = myList
print(num1)
print(num2)
print(num3)

resultList = []

for num1, num2 in zip(myList, myList2):
    resultList.append(num1 * num2)
print(resultList)

resultList2 = [num1 * num2 for num1, num2 in zip(myList, myList2)]
print(resultList2)
