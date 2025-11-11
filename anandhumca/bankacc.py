class BankAccount:
    def __init__(self,acc_no,name,acc_type,initial_balance=0):
        self.name=name
        self.acc_no=acc_no
        self.acc_type=acc_type
        self.balance=initial_balance
    def deposit(self,amount):
        self.balance+=amount
        print(f"Name:{self.name}\nAccount Number:{self.acc_no}\nAccount Type:{self.acc_type}")
        print(f"Deposited amount is:{amount}")
        print(f"Balance amount is:{self.balance}")
    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance-=amount
            print(f"\nName:{self.name}\nAccount Number:{self.acc_no}\nAccount Type:{self.acc_type}")
            print(f"withdrawn amount is:{amount}")
            print(f"Balance amount is:{self.balance}")
        else:
            print("Insufficient Balance")
name=input("Enter the name:")
acc_no=input("Enter the account number:")
acc_type=input("Enter the account type:")
acc=BankAccount(acc_no,name,acc_type,initial_balance=0)
while True:
    print("\n1.Deposit\n2.Withdraw\n3.Exit")
    option=int(input("Enter an option:"))
    if option==1:
        amt=int(input("Enter an amount:"))
        acc.deposit(amt)
    elif option==2:
        amt=int(input("Enter an amount:"))
        acc.withdraw(amt)
    elif option==3:
        break
    else:
        print("Invalid option")
    
        
        
