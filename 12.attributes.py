class Account:
    interest = 0.02
    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    def withdraw(self, amount):
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance -= amount
        return self.balance

kirk_account = Account('Kirk')
print(kirk_account.balance)
print(kirk_account.holder)
spock_account = Account('Spock')
spock_account.balance = 200
print([acc.balance for acc in [kirk_account, spock_account]])
spock_account = Account('spock')
print(spock_account.deposit(100))
print(spock_account.withdraw(90))
print(spock_account.withdraw(90))
print(getattr(spock_account, 'balance'))
print(hasattr(spock_account, 'deposit'))
print(spock_account.interest)
Account.interest = 0.04
print(spock_account.interest)
kirk_account.interest = 0.08
print(kirk_account.interest)
print(Account.interest)
Account.interest = 0.05
print(spock_account.interest, kirk_account.interest)
print(type(Account.deposit))
print(type(spock_account.deposit))
print(Account.deposit(spock_account, 20))
print(spock_account.deposit(30))