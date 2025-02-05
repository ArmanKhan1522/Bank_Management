from random import randint


class Bank:
    def __init__(self) -> None:
        self.account_no = randint(100000, 999999)
        self.name = input("Enter Name:")
        self.phone_no = int(input("Enter Phone Number:"))
        self.balance = 0

    def info(self):
        print(f"Account No : {self.account_no}")
        print(f"Name:{self.name}")
        print(f"Phone No : {self.phone_no}")
        print(f"Current Balance:{self.balance}")

    def deposite(self):
        amount = int(input("Enter the Amount to be Deposite:"))
        self.balance += amount
        print("Amount Deposite successfuly")

    def withdrawl(self):
        amount = int(input("Enter amount to be Withdrawal:"))
        if amount > self.balance:
            print("Insufficent Balance")
        else:
            self.balance -= amount
            print("Amount Withdrawal Successfully")


banks = []


def check_acc_exist(account_no):
    global banks
    for account in banks:
        if account.account_no == account_no:
            return account
    return False


while True:
    print("Enter 1 to Open Account")
    print("Enter 2 to display information")
    print("Enter 3 to deposit")
    print("Enter 4 for withdrawal ")
    print("Enter 5 for Transfer Money ")
    print("Enter 6 to exit")
    choice = int(input("Enter your Choice:"))
    if choice == 1:
        b = Bank()
        banks.append(b)
        print("Account Successfully Opened")
    elif choice == 2:
        if len(banks) == 0:
            print("No Account has been Created.")
        else:
            for accounts in banks:
                accounts.info()
    elif choice == 3:
        if len(banks) == 0:
            print("No Account has been created.")
        else:
            Account_no = int(input("Enter Account No:"))
            for accounts in banks:
                if accounts.account_no == Account_no:
                    accounts.deposite()
    elif choice == 4:
        if len(banks) == 0:
            print("No Account has been Created.")
        else:
            Account_no = int(input("Enter Account Number : "))
            for accounts in banks:
                if accounts.account_no == Account_no:
                    accounts.withdrawl()
    elif choice == 5:
        from_acc_no = int(
            input("Enter Account number to which you want to transfer money= ")
        )
        to_acc_no = int(
            input("Enter Account number to which you want to transfer money= ")
        )
        from_account = check_acc_exist(from_acc_no)
        to_account = check_acc_exist(to_acc_no)
        if from_account != None and to_account != None:
            transfer_amount = int(input("Enter amount:"))
            if from_account.balance < transfer_amount:
                print("Insufficient Balance")
            else:
                from_account.balance -= transfer_amount
                to_account.balance += transfer_amount
        else:
            print("Account does not exists")
    elif choice == 6:
        break
    else:
        print(f"Invalid Input {choice}")
