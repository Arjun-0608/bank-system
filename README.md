# Bank System 🏦

## Overview
Welcome to the **Bank System**, a Python-based application simulating essential banking operations! 
Manage your accounts securely and effortlessly. 💳💼

---

## Features ✨

### 1. Add New Accounts 🆕
- Create a new account with a **unique account number** and a **secure passcode**.
- Set an initial balance during account creation (optional).

### 2. Deposit Money 💰
- Deposit funds into your account securely.
- Validates that the deposit amount is **positive**.

### 3. Withdraw Money 🏧
- Withdraw funds if you have sufficient balance.
- Ensures that the withdrawal amount is **positive** and passcode-protected.

### 4. Check Balance 📊
- Instantly retrieve and display your account balance after **passcode verification**.

### 5. Display All Accounts 📜
- View details of all accounts for **administrative purposes**.

### 6. Test Coverage ✅
- Comprehensive unit tests ensure the **reliability** of all functionalities.

---

## How It Works 🔍

1. **Account Management:**
   - Add accounts with a name, account number, passcode, and optional initial balance.
   - Accounts are stored securely using Python classes.

2. **Transactions:**
   - Perform deposits and withdrawals with real-time balance updates.
   - Invalid transactions (e.g., negative amounts or insufficient funds) are **gracefully handled**.

3. **Security:**
   - Passcodes protect sensitive operations like deposits, withdrawals, and balance checks.

4. **Testing:**
   - All functionalities are rigorously tested using **unittest** to ensure error-free operation.

---

## Folder Structure 📂

```plaintext
bank-system/
│
├── bank/
│   ├── __init__.py  # Enables the folder to be treated as a package
│   ├── account.py   # Contains the Account class with attributes and methods for account operations
│   ├── bank_system.py  # Implements the BankSystem class to manage multiple accounts and their transactions
│   └── main.py  # Entry point of the application that interacts with users
│
├── tests/
│   └── test_bank_system.py  # Unit tests to ensure the functionality of the Bank System
│
├── requirements.txt  # Lists project dependencies
└── README.md  # Documentation for the project
```

---

## Getting Started 🚀

1. **Clone the Repository**
   ```bash
   git clone <repository_url>
   cd bank-system
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**
   ```bash
   python bank/main.py
   ```

4. **Run Tests**
   ```bash
   python -m unittest discover tests
   ```

---

## Technologies Used 🛠️

- **Python**: Core programming language.
- **unittest**: For testing all functionalities.

---

## Contributing 🤝
Feel free to fork the repository and contribute via pull requests! Suggestions and improvements are welcome. 🎉

---
