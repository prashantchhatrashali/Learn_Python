#Assignment: Simple ATM Simulator
#Write a Python program that:
#- Asks the user to enter their PIN (assume a fixed correct PIN, e.g., "1234").
#- Allows the user to check their balance, deposit money, or withdraw money.
#- Ensures the user cannot withdraw more than the available balance.
#- Runs in a loop until the user chooses to exit.

import time

from python_basic_1 import attempts

balance=100
pin=1234
attempt=0
input_pin = int(input("Please enter the PIN number: "))
#PIN Handling
for attempt in range(3):
    attempt+=1
    if input_pin==pin:
        break
    else:
        print("Wrong PIN in Three Attempts.")

while True:
        if pin == input_pin:
            choice=int(input("Please enter your choice. \n 1 - Balance Enquiry\n 2 - Deposite Money \n 3 - Withdraw \n 4 - Exit \n"))
            if choice == 1:
                print(f"Your account balance is INR: {balance}")
            elif choice == 2:
                deposit_amt=int(input("Please enter the amount you wish to deposit: \n"))
                print("Depositing amount, please wait.")
                time.sleep(5)
                balance=balance+deposit_amt
                print(f"Your updated balance is: {balance}")
            elif choice == 3:
                amt_withdraw=int(input("Please enter the amount you wish to withdraw: "))
                if amt_withdraw <= balance:
                    print("Your Transaction is being processed! Please collect your Cash. ")
                    time.sleep(2)
                    balance=balance-amt_withdraw
                    print(f"Your account balance after the Withdrawal is : {balance}")
                else:
                    print("Sorry! Insufficient Balance!")
            elif choice == 4:
                print("Thank you for choosing Apex Bank.")
                break
        else:
            print("You've entered the wrong PIN. \nPlease try again.")