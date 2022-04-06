#import random
#from random import random, randint
from random import *
from copy import deepcopy
#random
num = random()  #0.1 - 1.0
#num = random() * 100 #0 - 100
print(num)

num2 = randint(20,50)
result = num2 + 10

print(num2)
print(result)

#randrange(start, stop, step)  - 1 number
num3 = randrange(0,120,5)
print(num3)

listNum = list(range(20,70,3))
print(listNum)

print(choice(listNum))

listWorkers = ['Asely','Nikolai', 'Sergei', 'Askar', 'Adilet']
workerChoice = choice(listWorkers)
print(workerChoice)

#shuffle
listWorkers = ['Asely','Nikolai', 'Sergei', 'Askar', 'Adilet']
listWorkers.sort()
print(listWorkers)
shuffledListWorker = deepcopy(listWorkers)
shuffle(shuffledListWorker)

#shuffledListWorker = shuffle(listWorkers)
print(shuffledListWorker)
#
# listNums = [23,43,2,4]
# listNums2 = listNums
# listNums3 = deepcopy(listNums)
#
# #listNums2[1] = 11
# listNums3[1] = 11
#
# print(listNums2)
# print(listNums)
# print(listNums3)

from math import *

print(pi)
num1 = 5
print(num1**2) #25
print(pow(5,2)) #25.0

#sqrt- Нахождения корня числа
num2 = 144
print(sqrt(num2)) #12.0

#log(x,y), log2, log10
print(log2(96))
print(log10(100))
print(log(100,20))

number1 = 23.65 #24
print(ceil(number1)) #Округление до ближ наибольшего числа
print(floor(number1)) #Округление до ближ наименьшего числа

print(round(number1)) #24

#5! = 1*2*3*4*5 - 120
print(factorial(5))

print(cos(radians(60))) #1/2
print(sin(radians(360)))


from MyProgram import someProgram as sp, RepeatingProgram as rp


print(sp.addNums(23,34,54,1,34))
sp.sayHello('Askar')

rp.showWorkers()

print(fmod(5,2))












