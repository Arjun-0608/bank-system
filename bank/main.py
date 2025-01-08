from bank_system import BankSystem

def main():
    """
    Provides a menu-driven interface for interacting with the BankSystem.
    """
    bank = BankSystem()

    while True:
        print("\n1. Add Account\n2. Deposit\n3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            account_no = input("Enter account number: ")
            passcode = input("Set passcode: ")
            bank.add_account(name, account_no, passcode)
        elif choice == "2":
            account_no = input("Enter account number: ")
            passcode = input("Enter passcode: ")
            amount = float(input("Enter amount to deposit: "))
            bank.deposit(account_no, passcode, amount)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
