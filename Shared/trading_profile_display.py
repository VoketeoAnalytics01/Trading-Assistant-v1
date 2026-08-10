def trading_profile_display(profile):
    """Displays the trader's saved trading profile."""

    username = profile.get("username", "Unknown")

    print("\n========================================")
    print("          TRADING PROFILE")
    print("========================================")

    print(f"Username      : {username}")
    print(f"Account Type  : {profile.get('account_type', 'Not set')}")
    print(f"Broker        : {profile.get('broker', 'Not set')}")
    print(f"Balance       : {profile.get('balance', 'Not set')}")

    print("\n========================================")
    input("Press Enter to return to Dashboard...")
