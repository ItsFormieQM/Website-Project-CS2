choice = 0
balance = 0
logged_in = False
globalUser = ''
globalAge = 0
accounts = {
    # bank_id: [balance, pin,name,age]
    "0000": [5100,123456,"Frisk", 8],
    "1111": [5300,246810,"Chara", 11],
    "2222": [5500,122555,"Kris", 15],
    "3333": [6767,123456,"Formie", 13]
}
print("Welcome to Grilby's ATM!")
print("How may I help you? - Grilby's")

def caseSwitch():
    if choice == 1:
        print("1")
    elif choice == 2:
        login_page()
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
    while True:
        try: 
            userInput = int(input("Enter index: "))
            break
        except ValueError:
            print("\nPlease input an integer only!\n")
    match userInput:
        case 1:
            pay_bills()
        case _:
            print("\nIndex out of range!\n")
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
    match userInput:
        case 1:
            if balance >= 3500:
                balance -= 3500
                print(f"\nSucessfully paid for CEBICO! Your total balance is now ₱{balance}!\n")
                pay_bills()
            else:
                print("\nYour balance is too low and purchasing this item will make you go bankrupt!\n")
                pay_bills()
        case 2:
            if balance >= 500:
                balance -= 500
                print(f"\nSucessfully paid for Siwassco! Your total balance is now ₱{balance}!\n")
                pay_bills()
            else:
                print("\nYour balance is too low and purchasing this item will make you go bankrupt!\n")
                pay_bills()
        case 3:
            if balance >= 2500:
                balance -= 2500
                print(f"\nSucessfully paid for Groceries! Your total balance is now ₱{balance}!\n")
                pay_bills()
            else:
                print("\nYour balance is too low and purchasing this item will make you go bankrupt!\n")
                pay_bills()
        case _:
            print("\nIndex out of range!\n")
            welcome_page()

welcome_page()
# eh work in progress type shi 