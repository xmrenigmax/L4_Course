class BankAccount:
    """Base class for bank accounts"""
    # Class variable to track total number of accounts
    total_accounts = 0
    
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.balance = initial_balance
        BankAccount.total_accounts += 1
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            return True
        return False
    
    def check_info(self):
        return f"Account: {self.account_number}, Balance: ${self.balance:.2f}"
    
    @classmethod
    def get_total_accounts(cls):
        return cls.total_accounts

class SavingAccount(BankAccount):
    """Savings account with interest rate"""
    def __init__(self, account_number, initial_balance=0, interest_rate=0.01):
        super().__init__(account_number, initial_balance)
        self.interest_rate = interest_rate
    
    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return interest
    
    def check_info(self):
        return f"{super().check_info()}, Interest Rate: {self.interest_rate*100}%"

class JointAccount(BankAccount):
    """Joint account for multiple holders"""
    def __init__(self, account_number, holders, initial_balance=0):
        super().__init__(account_number, initial_balance)
        self.holders = holders
    
    def check_info(self):
        holders_str = ", ".join(self.holders)
        return f"{super().check_info()}, Holders: {holders_str}"

# Example usage
if __name__ == "__main__":
    # Create accounts
    savings1 = SavingAccount("SA001", 1000)
    savings2 = SavingAccount("SA002", 2000)
    joint1 = JointAccount("JA001", ["John", "Jane"], 3000)
    
    # Test instance counting
    print(f"Total accounts created: {BankAccount.get_total_accounts()}")  # Should show 3
    
    # Test account operations
    print(savings1.check_info())
    savings1.deposit(500)
    print(f"After deposit: {savings1.check_info()}")
    
    print(joint1.check_info())
    joint1.withdraw(1000)
    print(f"After withdrawal: {joint1.check_info()}")