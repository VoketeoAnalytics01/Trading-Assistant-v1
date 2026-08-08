def trading_asset(profile):
    """Collects specific assets to trade from a catalog matched to selected markets."""
    market_assets = {
        "Forex": ["EURUSD", "GBPUSD", "USDJPY", "AUDUSD", "USDCHF", "USDCAD", "NZDUSD"],
        "Crypto": ["BTCUSD", "ETHUSD", "SOLUSD", "XRPUSD"],
        "Indices": ["US100", "SPX500", "GER40", "UK100"],
        "Stocks": ["AAPL", "TSLA", "NVDA", "MSFT"],
        "Commodities": ["XAUUSD", "XAGUSD", "WTI", "Brent"],
        "Options": ["Stock Options", "Index Options"],
        "Futures": ["ES", "NQ", "CL", "GC"]
    }

    print("\nTrading Assets")

    for market in profile["trading"]["markets"]:
        print(f"\n{market}")
        assets = market_assets.get(market, [])

        if not assets:
            raw = input(f"No preset list for '{market}'. Enter asset symbols, comma-separated (blank to skip): ").strip()
            for asset in [a.strip() for a in raw.split(",") if a.strip()]:
                if asset not in profile["trading"]["assets"]:
                    profile["trading"]["assets"].append(asset)
            continue

        while True:
            for i, asset in enumerate(assets, start=1):
                print(f"{i}. {asset}")
            print("0. Done")

            choice = input("Select asset: ").strip()

            if choice == "0":
                break

            if choice.isdigit():
                index = int(choice) - 1
                if 0 <= index < len(assets):
                    a = assets[index]
                    if a not in profile["trading"]["assets"]:
                        profile["trading"]["assets"].append(a)
                        print(f"✓ {a} added.")
                    else:
                        print("Asset already selected.")
                else:
                    print("Invalid choice.")
            else:
                print("Please enter a number.")
