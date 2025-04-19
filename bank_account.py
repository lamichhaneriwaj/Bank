
class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, initaialAmount, accName):
        self.balance = initaialAmount
        self.accName = accName
        print(f"\nAccount '{self.accName}' created.\nBalance = ${self.balance:.2f}")

    def getBalance(self):
        print(f"\nAccount '{self.accName}' balance = ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("\nDeposite Complete.✅")
        self.getBalance()

    def viableTransiction(self, amount):
        if (self.balance >= amount):
            return
        else:
            raise BalanceException(
               f"\nSorry, account'{self.accName}' has insufficient balance. Available balance is ${self.balance:.2f}"
            )
        
    def withdraw(self, amount):
        try:
            self.viableTransiction(amount)
            self.balance = self.balance - amount
            print("\nWithdraw Completed.✅")
            self.getBalance()
        except BalanceException as error:
            print(f'\nWithdraw interrupted: {error}')


    def transfer(self, amount, account):
        try:
            print("\n**********\n\nBegining Transfer.. 🚀")
            self.viableTransiction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("\nTransfer Complete! ✅\n\n**********")
        except BalanceException as error:
            print(f'\nTransfer Interrupted. ❌ {error}')


class InterestRewardAccount(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("\nDeposite Complete.")
        self.getBalance()


class SavingsAcct(InterestRewardAccount):
    def __init__(self, initaialAmount, accName):
        super().__init__(initaialAmount, accName)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.viableTransiction(amount + self.fee)
            self.balance -= (amount + self.fee)
            print("\nWithdraw Complete. ✅")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw Interrupted: {error}")