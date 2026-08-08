def risk_setting(profile):

    print("\n=== Risk Settings ===")

    # Risk Per Trade
    while True:
        try:
            risk = float(input("Risk per Trade (%): "))

            if 0 < risk <= 100:
                profile["risk"]["settings"]["risk_per_trade"] = risk
                break

            print("Risk must be between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")

    # Daily Loss Limit
    while True:
        try:
            daily = float(input("Daily Loss Limit (%): "))

            if daily > 0:
                profile["risk"]["settings"]["daily_loss_limit"] = daily
                break

            print("Must be greater than 0.")

        except ValueError:
            print("Please enter a valid number.")

    # Weekly Loss Limit
    while True:
        try:
            weekly = float(input("Weekly Loss Limit (%): "))

            if weekly > 0:
                profile["risk"]["settings"]["weekly_loss_limit"] = weekly
                break

            print("Must be greater than 0.")

        except ValueError:
            print("Please enter a valid number.")

    # Maximum Open Trades
    while True:
        try:
            trades = int(input("Maximum Open Trades: "))

            if trades > 0:
                profile["risk"]["settings"]["max_open_trades"] = trades
                break

            print("Must be at least 1.")

        except ValueError:
            print("Enter a whole number.")

    # Minimum Risk:Reward
    while True:
        try:
            rr = float(input("Minimum Risk:Reward Ratio: "))

            if rr > 0:
                profile["risk"]["settings"]["minimum_rr"] = rr
                break

            print("Must be greater than 0.")

        except ValueError:
            print("Please enter a valid number.")
