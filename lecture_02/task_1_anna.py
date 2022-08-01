"""
Create a bank account program that will first let the user create a new account with a name that the user inputs.
Then let the user input initial balance (you can omit the currency for now). You should confirm that they input a valid
positive amount or default to 0. And then let the user either withdraw or deposit money (ask them if they would like to
withdraw or deposit and then ask them how much). Again confirm that the user inputs valid amounts. For the withdrawal
also confirm that they are not withdrawing more than what the balance is. And finally, return the final balance to
the user with the name of the account.
"""

name = input("Enter a name for your account: ")
balance = int(input("Enter account's balance: "))
confirmation = "Current balance of account '{}' is {}."

if balance >= 0:
    withdraw_or_deposit = input("Would you like to a) withdraw or b) deposit money? ")
    if withdraw_or_deposit == "a" or "b":
        if withdraw_or_deposit == "a":
            amount = int(input("Please enter amount you'd like to withdraw: "))
            if amount > balance:
                print("Insufficient funds on the account.")
            else:
                new_balance = balance - amount
                print("Operation completed.")
                print(confirmation.format(name,new_balance))
        else:
            amount = int(input("Please enter amount you'd like to deposit: "))
            new_balance = balance + amount
            print("Operation completed.")
            print(confirmation.format(name,new_balance))
    else:
        print("Incorrect input. You should enter 'a' or 'b'.")
else:
     print("Incorrect input. Amount has to be equal to or grater then 0.")



    
    
