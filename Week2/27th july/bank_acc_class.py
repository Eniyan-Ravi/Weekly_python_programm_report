class BankAccount:
    def __init__(self,name,acc_no,balance):
        self.name=name
        self.acc_no=acc_no
        self.balance=balance

    def deposite(self,amount):
        self.balance+=amount
        print("Amount deposited=",amount)

    def withdraw(self,amount):
        if amount<self.balance:
            self.balance-=amount
            print("Amount Withdrawn:",amount)
        else:
            print("Amount attempted to withdraw:",amount," is higer than the balance")
            print("Insufficient Balance")

    def display_bal(self):
        print("Account ID:",self.acc_no)
        print("Account Balance=",self.balance)
        print("")

a = BankAccount("Eniyan",101,10000)
a.display_bal()
a.deposite(5000)
a.display_bal()
a.withdraw(2005)
a.display_bal()
a.withdraw(20000)

