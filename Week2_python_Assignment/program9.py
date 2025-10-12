class BankAccount:
    def __init__(self, account_holder, balance, account_type):
        self.account_holder = account_holder
        self.balance = balance
        self.account_type = account_type
        
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}, New Balance: {self.balance}")
        
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrew: {amount}, New Balance: {self.balance}")
            
    def display_balance(self):  
        print(f"Account Holder: {self.account_holder}, Balance: {self.balance}, Account Type: {self.account_type}")
        
if __name__ == "__main__":
    account1 = BankAccount("Alice", 1000, "Current")
    account1.display_balance()
    account1.deposit(500)
    account1.withdraw(200)
    
    account2 = BankAccount("Bob", 1500, "Savings")
    account2.display_balance()
    account2.deposit(300)
    account2.withdraw(1800)
    
    account3 = BankAccount("Charlie", 2000, "Savings")
    account3.display_balance()
    account3.deposit(700)
    account3.withdraw(1000) 
        
        
        
    

    