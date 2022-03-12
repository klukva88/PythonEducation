#Множества

#Задача 1
sampleSet = {"Yellow", "Orange", "Black"}
sampleList = ["Blue", "Green", "Red"]

sampleSet.update(sampleList)
print(sampleSet)

#Задача 2

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(set1.intersection(set2))

#Задача 3

set1 = {10, 20, 30}
set2 = {20, 40, 50}
print(set1.difference(set2))

#Задача 4
newArray = sampleSet.union(set1)


newArray.add(11)
newArray.add('Vasya')

newArray.update(['hh', 'ff', 'dd'], {'zz', 'rr'})
print(newArray)

#Задача 5
'''
Создайте set и frozenset. Объедините оба множество в одно целое. 
Выполните операции:
к объединенному множеству добавьте элемент 2 и 5;
удалите число 2, а также первый элемент в множестве
'''
mySet = {x+2 for x in range (10)}
myFrozenSet = frozenset({y+3 for y in range(12, 30)})
unitedSet = mySet.union(myFrozenSet)
unitedSet.add(2)
unitedSet.add(5)
print(unitedSet)
unitedSet.remove(2)
unitedSet.pop()

print(unitedSet)

