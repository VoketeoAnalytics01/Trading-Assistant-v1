def trading_style(profile):
    """Prompts for trading style from a fixed menu (with custom option)."""
    styles = {
        "1": "scalping",
        "2": "day_trading",
        "3": "swing_trading",
        "4": "position",
        "5": "custom"
    }
    print("\nTrading style:")
    for key, val in styles.items():
        print(f"  {key}. {val}")

    while True:
        choice = input("Select 1-5: ").strip()
        if choice in styles:
            break
        print("Invalid choice. Please select a number between 1 and 5.")

    if choice == "5":
        profile["trading"]["style"] = input("Enter your custom style name: ").strip()
    else:
        profile["trading"]["style"] = styles[choice]
