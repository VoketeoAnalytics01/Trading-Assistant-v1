import hashlib
import os


def hash_password(password, salt=None):
    """Hashes a password with PBKDF2-HMAC-SHA256 (stdlib only, no pip install needed).
    Returns (salt_hex, hash_hex). Generates a random salt if none is given.
    """
    if salt is None:
        salt = os.urandom(16)
    pw_hash = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100_000)
    return salt.hex(), pw_hash.hex()


def verify_password(password, salt_hex, hash_hex):
    salt = bytes.fromhex(salt_hex)
    _, attempt_hash = hash_password(password, salt)
    return attempt_hash == hash_hex


def login_system():
    credentials = {}  # username -> {"salt": ..., "hash": ...}

    while True:
        print('1. New user')
        print('2. Verified user')
        print('3. Exit')
        select = input("Select an option: ").strip()

        if select == "1":
            new_username = input("New username: ").strip()

            if not new_username:
                print("Username can't be empty.")
                continue

            if new_username in credentials:
                print("Username already registered, please login.")
                continue

            new_password = input("Enter new password: ")

            upper_case = lower_case = digits = special_count = 0
            special_char = "!@#$%^&*()-_=+[]{};:,.<>?/"

            for ch in new_password:
                if ch.isupper():
                    upper_case += 1
                elif ch.islower():
                    lower_case += 1
                elif ch.isdigit():
                    digits += 1
                elif ch in special_char:
                    special_count += 1

            if (len(new_password) >= 8 and upper_case >= 2 and lower_case >= 2
                    and digits >= 1 and special_count >= 2):
                salt, pw_hash = hash_password(new_password)
                credentials[new_username] = {"salt": salt, "hash": pw_hash}
                print("Valid password, registered.")
            else:
                requirements = [
                    "At least 8 characters total",
                    "At least 2 uppercase characters",
                    "At least 2 lowercase characters",
                    "At least 1 number and 2 special characters"
                ]
                print("Password requirements:")
                print('=' * 35)
                for i, req in enumerate(requirements, start=1):
                    print(f"{i}. {req}")

        elif select == "2":
            logged_in = False
            tries = 4
            while tries > 0 and not logged_in:
                username = input('Enter username: ').strip()
                password = input('Enter password: ')

                record = credentials.get(username)
                if record and verify_password(password, record["salt"], record["hash"]):
                    logged_in = True
                    print('=' * 40)
                    print(f"Welcome, {username}")
                    print("Login successful!")
                    print('=' * 40)
                    return username
                else:
                    tries -= 1
                    print("Invalid username or password.")
                    print(f"Attempts remaining: {tries}")

            if not logged_in:
                print("Out of attempts.")

        elif select == "3":
            print("Have a nice day!")
            break

        else:
            print("Please select one of the options above.")


if __name__ == "__main__":
    login_system()
