import typing

# Mono_account = SavingsAccount(250, 674534, 13)
# print(Mono_account)
# Mono1_account = SavingsAccount(1200.35, 342134, 13)
# print(Mono1_account)

# Privat_account = CurrentAccount(-100, 34213435422, 1000)
# print(Privat_account)
# Swed_account = CurrentAccount(34.78, 11112222, 10.10)
# print(Swed_account)

# mybank = Bank([Mono_account, Privat_account, Alisa_account])
# mybank.update(interest=15)
# print(Mono_account)

# mybank.open_acc(567432)
# print(f"Openning Account with acc number 567432 : {mybank.accounts}")
# mybank.close_acc(674534)
# print(
#     f"Closing  Mono_account saving account with acc number 674534 : {mybank.accounts}")

class Account:
    def __init__(self, balance, account_number):
        self._balance = balance
        self._account_number = account_number

    @classmethod
    def create_account(cls, account_number):
        return cls(0.0, account_number)

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            raise ValueError('Amount must be positive')

    def withdraw(self, amount):
        if amount > 0:
            self._balance -= amount
        else:
            raise ValueError('Amount must be positive')

    def get_balance(self):
        return self._balance

    def get_account_number(self):
        return self._account_number

    def __str__(self):
        return f'Account number: {self._account_number}, balance: {self._balance}'


class SavingsAccount(Account):

    def __init__(self, balance: float, account_number: int, interest: int):
        super().__init__(balance, account_number)
        self.interest = interest

    def interest_add(self):
        self._balance += self._balance * self.interest
        

    def __str__(self):
        return f'Account number: {self._account_number}, balance: {self._balance}, interest:{self.interest}'


class CurrentAccount(Account):

    def __init__(self, balance: float, account_number: int, overdraft_limit: int):
        super().__init__(balance, account_number)
        self.overdraft_limit = overdraft_limit

    def __str__(self):
        return f'Account number: {self._account_number}, balance: {self._balance}, overdraft limit:{self.overdraft_limit}'


class Bank:
    def __init__(self, accounts: typing.List[Account]):
        self.accounts = accounts

    def update(self):
        for account in self.accounts:
            if isinstance(account, SavingsAccount):
                account.interest_add()
            elif isinstance(account, CurrentAccount):

                if account._balance < account.overdraft_limit:
                    print(
                        f'Message for account {account._account_number}: You are in overdraft!')

    def dividend_pay(self, dividend):
        for account in self.accounts:
            account._balance += dividend

    def open_acc(self, balance, account_number):
        new_acc = Account.create_account(account_number)
        new_acc._balance = balance
        self.accounts.append(new_acc)

    def close_acc(self, account_number):
        for account in self.accounts:
            if account_number == account._account_number:
                self.accounts.remove(account)
    
    def __str__(self):
        for account in self.accounts:
            return f'acc_number: {account._account_number}, bаlance: {account._balance}, interest: {account.interest}'

    # def __repr__(self):
    #     for account in self.accounts:
    #         return f'acc_number: {account._account_number}, bаlance: {account._balance} and interest: {account.interest}'



# 1. Write a test for the Bank class that we wrote in 14 lesson. You should write a test for the open_account method. Ensure that the account is opened and has  balance.
# 2. Test update method. It should check that code added interest and sended a message(print function was called).

# 1. Напишите тест для класса Банк, который мы написали в 14 уроке. Вы должны написать тест для метода open_account. Убедитесь, что счет открыт и на нем есть баланс.
# 2. Тестовый метод обновления. Он должен проверить, что код добавил интерес и отправил сообщение(была вызвана функция печати).

Mono_account = SavingsAccount(250, 674534, 1)
print(Mono_account)
mybank = Bank([Mono_account])
print(mybank)
mybank.update()
print(mybank)

