import hashlib
import hmac
import json
import os


# --------------------------------------------------
# Persistent authentication storage
# --------------------------------------------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AUTH_DIR = os.path.join(BASE_DIR, "Data", "auth")
USERS_FILE = os.path.join(AUTH_DIR, "users.json")


def load_credentials():
    """Load registered users from persistent storage."""

    os.makedirs(AUTH_DIR, exist_ok=True)

    if not os.path.exists(USERS_FILE):
        return {}

    try:
        with open(USERS_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    except (json.JSONDecodeError, OSError):
        print("Warning: Could not load saved user credentials.")
        return {}


def save_credentials(credentials):
    """Save registered users to persistent storage."""

    os.makedirs(AUTH_DIR, exist_ok=True)

    with open(USERS_FILE, "w", encoding="utf-8") as file:
        json.dump(credentials, file, indent=4)

    # Restrict file permissions where supported.
    try:
        os.chmod(USERS_FILE, 0o600)
    except OSError:
        pass


# --------------------------------------------------
# Password security
# --------------------------------------------------

def hash_password(password, salt=None):
    """
    Hash a password using PBKDF2-HMAC-SHA256.

    Returns:
        (salt_hex, hash_hex)
    """

    if salt is None:
        salt = os.urandom(16)

    pw_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt,
        100_000
    )

    return salt.hex(), pw_hash.hex()


def verify_password(password, salt_hex, hash_hex):
    """Verify a password against the stored salt and hash."""

    try:
        salt = bytes.fromhex(salt_hex)
    except ValueError:
        return False

    _, attempt_hash = hash_password(password, salt)

    return hmac.compare_digest(attempt_hash, hash_hex)


# --------------------------------------------------
# Password validation
# --------------------------------------------------

def valid_password(password):
    """Check whether password meets the current Beta requirements."""

    upper_case = 0
    lower_case = 0
    digits = 0
    special_count = 0

    special_char = "!@#$%^&*()-_=+[]{};:,.<>?/"

    for ch in password:
        if ch.isupper():
            upper_case += 1
        elif ch.islower():
            lower_case += 1
        elif ch.isdigit():
            digits += 1
        elif ch in special_char:
            special_count += 1

    return (
        len(password) >= 8
        and upper_case >= 2
        and lower_case >= 2
        and digits >= 1
        and special_count >= 2
    )


# --------------------------------------------------
# Login system
# --------------------------------------------------

def login_system():
    """Register and authenticate users using persistent credentials."""

    credentials = load_credentials()

    while True:

        print("1. New user")
        print("2. Verified user")
        print("3. Exit")

        select = input("Select an option: ").strip()

        # ------------------------------------------
        # New user
        # ------------------------------------------

        if select == "1":

            new_username = input("New username: ").strip()

            if not new_username:
                print("Username can't be empty.")
                continue

            if new_username in credentials:
                print("Username already registered, please login.")
                continue

            new_password = input("Enter new password: ")

            if valid_password(new_password):

                salt, pw_hash = hash_password(new_password)

                credentials[new_username] = {
                    "salt": salt,
                    "hash": pw_hash
                }

                save_credentials(credentials)

                print("Valid password, registered.")

            else:

                requirements = [
                    "At least 8 characters total",
                    "At least 2 uppercase characters",
                    "At least 2 lowercase characters",
                    "At least 1 number and 2 special characters"
                ]

                print("Password requirements:")
                print("=" * 35)

                for i, req in enumerate(requirements, start=1):
                    print(f"{i}. {req}")

        # ------------------------------------------
        # Existing user
        # ------------------------------------------

        elif select == "2":

            logged_in = False
            tries = 4

            while tries > 0 and not logged_in:

                username = input("Enter username: ").strip()
                password = input("Enter password: ")

                record = credentials.get(username)

                if (
                    record
                    and verify_password(
                        password,
                        record["salt"],
                        record["hash"]
                    )
                ):

                    logged_in = True

                    print("=" * 40)
                    print(f"Welcome, {username}")
                    print("Login successful!")
                    print("=" * 40)

                    return username

                else:

                    tries -= 1

                    print("Invalid username or password.")
                    print(f"Attempts remaining: {tries}")

            if not logged_in:
                print("Out of attempts.")

        # ------------------------------------------
        # Exit
        # ------------------------------------------

        elif select == "3":

            print("Have a nice day!")
            return None

        else:

            print("Please select one of the options above.")


# --------------------------------------------------
# Standalone test
# --------------------------------------------------

if __name__ == "__main__":

    print("=== Trading Assistant V1 Login ===\n")

    username = login_system()

    if username:
        print(f"\nAuthenticated user: {username}")
