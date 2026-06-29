from fileh1 import load_users, save_users, login, logout, register
from fileh2 import check_balance, deposit, withdraw


def main_menu(users, username):
    while True:
        print("\n--- Banking Menu ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Save & Stay Logged In")
        print("5. Logout")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            check_balance(users, username)
        elif choice == "2":
            deposit(users, username)
        elif choice == "3":
            withdraw(users, username)
        elif choice == "4":
            save_users(users)
            print("Data saved.")
        elif choice == "5":
            logout(username)
            break
        else:
            print("Invalid option. Try again.")


def start():
    users = load_users()

    while True:
        print("\n=== Simple Bank App ===")
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            username = login(users)
            if username:
                main_menu(users, username)
        elif choice == "2":
            register(users)
        elif choice == "3":
            print("Exiting app. Goodbye!")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    start()
