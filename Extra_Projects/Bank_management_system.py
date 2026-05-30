from abc import ABC,abstractmethod
class Account(ABC):
    bank_name = "State Bank of India"
    account_number=100001

    def __init__(self,balance,account_holder):
        self.__balance=balance
        self.__account_number=Account.account_number
        self.__account_holder=account_holder
        print(f"Account created! Your Account Number is {self.__account_number}")
        Account.account_number+=1
    
    @abstractmethod
    def withdraw(self,amount):
        pass

    def deposit(self, amount):
        print(f"₹{amount} deposited.")
        self.__balance+=amount
        print(f"Current Balance: ₹{self.show_balance()}")

    def show_balance(self):
        return self.__balance
    
    def withdraw_balance(self,amount):
        self.__balance-=amount
        print(f"Current Balance: ₹{self.show_balance()}")

    def show_details(self):
        print(f"Bank Name: {Account.bank_name}")
        print(f"Account Holder Name: {self.__account_holder}")
        print(f"Account Number: {self.__account_number}")
        print(f"Account Type: {type(self).__name__}")
        print(f"Current Balance: ₹{self.show_balance()}")

    def get_account_number(self):
        return self.__account_number

class SavingsAccount(Account):
    min_balance=1000
    def withdraw(self, amount):
        if(self.show_balance()-amount)>=1000:
            print(f"₹{amount} withdrawn.")
            self.withdraw_balance(amount)
        else:
            print("Minimum balance must be maintained")
    
class CurrentAccount(Account):
    def withdraw(self, amount):
        if(self.show_balance()-amount)>=0:
            print(f"₹{amount} withdrawn.")
            self.withdraw_balance(amount)
        else:
            print("Minimum balance must be maintained")

def find_account(acc_no):
    for acc in Accounts:
        if acc.get_account_number() == acc_no:
            return acc
    return None
        
Accounts=[]
while True:

    print("\n===== BANK MANAGEMENT SYSTEM =====")
    print("1. Create Savings Account")
    print("2. Create Current Account")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. Show Account Details")
    print("6. Show Account Balance")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name=input("Enter Account Holder Name:  ")
        balance=float(input("Enter Balance:  "))
        acc=SavingsAccount(balance,name)
        Accounts.append(acc)
        
    elif choice == 2:
        name=input("Enter Account Holder Name:  ")
        balance=float(input("Enter Balance:  "))
        acc=CurrentAccount(balance,name)
        Accounts.append(acc)

    elif choice == 3:
        acc_no=int(input("Enter Account Number:  "))
        amount=float(input("Enter Deposit Amount:  "))
        if amount <= 0:
            print("Invalid amount")
            continue
        acc = find_account(acc_no)
        if acc:
            acc.deposit(amount)
        else:
            print("Account not found")        
        

    elif choice == 4:
        acc_no=int(input("Enter Account Number:  "))
        amount=float(input("Enter Withdrawal Amount:  "))
        if amount <= 0:
            print("Invalid amount")
            continue
        acc = find_account(acc_no)
        if acc:
            acc.withdraw(amount)
        else:
            print("Account not found")        

    elif choice == 5:
        acc_no=int(input("Enter Account Number:  "))
        acc = find_account(acc_no)
        if acc:
            acc.show_details()
        else:
            print("Account not found")     

    elif choice == 6:
        acc_no=int(input("Enter Account Number:  "))
        acc = find_account(acc_no)
        if acc:
            print(f"Current Balance: ₹{acc.show_balance()}")
        else:
            print("Account not found")     
        

    elif choice == 7:
        print("Thank you for using our banking system.")
        break

    else:
        print("Invalid Choice")

