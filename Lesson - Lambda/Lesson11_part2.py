def sumNums(*nums):
    sumNums = 0
    for i in nums:
        sumNums += i

    return sumNums

def workerInfo(name, *, age, salary, numchild):
    print(f'Name of this person is: {name}')
    print(f'Age is {age}')
    print(f'Salary is {salary}')
    print(f'numChild is {numchild}')

def workerInfo2(name, address, /, age, salary, numchild):
    print(f'Name of this person is: {name}')
    print(f'Address of this person is: {address}')
    print(f'Age is {age}')
    print(f'Salary is {salary}')
    print(f'numChild is {numchild}')

#*args, **kwargs

def namesOfWorkers(*args):
    for name in args:
        print(name,end=',')


def infoWorker(**kwargs):
    print('\n')
    for k,v in kwargs.items():
        print(f'{k}:{v}')

def bothArgs(*args, **kwargs):
    print(args)
    print(kwargs)

    for i in args:
        print(i)

    for k,v in kwargs.items():
        print(k,v)


def main():
    print(sumNums(12,23,43,54))
    print(sumNums(12,23,43))
    print(sumNums(12,23,43,12,43,54,23))

    workerInfo2('Tilek', 'Lev tolstoy123',salary = 25000, numchild = 3, age = 25)

    tupleOfWorkers = (
        'Robert De Niro',
        'Juliana Moor',
        'Brad Pitt',
        'Leo Di Caprio'
    )

    robertDeniro = None,
    JulianaMoor = None,
    Brad_Pitt = None,
    leoDi = None


    dictofWorkers = {
        robertDeniro: 'Famouse actor',
        JulianaMoor: 'Wooman actor',
        Brad_Pitt:'Ex hasband Anj Jolie',
        leoDi: 'from Titanic'

    }

    namesOfWorkers(tupleOfWorkers)
    infoWorker(robertDeniro = 'Famouse actor', JulianaMoor = 'Wooman actor',
               Brad_Pitt = 'Ex hasband Anj Jolie', leoDi = 'from Titanic')

    bothArgs('Forest','Ocean', 'Sky', 'Mountain', predator = 'wolf', fish = 'Dolphin', bird = 'Eagle')




if __name__ == '__main__':
    main()

