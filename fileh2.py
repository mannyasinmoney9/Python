from fileh1 import save_users, log_audit


def check_balance(users, username):
    balance = users[username]["balance"]
    print(f"Current balance: ${balance:.2f}")
    log_audit(username, f"CHECKED BALANCE | Balance=${balance:.2f}")


def deposit(users, username):
    try:
        amount = float(input("Enter deposit amount: $"))
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
        users[username]["balance"] += amount
        save_users(users)
        print(f"Deposited ${amount:.2f}. New balance: ${users[username]['balance']:.2f}")
        log_audit(username, f"DEPOSIT | Amount=${amount:.2f} | Balance=${users[username]['balance']:.2f}")
    except ValueError:
        print("Invalid amount entered.")


def withdraw(users, username):
    try:
        amount = float(input("Enter withdrawal amount: $"))
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
        if amount > users[username]["balance"]:
            print("Insufficient funds.")
            log_audit(username, f"FAILED WITHDRAWAL | Amount=${amount:.2f} | Reason=Insufficient funds")
            return
        users[username]["balance"] -= amount
        save_users(users)
        print(f"Withdrew ${amount:.2f}. New balance: ${users[username]['balance']:.2f}")
        log_audit(username, f"WITHDRAWAL | Amount=${amount:.2f} | Balance=${users[username]['balance']:.2f}")
    except ValueError:
        print("Invalid amount entered.")
