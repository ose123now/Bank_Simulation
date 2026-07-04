import random


def home2():
    print(
        """Welcome to Jerome Magic Banking.
To sign up choose 1, to sign in choose 2.
Please contact 08130078635 for help.""")
    option = input("> ")
    return option


def sign_up():
    print("To sign up please enter your details correctly.")
    name = input("Enter your full name (first_name middle_name last_name): ")
    phone_number = input("Enter your Phone Number: ")

    while True:
        pin_input = input("Choose a 4 digit pin: ")
        pin2_input = input("Confirm the pin: ")
        if pin_input != pin2_input:
            print("Pins do not match. Please try again.")
            continue
        if not (pin_input.isdigit() and len(pin_input) == 4):
            print("Your pin must be exactly 4 digits. Please try again.")
            continue
        pin = int(pin_input)
        break

    print("You have successfully signed up for a Jerome Bank Account, please use your details to sign in.")
    values = [name, phone_number, pin]
    return values


def generate_account_number(bank_accounts):
    while True:
        account_number = str(random.randint(1000000000, 9999999999))
        if not any(account_number == value_list[0] for value_list in bank_accounts.values()):
            return account_number


def sign_in1():
    print("To sign in please enter your account name and number correctly.")
    account_name = input("Enter the name on your account: ")
    account_number = input("Enter your account number: ").strip()
    pin = int(input("Enter your pin: "))
    values = [account_name, account_number, pin]
    return values


def trial(name, account_number, bank_accounts, pin):
    for key, value_list in bank_accounts.items():
        if name == key and account_number == value_list[0] and pin == value_list[1]:
            break
    else:
        print("Wrong details. Please check your name, account number and pin.")
        return

    while True:
        option = home1()
        balance = bank_accounts[name][2]

        if option == "1":
            bank_accounts[name][2] = jerome_account(balance, pin)
        elif option == "2":
            bank_accounts[name][2] = other_account(balance, pin)
        elif option == "3":
            bank_accounts[name][2] = airtime(balance, pin)
        elif option == "4":
            print("Thank you for banking with Jerome Microfinance Bank. Goodbye!")
            break
        else:
            print("Please choose a valid option.")


def home1():
    option = input(
        """Welcome to Jerome Microfinance Bank
Enter 1 to send money to a Jerome account
Enter 2 to send money to other banks
Enter 3 to buy airtime.
Enter 4 to log out.
> """)
    return option


def jerome_account(balance, pin):
    amount = float(input("Enter the amount: "))
    if amount <= 0:
        print("Please enter an amount greater than zero.")
        return balance
    if amount > balance:
        print("You have insufficient balance to perform this transaction.")
        return balance

    recipient_account = input("Enter recipient's account number: ")
    entered_pin = int(input(
        f"""Transferring {round(amount, 2)} Naira to {recipient_account},
please enter your pin to confirm the transfer
Choose 0 to go back.
> """))

    if entered_pin == 0:
        print("Transaction cancelled.")
        return balance
    if entered_pin != pin:
        print("Incorrect pin. Transaction failed.")
        return balance

    balance -= amount
    print(f"Successfully transferred {round(amount, 2)} Naira to {recipient_account}.")
    return balance


def other_account(balance, pin):
    amount = float(input("Enter the amount: "))
    if amount <= 0:
        print("Please enter an amount greater than zero.")
        return balance
    if amount > balance:
        print("You have insufficient balance to perform this transaction.")
        return balance

    while True:
        recipient_account = input("Enter recipient's account number: ").strip()
        if len(recipient_account) == 10:
            break
        print("Please enter a correct account number of 10 digits.")

    recipient_bank = input("Enter recipient's bank: ")
    entered_pin = int(input(
        f"""Transferring {round(amount, 2)} Naira to {recipient_account} ({recipient_bank}),
please enter your pin to confirm the transfer
Choose 0 to go back.
> """))

    if entered_pin == 0:
        print("Transaction cancelled.")
        return balance
    if entered_pin != pin:
        print("Incorrect pin. Transaction failed.")
        return balance

    balance -= amount
    print(f"Successfully transferred {round(amount, 2)} Naira to {recipient_account}.")
    return balance


def airtime(balance, pin):
    number = input("Enter the phone number you are buying airtime for.\n> ")
    amount = float(input("Enter the airtime amount.\n> "))

    if amount > balance:
        print("Your balance is insufficient to purchase this amount of airtime. Please fund your account.")
        return balance

    entered_pin = int(input(
        f"""Enter your pin to buy {round(amount, 2)} naira airtime for {number}
Else press 0 to go back.
> """))

    if entered_pin == 0:
        print("Transaction cancelled.")
        return balance
    if entered_pin != pin:
        print("Incorrect pin. Transaction failed.")
        return balance

    balance -= amount
    print(f"You have successfully bought {round(amount, 2)} naira airtime for {number}.")
    return balance
