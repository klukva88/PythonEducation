'''Задача
1) Создать классы Vip_Account, PremiumAccount, кот-ые наследуются от класса BankAccount
2) Добавить к аккаунту Vip_Account - метод vipserving(): "Обслуживание в 1-ую очередь и отдельно"
3) Добавить к аккаунту Premium_Account - метод privalages(): "Скидка по карте 25%, резервирование
премиальных услуг скидка в 10%'''
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

class Vip_Account(BankAccount):
    def __init__(self, id, balance, isVip):
        super().__init__(id, balance)
        self.isVip = isVip

    def vipserving(self):
        if self.isVip==True:
            print('Обслуживание в первую очередь')

class Premium_account(Vip_Account):
    def __init__(self, id, balance, isVip, isPremium):
        Vip_Account.__init__(self, isVip)
        self.isPremium = isPremium

    def priveleges(self):
        if self.isPremium == True:
            print('Скидка по карте 25%, резервирование премиальных услуг скидка в 10%')
        elif self.isPremium == True and self.isVip == True:
            print('Вы VIP')



user = Vip_Account('12335', 10000, True)

user.vipserving(False)

user = Premium_account(True, True)
user.priveleges()
user.vipserving()
