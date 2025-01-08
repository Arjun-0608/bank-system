from .account import Account

class BankSystem:
    """
    Handles bank operations such as adding accounts, deposits, withdrawals, and balance checks.
    """

    def __init__(self):
        """Initialize the BankSystem with an empty dictionary of accounts."""
        self.accounts = {}

    def add_account(self, name, account_no, passcode, initial_balance=0):
        """
        Adds a new account to the system. Checks for duplicate account numbers or names.
        """
        if account_no in self.accounts:
            print("Account with this account number already exists!")
        elif any(acc.name == name for acc in self.accounts.values()):
            print(f"User '{name}' already exists!")
        else:
            self.accounts[account_no] = Account(name, account_no, passcode, initial_balance)
            print("Account created successfully!")

    def deposit(self, account_no, passcode, amount):
        """
        Deposits money into the specified account after verifying the passcode.
        """
        account = self.accounts.get(account_no)
        if account and account.passcode == passcode:
            if amount > 0:
                account.set_balance(account.get_balance() + amount)
                print(f"Deposited {amount} successfully! New balance: {account.get_balance()}")
            else:
                print("Deposit amount must be positive.")
        else:
            print("Invalid account or passcode.")
