import json
import os

FILE_NAME = "accounts.json"
global accounts

if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        accounts = json.load(f)
else:
    accounts = {
        "0000": [5100,123456,"Frisk", 8],
        "1111": [5300,246810,"Chara", 11],
        "2222": [5500,122555,"Kris", 15],
        "3333": [6767,123456,"Formie", 13]
    }
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(accounts, f, indent=4)

choice = 0
balance = 0
logged_in = False
globalUser = ''
globalAge = 0

print("Welcome to Grilby's ATM!")
print("How may I help you? - Grilby's")

def caseSwitch():
    if choice == 1:
        registration_page()
    elif choice == 2:
        login_page()
    elif choice == 3:
        print(accounts)
        welcome_page()
    else:
        print("\nIndex out of range!\n")
        welcome_page()

def welcome_page():
    global choice
    print("\nOptions")
    print("\n1. Register")
    print("2. Login")
    print("3. Exit")
    while True:
        try:
            choice = int(input("Enter index: "))
            caseSwitch()
            break
        except ValueError:
            print("\nPlease input an integer only!\n")

def login_page():
    global logged_in, globalUser, globalAge, balance
    print("\nLogin Page")
    userInput = input("Enter your username or bank ID: ")
    passInput = int(input("Enter your password: "))
    for user, data in accounts.items():
        if (userInput == data[2] or userInput == str(user)) and passInput == data[1]:
            print(f"\nLogged in as {data[2]}\n")
            logged_in = True
            globalUser = data[2]
            globalAge = data[3]
            balance = data[0]
            profile()
            return
    print("\nIncorrect input! Either the account doesn't exist or the credentials are wrong.\n")
    welcome_page()

def profile():
    print(f"Welcome {globalUser}!\n")
    print(f"Total Balance: ₱{balance}")
    print(f"Age: {globalAge}")
    print("Options")
    print("1. Pay")
    print("2. Change details")
    print("3. Delete account...")
    while True:
        try: 
            userInput = int(input("Enter index: "))
            break
        except ValueError:
            print("\nPlease input an integer only!\n")
    match userInput:
        case 1:
            pay_bills()
        case 2:
            change_details()
        case 3:
            delete_account()
        case _:
            print("\nIndex out of range!")
            welcome_page()

def pay_bills():
    global balance
    print(f"Balance: ₱{balance}")
    print("Pay your bills for these things!")
    print("\n1. CEBICO (₱3500)")
    print("2. Siwassco (₱500)")
    print("3. Groceries (₱2500)")
    while True:
        try: 
            userInput = int(input("Enter index: "))
            break
        except ValueError:
            print("\nPlease input an integer only!\n")
    cost = 0
    if userInput == 1: 
        cost = 3500
    elif userInput == 2: 
        cost = 500
    elif userInput == 3: 
        cost = 2500
    else:
        print("\nIndex out of range!\n")
        profile()
        return
    if balance >= cost:
        balance -= cost
        for bank_id, data in accounts.items():
            if data[2] == globalUser:
                data[0] = balance
                break
        with open(FILE_NAME, "w", encoding="utf-8") as f:
            json.dump(accounts, f, indent=4)
        print(f"\nSuccessfully paid! Your total balance is now ₱{balance}!\n")
    else:
        print("\nYour balance is too low!\n")
    profile()

def registration_page():
    global result
    userInput = input("Enter your username: ")
    pinInput = input("Enter your PIN: ")
    if len(str(pinInput)) != 6:
        print("Your PIN must be 6 digits long!")
        registration_page()
    while True:
        try:
            ageInput = int(input("Enter your age: "))
            break
        except ValueError:
            print("Please input an integer only!")
    if ageInput <= 12:
        print("You are too young to use our services!")
        welcome_page()
        return
    result = randomize_bank_id()
    print(f"Account added with bank ID {result}.")
    accounts[result] = [0, int(pinInput), userInput, ageInput]
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(accounts, f, indent=4)
    welcome_page()

def randomize_bank_id():
    last_id = max(accounts.keys())      
    next_id = str(int(last_id) + 1).zfill(4)
    return next_id

def change_details():
    global accounts, globalUser

    account_id = None
    for bank_id, data in accounts.items():
        if data[2] == globalUser:
            account_id = bank_id
            break

    if account_id is None:
        print("Account not found!")
        return

    changeUser = input("Enter new username (skip to leave unchanged): ")
    if changeUser != "":
        accounts[account_id][2] = changeUser
        globalUser = changeUser

    while True:
        try:
            changeAge = input("Enter new age (skip to leave unchanged): ")
            if changeAge != "":
                changeAge = int(changeAge)
                accounts[account_id][3] = changeAge
            break
        except ValueError:
            print("Please input an integer only!")

    while True:
        try:
            changePin = input("Enter new PIN (skip to leave unchanged): ")
            if changePin != "":
                changePin = int(changePin)
                accounts[account_id][1] = changePin
            elif len(str(changePin)) != 6:
                print("Your PIN must be 6 digits long!")
            break
            
        except ValueError:
            print("Please enter an integer only!")

    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(accounts, f, indent=4)

    print("\nDetails changed successfully!\n")
    profile()


def delete_account():
    global accounts, logged_in, globalUser, globalAge, balance

    while True:
        confirm = input("Are you sure you want to delete this account? (Y/N): ")
        if confirm.lower() == "y":
            pinInput = input("Enter your PIN to confirm: ")
            account_to_delete = None
            for bank_id, data in accounts.items():
                if data[2] == globalUser:
                    account_to_delete = bank_id
                    if str(data[1]) == pinInput:
                        print(f"Account {globalUser} has been deleted!")
                        del accounts[bank_id]
                        with open(FILE_NAME, "w", encoding="utf-8") as f:
                            json.dump(accounts, f, indent=4)
                        logged_in = False
                        globalUser = ''
                        globalAge = 0
                        balance = 0
                        welcome_page()
                        return
                    else:
                        print("Incorrect PIN!")
                        return
            print("Account not found!")
            return
        elif confirm.lower() == "n":
            profile()
            return

welcome_page()
