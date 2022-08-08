"""
Create a bank account program that will first let the user create a new account with a name that the user inputs.
Then let the user input initial balance (you can omit the currency for now). You should confirm that they input a valid
positive amount or default to 0. And then let the user either withdraw or deposit money (ask them if they would like to
withdraw or deposit and then ask them how much). Again confirm that the user inputs valid amounts. For the withdrawal
also confirm that they are not withdrawing more than what the balance is. And finally, return the final balance to
the user with the name of the account.
"""

name = input("Enter a name for your account: ")

# you should use `float` for storing amount of money
balance = float(input("Enter account's balance: "))

if balance >= 0:
    withdraw_or_deposit = input("Would you like to a) withdraw or b) deposit money? ")

    # this doesn't do what you probably expected
    # this actaully does following (withdraw_or_deposit == "a") OR ("b") which is always evaluated as True
    # a more advanced way would be to use the `in` operator, then the condition would look like this:
    # if withdraw_or_deposit in {"a", "b"}:
    # with the condition like this, when I run the app and insert `c` it asks me about depositing money
    if withdraw_or_deposit in {"a", "b"}:
        if withdraw_or_deposit == "a":
            amount = float(input("Please enter amount you'd like to withdraw: "))
            if amount > balance:
                print("Insufficient funds on the account.")
            else:
                new_balance = balance - amount
                print("Operation completed.")
                # I guess you used `format` to reused the confirmation message
                # these days, f-strings are preferred as they are easier to read
                print(f"Current balance of account {name} is '{new_balance}'.")
        else:
            amount = float(input("Please enter amount you'd like to deposit: "))
            new_balance = balance + amount
            print("Operation completed.")
            print(f"Current balance of account {name} is '{new_balance}'.")
    else:
        print("Incorrect input. You should enter 'a' or 'b'.")
else:
     print("Incorrect input. Amount has to be equal to or grater then 0.")



    
    
