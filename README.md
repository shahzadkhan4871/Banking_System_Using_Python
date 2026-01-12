🏦 Dynamic Banking System (Python)
📌 Overview

This project is a menu-driven banking system built using Python.
It allows users to dynamically enter values at runtime and perform basic banking operations through a terminal-based interface.

✨ Features

Dynamic account creation using user input

Deposit money

Withdraw money

Check account balance

Menu-driven system

Input validation for transactions

📂 Project Structure
dynamic-banking-system/
│
├── banking_system.py
└── README.md

🛠 Technologies Used

Python 3

Object-Oriented Programming (OOP)

🚀 How to Run the Program
Prerequisites

Python 3.x installed on your system

Steps

Download or clone the project.

Open a terminal in the project directory.

Run the program using:

python banking_system.py

🧑‍💻 How the System Works

User enters:

Account number

Account holder name

Initial balance

A menu is displayed with the following options:

Deposit money

Withdraw money

Check balance

Exit

The program runs continuously until the user chooses to exit.

📘 Sample Menu
----- MENU -----
1. Deposit
2. Withdraw
3. Check Balance
4. Exit

🧱 Code Overview
BankAccount Class

deposit(amount) – Adds money to the account

withdraw(amount) – Withdraws money if balance is sufficient

check_balance() – Displays current balance

⚠️ Limitations

Supports only one account at a time

No data persistence (data resets after program exits)

No authentication or PIN system

🚧 Future Enhancements

Support multiple bank accounts

Add PIN/password authentication

Store data in files or a database

Improve error handling

Add GUI or web interface

📄 License

This project is free to use for learning and educational purposes.
