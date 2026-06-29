from datetime import datetime

USERS_FILE = "users.txt"
AUDIT_FILE = "audittrail.txt"


def log_audit(username, action):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(AUDIT_FILE, "a") as f:
        f.write(f"[{timestamp}] USER={username} | ACTION={action}\n")


def load_users():
    users = {}
    try:
        with open(USERS_FILE, "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    parts = line.split(",")
                    username, password, balance = parts[0], parts[1], float(parts[2])
                    users[username] = {"password": password, "balance": balance}
    except FileNotFoundError:
        pass
    return users


def save_users(users):
    with open(USERS_FILE, "w") as f:
        for username, data in users.items():
            f.write(f"{username},{data['password']},{data['balance']}\n")
    log_audit("SYSTEM", "User data saved to file")


def login(users):
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()
    if username in users and users[username]["password"] == password:
        print(f"Login successful. Welcome, {username}!")
        log_audit(username, "LOGGED IN")
        return username
    else:
        print("Invalid username or password.")
        log_audit(username, "FAILED LOGIN ATTEMPT")
        return None


def logout(username):
    print(f"Goodbye, {username}!")
    log_audit(username, "LOGGED OUT")


def register(users):
    username = input("Choose a username: ").strip()
    if username in users:
        print("Username already exists.")
        return
    password = input("Choose a password: ").strip()
    users[username] = {"password": password, "balance": 0.0}
    save_users(users)
    print(f"Account created for '{username}'.")
    log_audit(username, "ACCOUNT REGISTERED")
