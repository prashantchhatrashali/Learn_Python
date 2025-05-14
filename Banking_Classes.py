class BankAccount:
    """A simple bank account class to test class basics."""

    def __init__(self, owner_name, initial_balance=0):
        """Initialize the bank account with owner name and balance."""
        self.owner = owner_name
        self.balance = initial_balance
        self.transaction_history = []

    def deposit(self, amount):
        """Add money to the account balance."""
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposit: +INR{amount}")
            return f"Deposited INR{amount}. New balance: INR{self.balance}"
        else:
            return "Deposit amount must be positive."

    def withdraw(self, amount):
        """Remove money from the account balance if sufficient funds exist."""
        if amount <= 0:
            return "Withdrawal amount must be positive."
        elif amount > self.balance:
            return f"Insufficient funds. Your balance is ${self.balance}"
        else:
            self.balance -= amount
            self.transaction_history.append(f"Withdrawal: -${amount}")
            return f"Withdrew ${amount}. New balance: ${self.balance}"

    def get_balance(self):
        """Return the current balance."""
        return f"Current balance: ${self.balance}"

    def show_transactions(self):
        """Display all transactions."""
        if not self.transaction_history:
            return "No transactions yet."

        result = f"Transaction history for {self.owner}:"
        for transaction in self.transaction_history:
            result += f"\n- {transaction}"
        return result


# Test your understanding by using the class
def main():
    # Create a bank account
    my_account = BankAccount("Prashant Chhatrashali", 100)

    # Test the methods
    print(f"Account created for {my_account.owner}")
    print(my_account.get_balance())

    print(my_account.deposit(50))
    print(my_account.withdraw(30))
    print(my_account.withdraw(200))  # Should fail - insufficient funds
    print(my_account.deposit(-10))  # Should fail - negative amount

    print(my_account.show_transactions())


if __name__ == "__main__":
    main()

if __name__="__main__":
    main()