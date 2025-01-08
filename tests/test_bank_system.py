import unittest
from bank.account import Account
from bank.bank_system import BankSystem

class TestBankSystem(unittest.TestCase):
    """
    Test suite for the BankSystem and Account classes.
    """

    def setUp(self):
        """Create a BankSystem instance and sample accounts for testing."""
        self.bank = BankSystem()
        self.bank.add_account("John Doe", "123", "pass", 100)

    def test_add_account(self):
        """Tests adding an account."""
        self.bank.add_account("Jane Doe", "124", "word", 200)
        self.assertIn("124", self.bank.accounts)

    def test_deposit(self):
        """Tests depositing money into an account."""
        self.bank.deposit("123", "pass", 50)
        account = self.bank.accounts["123"]
        self.assertEqual(account.get_balance(), 150)
