import bank_functions as Bank

bank_accounts = {
    "Ose": ["8130076487", 2680, 200000000]
}

while True:
    option = Bank.home2()
    if option == "1":
        values = Bank.sign_up()
        name, pin = values[0], values[2]
        account_number = Bank.generate_account_number(bank_accounts)
        bank_accounts.update({f"{name}": [account_number, pin, 0]})
        print(f"Your account number is {account_number}, please save it.")
        print(bank_accounts)
        Bank.trial(name, account_number, bank_accounts, pin)
        break

    elif option == "2":
        details = Bank.sign_in1()
        name, account_number, pin = details[0], details[1], details[2]
        Bank.trial(name, account_number, bank_accounts, pin)
        break
