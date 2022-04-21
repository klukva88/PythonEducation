'''Задача1
Создать класс BankAccount с приватными параметрами у которых есть
Set и Get методы:
• Id - Строковый тип данных
• balance - Тип данных Int или Float
Создать экземпляр этого класса и задать для него данные через
конструктор.
Дополнительно реализовать следующие методы:
• Deposit - Через этот метод человек восполняет баланс и баланс
увеличивается.
После депозита средств на счет должно выводится следующее
сообщение:
«Вы пополнили счет 123231434000034 на сумму: 25000 сом
Баланс после пополнения счета: 60000 сом»
• Withdraw - Снятие денег, через этот метод происходит снятие денег и
после снятия происходит снижение текущего баланса, в случае если
денег на балансе нету то, выводится сообщение:
«У вас закончились деньги на балансе»
Иначе
«Вы сняли со счета 123231434000034: 15000 сом
Баланс после пополнения счета: 35000 сом
Текущий баланс:35000 сом»'''

class BankAccount:
    def __init__(self, id, balance=0):
        self.__id = str(id)
        self.__balance = float(balance)

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, balance):
        self.__balance = balance

    @property
    def id(self):
        return self.id

    @id.setter
    def id(self, id):
        self.__id = id


    def deposit(self, amount):
        self.__balance = self.__balance + amount
        print(f'Вы пополнили депозит {self.__id} на сумму: {amount} сом', end='\n' 
              f'Баланс после пополнения: {self.__balance}\n')


    def withdraw(self, amount):
        if self.__balance < amount:
            print(f'Недостаточно средств', end='\n'
                  f'Текущий баланс {self.__balance}\n')
        else:
            self.__balance = self.__balance - amount
            print(f'Вы вывели со счета {self.__id} сумму в {amount} сом', end='\n'
                  f'Текущий баланс: {self.__balance}')





user = BankAccount('123', 200 )


user.balance = 300
user.deposit(500)
user.withdraw(100)

