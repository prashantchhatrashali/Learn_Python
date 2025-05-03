#Assignment: Simple ATM Simulator
#Write a Python program that:
#- Asks the user to enter their PIN (assume a fixed correct PIN, e.g., "1234").
#- Allows the user to check their balance, deposit money, or withdraw money.
#- Ensures the user cannot withdraw more than the available balance.
#- Runs in a loop until the user chooses to exit.

import time

balance = 100
pin = 1234
attempts = 3  # Allow PIN retry attempts

# PIN authentication loop
while attempts > 0:
    input_pin = input("Please enter the PIN number: ")

    if input_pin.isdigit() and int(input_pin) == pin:
        break  # PIN is correct, proceed to transactions
    else:
        attempts -= 1
        print(f"Incorrect PIN! Attempts left: {attempts}")

if attempts == 0:
    print("Too many incorrect attempts. Exiting...")
    exit()

# Transaction menu loop
while True:
    try:
        choice = int(input("Please enter your choice:\n 1 - Balance Enquiry\n 2 - Deposit Money \n 3 - Withdraw \n 4 - Exit\n"))

        if choice == 1:
            print(f"Your account balance is INR: {balance}")
        elif choice == 2:
            deposit_amt = int(input("Enter amount to deposit: "))
            print("Depositing, please wait...")
            time.sleep(2)
            balance += deposit_amt
            print(f"Updated balance: INR {balance}")
        elif choice == 3:
            amt_withdraw = int(input("Enter amount to withdraw: "))
            if amt_withdraw <= balance:
                print("Processing withdrawal, please collect cash.")
                time.sleep(2)
                balance -= amt_withdraw
                print(f"Remaining balance: INR {balance}")
            else:
                print("Insufficient Balance!")
        elif choice == 4:
            print("Thank you for choosing Apex Bank.")
            break
        else:
            print("Invalid choice! Please enter a valid option.")
    except ValueError:
        print("Invalid input! Please enter a number.")
