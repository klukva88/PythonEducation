#Creation lambda
def helloSay():
    print('Hello there!')

def helloSayName(n):
    print(f'Hello {n}!')

def resultSum(n1, n2, n3):
    return n1 + n2 + n3


def mathResult(n1,n2,n3):
    return n1 + n2 * n3

def mathOperation(n1,n2,n3, operation1, operation2):
    sumResult = operation1(n1,n2,n3)
    additionResult = operation2(n1,n2)

    result = sumResult + additionResult


    return result

def main():
    sayHello = lambda: print('Hello there!')
    sayHello()
    helloSay()

    nameUser = input('Name: ')

    sayHelloName = lambda n: print(f'Hello {n}!')
    sayHelloName(nameUser)

    helloSayName(nameUser)

    mathResultLambda  = lambda n1, n2, n3: n1 + n2 * n3

    print(mathResultLambda(12,3,4))
    print(resultSum(12, 3, 4))

    number1 = int(input('Num1: '))
    number2 = int(input('Num2: '))
    number3 = int(input('Num3: '))

    addition = lambda n1, n2: n1+n2

    #sumResult = mathOperation(number1,number2,number3, sumResult)
    multipleResult = mathOperation(23,43,54, mathResultLambda, addition)
    #avgNums = mathOperation(23, 43, 54, lambda num1, num2, num3: (num1 + num2 + num3)/3)

    print(multipleResult)




if __name__ == '__main__':
    main()

