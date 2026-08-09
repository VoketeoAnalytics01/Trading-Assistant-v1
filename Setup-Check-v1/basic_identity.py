def basic_identity(profile):
    """Collects additional identity information for an authenticated user."""

    print("\n=== Basic Identity ===")

    print(f"Username: {profile['username']}")

    profile["full_name"] = input("Full name (optional): ").strip()
    profile["email"] = input("Email: ").strip()
