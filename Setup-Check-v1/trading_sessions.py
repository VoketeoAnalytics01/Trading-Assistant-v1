def trading_sessions(profile):
    """Collects which trading session(s) the user operates in (supports multiple)."""
    sessions_options = {
        "1": "Asian Session",
        "2": "London Session",
        "3": "New York Session",
        "4": "London/New York Overlap",
        "5": "Custom"
    }

    print("\nTrading sessions (you can pick more than one):")
    for key, val in sessions_options.items():
        print(f"  {key}. {val}")

    while True:
        raw = input("Select session numbers, separated by commas (e.g. 1,3): ").strip()
        choices = [c.strip() for c in raw.split(",") if c.strip()]

        if choices and all(c in sessions_options for c in choices):
            break
        print("Invalid entry. Use numbers from the list, separated by commas.")

    for choice in choices:
        if choice == "5":
            custom_name = input("Enter your custom session name: ").strip()
            profile["trading"]["sessions"].append(custom_name)
        else:
            profile["trading"]["sessions"].append(sessions_options[choice])
