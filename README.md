# Jerome Magic Banking

A simple command line banking simulation written in Python. It lets a user sign up for a new account or sign in to an existing one, then perform basic banking operations like transferring money to another Jerome account, transferring to another bank, or buying airtime.

## Features

- Sign up for a new account with a full name, phone number, and a 4 digit pin
- Automatically generated 10 digit account numbers that are guaranteed unique
- Sign in with your name, account number, and pin
- Transfer money to another Jerome account
- Transfer money to an account at another bank
- Buy airtime for any phone number
- Balance checks before every transaction, so you can never send more than you have
- Pin confirmation before every transaction, so a wrong pin will not move any money
- Option to cancel a transaction at the confirmation step
- Log out option to end your session cleanly

## Files

| File | Purpose |
|---|---|
| `bank.py` | The entry point. Runs the sign up / sign in menu and starts a session. |
| `bank_functions.py` | All the actual banking logic: sign up, sign in, transfers, and airtime. |

## How to run

Make sure both files are in the same folder, then run:

```
python3 bank.py
```

You will be asked to sign up or sign in. If you sign up, save the account number you are given, since you will need it to sign in.

To try the demo account that already exists in `bank_accounts`, sign in with:

```
Name: Ose
Account number: 8130076487
Pin: 3423
```

## How it works

`bank_accounts` is a dictionary that stores every account, keyed by name. Each account is a list in the form:

```
[account_number, pin, balance]
```

When you sign in, `trial()` checks your name, account number, and pin against the dictionary. If they match, you land on a menu where you can choose to transfer money, buy airtime, or log out. Every transaction function takes the current balance and pin, checks that you have enough money and that your pin is correct, and only then updates and returns the new balance.

## Known limitations

This is a learning project, not a real banking system, so a few things are simplified on purpose:

- All data lives in memory and is lost when the program closes. There is no file or database storage.
- There is no encryption. Pins and balances are stored as plain numbers.
- Inputs are assumed to be well formed. Entering letters where a number is expected (like the pin or amount) will crash the program.
- Only one bank session runs at a time. There is no support for multiple accounts being active at once.

## Possible improvements

- Save `bank_accounts` to a file (or a real database) so accounts persist between runs
- Add input validation with `try/except` around number inputs
- Add a transaction history log for each account
- Add an option to check balance without making a transaction
