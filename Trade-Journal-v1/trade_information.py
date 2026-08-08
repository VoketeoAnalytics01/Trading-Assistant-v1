from datetime import date


def trade_information(profile):
    """Collects basic trade info: market, symbol, session, direction, and date."""
    print("\n=== Trade Information ===")

    trading = profile.get("trading", {})

    # Market -- reuse markets configured in Setup-Check if available
    markets = trading.get("markets", [])
    if markets:
        print("\nMarket:")
        for i, m in enumerate(markets, start=1):
            print(f"  {i}. {m}")
        while True:
            choice = input(f"Select 1-{len(markets)}: ").strip()
            if choice.isdigit() and 1 <= int(choice) <= len(markets):
                market = markets[int(choice) - 1]
                break
            print("Invalid choice.")
    else:
        market = input("Market: ").strip()

    # Symbol -- reuse configured assets if available, with a manual fallback
    assets = trading.get("assets", [])
    if assets:
        print("\nSymbol:")
        for i, a in enumerate(assets, start=1):
            print(f"  {i}. {a}")
        other_index = len(assets) + 1
        print(f"  {other_index}. Other (type manually)")
        while True:
            choice = input(f"Select 1-{other_index}: ").strip()
            if choice.isdigit() and 1 <= int(choice) <= len(assets):
                symbol = assets[int(choice) - 1]
                break
            elif choice.isdigit() and int(choice) == other_index:
                symbol = input("Enter symbol: ").strip().upper()
                break
            print("Invalid choice.")
    else:
        symbol = input("Symbol: ").strip().upper()

    # Session -- reuse configured sessions if available
    sessions = trading.get("sessions", [])
    if sessions:
        print("\nSession:")
        for i, s in enumerate(sessions, start=1):
            print(f"  {i}. {s}")
        while True:
            choice = input(f"Select 1-{len(sessions)}: ").strip()
            if choice.isdigit() and 1 <= int(choice) <= len(sessions):
                session = sessions[int(choice) - 1]
                break
            print("Invalid choice.")
    else:
        session = input("Session: ").strip()

    # Direction
    directions = {"1": "Long", "2": "Short"}
    print("\nDirection:")
    for key, val in directions.items():
        print(f"  {key}. {val}")
    while True:
        choice = input("Select 1-2: ").strip()
        if choice in directions:
            direction = directions[choice]
            break
        print("Invalid choice.")

    # Date -- captured automatically, no need to ask
    trade_date = date.today().isoformat()

    profile["journal"]["current_trade"]["trade_info"] = {
        "market": market,
        "symbol": symbol,
        "session": session,
        "direction": direction,
        "date": trade_date
    }
