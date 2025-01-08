class Account:
    """
    Represents a bank account with basic attributes and methods for balance management.
    """

    def __init__(self, name, account_no, passcode, balance=0):
        """
        Initialize an account with a name, account number, passcode, and initial balance.
        """
        self.name = name
        self.account_no = account_no
        self.passcode = passcode
        self.__balance = balance  # Private attribute for balance

    def get_balance(self):
        """Returns the current balance."""
        return self.__balance

    def set_balance(self, amount):
        """
        Updates the balance. Ensures that the balance is non-negative.
        """
        if amount >= 0:
            self.__balance = amount
        else:
            raise ValueError("Balance cannot be negative.")

    def __str__(self):
        """Returns a string representation of the account."""
        return f"Name: {self.name}, Account No: {self.account_no}, Balance: {self.__balance}"
