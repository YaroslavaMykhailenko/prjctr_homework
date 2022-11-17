import unittest
from unittest.mock import patch, Mock
import typing


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
        self._balance += self._balance * (self.interest)/ 100

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
                    print('You are in overdraft!')

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


# 2. Test update method. It should check that code added interest and sended a message(print function was called).
# 2. Протестируйте метод обновления. Он должен проверить, что код добавил интерес и отправил сообщение(была вызвана функция печати).

class TestBank(unittest.TestCase):
    def test_bank_account_creation(self):

        account_num = 345423  
        add_balance = 100  

        bank = Bank(accounts=[])
        
        assert len(bank.accounts) == 0

        bank.open_acc(add_balance, account_num)

        assert len(bank.accounts) == 1   
        self.assertEqual(bank.accounts[0]._balance, add_balance)


    
    def test_bank_update_interest(self):

        interest = 2  # interest equals 2 percent       

        # prepare
        Mono_account = SavingsAccount(balance=250, account_number=674534, interest=interest)
        bank = Bank(accounts=[Mono_account])

        # current balance on saving account withount adding interest
        assert bank.accounts[0]._balance == 250
        # act 
        bank.update()

        # check for updates
        assert bank.accounts[0]._balance == 255

    @patch('builtins.print')
    def test_bank_send_message_overdraft(self, mock_print):

        # prepare
        My_account = CurrentAccount(balance=200, account_number=674534, overdraft_limit=280)
        bank = Bank(accounts=[My_account])
        # act
        bank.update()

        # check if print is called
        mock_print.assert_called_with('You are in overdraft!')


    @patch('builtins.print')
    def test_bank_no_sent_message(self, mock_print):

        # prepare
        My_account = CurrentAccount(balance=2000, account_number=674534, overdraft_limit=1000)
        bank = Bank(accounts=[My_account])
        # act
        bank.update()

        # check if print is not called

        mock_print.assert_not_called()



    


if __name__ == '__main__':
    unittest.main()
