def account_information(profile):

    print("\n=== Account Information ===")

    # Account Balance
    while True:
        try:
            balance = float(input("Account Balance: "))
            if balance > 0:
                profile["risk"]["account"]["balance"] = balance
                break
            print("Balance must be greater than 0.")
        except ValueError:
            print("Please enter a valid number.")

    # Currency
    currencies = {
        "1": "USD",
        "2": "EUR",
        "3": "GBP",
        "4": "KES",
        "5": "Custom"
    }

    print("\nAccount Currency:")
    for key, value in currencies.items():
        print(f"{key}. {value}")

    while True:
        choice = input("Select 1-5: ").strip()

        if choice in currencies:
            if choice == "5":
                profile["risk"]["account"]["currency"] = input(
                    "Enter currency: "
                ).upper()
            else:
                profile["risk"]["account"]["currency"] = currencies[choice]
            break

        print("Invalid choice.")

    # Broker
    profile["risk"]["account"]["broker"] = input(
        "Broker Name: "
    ).strip()

    # Account Type
    account_types = {
        "1": "Demo",
        "2": "Live",
        "3": "Prop Firm"
    }

    print("\nAccount Type:")
    for key, value in account_types.items():
        print(f"{key}. {value}")

    while True:
        choice = input("Select 1-3: ").strip()

        if choice in account_types:
            profile["risk"]["account"]["account_type"] = account_types[choice]
            break

        print("Invalid choice.")
