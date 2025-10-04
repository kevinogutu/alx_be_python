# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0.0):
        """Initialize the account with an optional starting balance."""
        self.__account_balance = float(initial_balance)  # encapsulated attribute

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.__account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw money if sufficient funds are available."""
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False

        if self.__account_balance >= amount:
            self.__account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """Display the current balance."""
        print(f"Current Balance: ${self.__account_balance:.2f}")
