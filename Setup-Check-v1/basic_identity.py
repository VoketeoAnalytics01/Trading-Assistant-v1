def basic_identity(profile):
    """Collects username, full name, and email."""
    profile["username"] = input("Choose a username: ").strip()
    profile["full_name"] = input("Full name (optional): ").strip()
    profile["email"] = input("Email: ").strip()
