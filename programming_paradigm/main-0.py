# main-0.py
import sys
from bank_account import BankAccount

def main():
    # Create a bank account with a default starting balance
    account = BankAccount(100)

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    # Split command and optional amount (e.g., "deposit:50")
    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    # Perform operation based on command
    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount:.2f}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount:.2f}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command or missing amount.")

if __name__ == "__main__":
    main()
