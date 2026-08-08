def trade_calculator(profile):

    print("\n=== New Trade ===")

    assets_by_market = {
        "Forex": [
            "EURUSD", "GBPUSD", "USDJPY",
            "AUDUSD", "USDCHF", "USDCAD", "NZDUSD"
        ],

        "Crypto": [
            "BTCUSD", "ETHUSD", "SOLUSD", "XRPUSD"
        ],

        "Indices": [
            "US100", "SPX500", "GER40", "UK100"
        ],

        "Commodities": [
            "XAUUSD", "XAGUSD", "WTI", "Brent"
        ],

        "Stocks": [
            "AAPL", "TSLA", "NVDA", "MSFT"
        ]
    }

    trader_assets = profile["trading"]["assets"]

    available_assets = []

    print("\nAvailable Assets:")

    number = 1

    for market in profile["trading"]["markets"]:

        print(f"\n{market}")

        for asset in assets_by_market.get(market, []):

            if asset in trader_assets:
                available_assets.append((asset, market))
                print(f"{number}. {asset}")
                number += 1

    while True:

        try:
            choice = int(input("\nSelect Asset: "))

            if 1 <= choice <= len(available_assets):

                asset, market = available_assets[choice - 1]

                profile["risk"]["current_trade"]["asset"] = asset
                profile["risk"]["current_trade"]["market"] = market

                break

            print("Invalid selection.")

        except ValueError:
            print("Please enter a number.")

    while True:

        direction = input("Direction (Buy/Sell): ").strip().lower()

        if direction in ["buy", "sell"]:
            profile["risk"]["current_trade"]["direction"] = direction.title()
            break

        print("Please enter Buy or Sell.")

    while True:
        try:
            profile["risk"]["current_trade"]["entry"] = float(
                input("Entry Price: ")
            )
            break
        except ValueError:
            print("Enter a valid number.")

    while True:
        try:
            profile["risk"]["current_trade"]["stop_loss"] = float(
                input("Stop Loss: ")
            )
            break
        except ValueError:
            print("Enter a valid number.")

    while True:
        try:
            profile["risk"]["current_trade"]["take_profit"] = float(
                input("Take Profit: ")
            )
            break
        except ValueError:
            print("Enter a valid number.")
