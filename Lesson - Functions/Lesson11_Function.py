print('Hello')
myList = list(range(1,10))
print(myList)
print(max(myList))

#Создание функции
def sayHello():
    for i in range(10):
        print('Hello')

def sayHello2(name):
    for i in range(5):
        print(f'Hello {name}')

def pythonLang(): print('I am learning python')

sayHello()
sayHello()
sayHello()

sayHello2('Tilek')
sayHello2('Nikolai')
sayHello2('Aselya')

pythonLang()

def helloGuest():
    print('Hello some guest!')

    def kitchen():
        print('You are in kitchen. Want some coffee?')

    def bathroom():
        print('You are in bathroom. Want to wash ur hand? ')

    #kitchen()
    bathroom()

helloGuest()

def sumNums():
    num1 = 25
    num2 = 50

    result = num1 + num2
    print(f'Sum: {result}')

def sumNumsParams(number1, number2):
    result = number1 + number2
    print(f'Sum: {result}')


sumNums()

numb1 = 50
numb2 = 55
sumNumsParams(numb1, numb2)
sumNumsParams(33, 50)
sumNumsParams(33,10)

def multipLy(a,b,c,d):
    result = a * b * c - d
    print(result)

multipLy(10,2,4,15)
multipLy(100,3,1,20)
multipLy(100,3,5,10)

def mathOperation(num1, num2 = 10):
    print(f'Result nums after addition: {num1 + num2 }')

def mathOperation2(num1=20, num2 = 10):
    print(f'Result nums after addition: {num1 + num2 }')

mathOperation(5,15)
mathOperation(5)

mathOperation2()

def dispkayUserInfo(name,age,addition):
    salary = 200 *  age + addition
    displayText = name + ' salary is: ' + str(salary)

    print(displayText)


dispkayUserInfo('Talant', 20, 5000)
dispkayUserInfo('Sergei', 30, 10000)
dispkayUserInfo(age = 28, name = 'Oleg', addition = 10000)

def findSum(*nums):
    sumNums = 0

    for i in nums:
        sumNums += i

    print(f'Sum of these numbers is: {sumNums}')


def findSum2(numMultiply, *nums):
    sumNums = 0
    for i in nums:
        sumNums += i #sumNums = sumNums + 4

    result = sumNums * numMultiply
    print(f'Result of these numbers is: {result}')

findSum(4,54,56,100)
findSum(4,54,56,100,56,43,1,23,34)
findSum(44,2)
findSum(4,54,56,100,56,43,1,23,34,12,32,43,54)

findSum2(10,4,54,56,100,56,43,1,23,34,12,32,43,54)
findSum2(20, 4,54,56,100,56,43,1,23,34)



def sumNumsParams2(number1, number2):
    result = number1 + number2
    return result

def sumNumsParams3(number1, number2):
    return number1 + number2

def sayHelloFr(n):
    resultText = f'Hello {n}'
    return resultText
    print('I am here!')


somenumber = 10
result2 = somenumber + sumNumsParams2(10,20) * 2
print(result2)

someResult = sumNumsParams2(50,100)
print(someResult)
print(sumNumsParams2(20,180))


print(sayHelloFr('Asyl'))

print(sumNumsParams3(20,180))


def checkAge(age):
    if age >=18:
        #resultText = 'You can vote'
        return 'You can vote'

    else:
        #resultText = 'You are too young!'
        return 'You are too young!'
age = 15

print(checkAge(29))
print(checkAge(19))
print(checkAge(15))
print(checkAge(14))

def printMyCollection(someCollection):
    for i in someCollection:
        print(i, end=' ')

    print('\n')

def printMyCollection2(someCollection):
    sumNums = sum(someCollection)
    result = sumNums + 100

    return result

myList2 = [23,433,55,6]
myList3 = [11,34,54,65,7,667,7]
myTuple = (34,54,65,7)

printMyCollection(myList2)
printMyCollection(myList3)
printMyCollection(myList)
printMyCollection(myTuple)

print(printMyCollection2(myList2))
print(printMyCollection2(myList3))





