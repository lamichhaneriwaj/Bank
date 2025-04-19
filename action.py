from bank_account import *

Riwaj = BankAccount(500, "Riwaj")
Elon = BankAccount(100, "Elon")

Riwaj.getBalance()
Elon.getBalance()

Elon.deposit(1500)

Riwaj.withdraw(1000)
Riwaj.withdraw(10)

Elon.transfer(800, Riwaj)

Bill = InterestRewardAccount(2000, "Bill")

Bill.getBalance() 

Bill.deposit(100)

Bill.transfer(100, Riwaj)


Zuckerberg = SavingsAcct(1000, 'Zuckerberg')

Zuckerberg.getBalance()

Zuckerberg.deposit(100)

Zuckerberg.transfer(10000, Riwaj)
Zuckerberg.transfer(1000, Riwaj)
