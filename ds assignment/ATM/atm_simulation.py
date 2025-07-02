class ATM:
    def __init__(self, pin, balance=0):
        self.correct_pin = pin
        self.balance = balance
        self.authenticated = False

    def authenticate(self):
        attempts = 0
        while attempts < 3:
            user_pin = input("Enter your 4-digit PIN: ")
            if user_pin == self.correct_pin:
                print("✅ Authentication successful!\n")
                self.authenticated = True
                return True
            else:
                attempts += 1
                print("❌ Incorrect PIN. Try again.\n")
        print("🚫 Too many failed attempts. Account locked.")
        return False

    def check_balance(self):
        print(f"💰 Your current balance is: ${self.balance:.2f}\n")

    def deposit(self):
        try:
            amount = float(input("Enter amount to deposit: $"))
            if amount <= 0:
                print("❗ Invalid amount.\n")
            else:
                self.balance += amount
                print(f"✅ Successfully deposited ${amount:.2f}")
                self.check_balance()
        except ValueError:
            print("❗ Please enter a valid number.\n")

    def withdraw(self):
        try:
            amount = float(input("Enter amount to withdraw: $"))
            if amount <= 0:
                print("❗ Invalid amount.\n")
            elif amount > self.balance:
                print("❌ Insufficient funds.\n")
            else:
                self.balance -= amount
                print(f"✅ Successfully withdrew ${amount:.2f}")
                self.check_balance()
        except ValueError:
            print("❗ Please enter a valid number.\n")

    def run(self):
        if not self.authenticate():
            return
        while True:
            print("===== ATM MENU =====")
            print("1. Check Balance 💰")
            print("2. Deposit Money 🏦")
            print("3. Withdraw Money 💸")
            print("4. Exit 🚪")
            choice = input("Choose an option (1-4): ")
            print()
            if choice == '1':
                self.check_balance()
            elif choice == '2':
                self.deposit()
            elif choice == '3':
                self.withdraw()
            elif choice == '4':
                print("👋 Thank you for using the ATM. Goodbye!")
                break
            else:
                print("❗ Invalid selection. Please try again.\n")


# Run the ATM simulation
if __name__ == "__main__":
    atm = ATM(pin="1234", balance=500.0)
    atm.run()
