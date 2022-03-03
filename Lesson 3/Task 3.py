"""
Task 3
Вычислите среднее арифметическое значение в промежутке между числами 15 и 30 и
отобразите на экране.
"""

start = 15
finish = 29
avgNumb = 0
totalSum = 0
distance = 0

while start <= finish:
    totalSum = start + totalSum
    start += 1
    distance += 1


print(distance)
print(totalSum)
avgNumb = totalSum/distance
print(avgNumb)