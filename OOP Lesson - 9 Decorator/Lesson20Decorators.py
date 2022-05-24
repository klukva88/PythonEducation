#Декораторы - обвертывание одной ф-ии другой функцией
#Используется специальный знак @имядекоратора

def my_simple_decorrator(function_to_decorate):
    def function_wrapper():
        print('Я тот код который внутри декоратора работает до вызова другой ф-ии')
        function_to_decorate()
        print('А я тот код который внутри декоратора работает ПОСЛЕ вызова другой ф-ии')

    return function_wrapper


def my_simple_decorrator2(function_to_decorate):
    def function_wrapper():
        print('*************************')
        function_to_decorate()
        print('*************************')

    return function_wrapper

def my_simple_decorrator3(function_to_decorate):
    def function_wrapper():
        print('$'*50)
        function_to_decorate()
        print('$'*50)

    return function_wrapper

@my_simple_decorrator2
@my_simple_decorrator3
@my_simple_decorrator
def my_simple_function_1():
    print('Мой первый текст, который хочу обернуть')

@my_simple_decorrator3
def my_simple_function_2():
    print('Мой Второй текст, который хочу обернуть')

###################################################
#Example2
def bread(function_to_wrap):
    def wrapper():
        print('~~~~~~~~~~~')
        function_to_wrap()
        print('~~~~~~~~~~~')

    return wrapper


def tomatos(function_to_wrap):
    def wrapper():
        print('~0~~0~~0~~0~')
        function_to_wrap()
        print('~0~~0~~0~~0~')
    return wrapper

def cucumber(function_to_wrap):
    def wrapper():
        print('<>$<>$<>$<>')
        function_to_wrap()
        print('<>$<>$<>$<>')
    return wrapper

def salads(function_to_wrap):
    def wrapper():
        print('~#~#~#~#~')
        function_to_wrap()
        print('~#~#~#~#~')
    return wrapper

@bread
@salads
@tomatos
def meat():
    print('===MEAT===')

@bread
@tomatos
@cucumber
def fish():
    print('===FISH===')

@bread
def chicken():
    print('==CHICKEN==')

"""
Декоратор с передачей аргумента 
"""
def decorator_with_functions(function_to_decor):
    # def wrapper(arg1, arg2, arg3='Португалия'):
    #     print(f'Добро пожаловать Гость!'
    #           f'\nПожалуйста представьтесь:')
    #     function_to_decor(arg1, arg2)
    #     print(f'Приятно познакомиться с вами мистер {arg1}!')

    def wrapper(*args, **kwargs):
        print(f'Добро пожаловать Гость!'
                  f'\nПожалуйста представьтесь:')
        function_to_decor(*args, **kwargs)

        fkClub = list(kwargs.values())
        print(f'Приятно познакомиться с вами мистер {args[1]} из {args[2]} '
              f'\n Мы поняли что вы выступаете за {fkClub[0]}!')

    return wrapper

# def decorator_soccerOffer(function_to_decor):
#     def wrapper(arg1, arg2):
#         print(f'{arg1}, вы бы не желали выступить за ФК Дордой?'
#               f'и как нам звать вас?')
#         function_to_decor(arg1, arg2)
#         print(f'мистер {arg2} ваш гонорар 200 млн сомов в год!')

    # return wrapper

@decorator_with_functions
# @decorator_soccerOffer
def show_fullName(firstName, second_name, country, fkClub):
    print(f'Меня зовут: {firstName} {second_name}')

def main():
    my_simple_function_1()
    print('====')
    my_simple_function_2()

    # callable_decorator = my_simple_decorrator(my_simple_function_1)
    # callable_decorator1_2 = my_simple_decorrator2(my_simple_function_1)
    # callable_decorator()
    # callable_decorator1_2()


    # callable_decorator2 = my_simple_decorrator(my_simple_function_2)
    # callable_decorator2()
    ############EXAMPLE##########
    meat()
    print('-'*100)
    fish()
    print('-' * 100)
    chicken()
    print('-' * 100)

    print('<b><i>dsfsd</i></b>')

    print('='*100)
    show_fullName('Криштиану', 'Роналду', 'Португлия', fkClub='MU')

if __name__ == '__main__':
    main()



