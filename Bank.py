class BankAccount:
    def __init__(self, account_number, owner_name, balance=0):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"✅ Deposited {amount}")
        else:
            print("❌ Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("❌ Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("❌ Insufficient balance.")
        else:
            self.balance -= amount
            print(f"✅ Withdrew {amount}")

    def check_balance(self):
        print(f"💰 Current balance: {self.balance}")


# --- Main Program ---
print("Welcome to Simple Banking System")

acc_no = input("Enter account number: ")
name = input("Enter account holder name: ")
balance = float(input("Enter initial balance: "))

account = BankAccount(acc_no, name, balance)

while True:
    print("\n----- MENU -----")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        amount = float(input("Enter deposit amount: "))
        account.deposit(amount)

    elif choice == "2":
        amount = float(input("Enter withdrawal amount: "))
        account.withdraw(amount)

    elif choice == "3":
        account.check_balance()

    elif choice == "4":
        print("Thank you for using the banking system 👋")
        break

    else:
        print("❌ Invalid choice. Please try again.")
