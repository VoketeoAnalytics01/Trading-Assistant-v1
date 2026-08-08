def trading_markets(profile):
    """Collects which market(s) the user trades (supports multiple)."""
    markets_options = {
        "1": "Forex",

        "2": "Crypto",
        "3": "Indices",
        "4": "Stocks",
        "5": "Commodities",
        "6": "Options",
        "7": "Futures"
    }

    print("\nMarkets you trade (you can pick more than one):")
    for key, val in markets_options.items():
        print(f"  {key}. {val}")

    while True:
        raw = input("Select market numbers, separated by commas (e.g. 1,2): ").strip()
        choices = [c.strip() for c in raw.split(",") if c.strip()]

        if choices and all(c in markets_options for c in choices):
            break
        print("Invalid entry. Use numbers from the list, separated by commas.")

    for choice in choices:
        market = markets_options[choice]
        if market not in profile["trading"]["markets"]:
            profile["trading"]["markets"].append(market)
