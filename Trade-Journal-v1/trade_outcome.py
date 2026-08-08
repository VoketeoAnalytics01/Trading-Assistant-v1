from datetime import datetime


def trade_outcome(profile):
    """Records the outcome of the trade: close price, P&L, result, and R multiple achieved."""
    execution = profile["journal"]["current_trade"].get("execution", {})

    print("\n=== Trade Outcome ===")

    if not execution.get("executed"):
        print("This trade wasn't executed, so there's no outcome to record.")
        profile["journal"]["current_trade"]["outcome"] = {
            "applicable": False,
            "close_price": 0,
            "close_time": None,
            "pnl": 0.0,
            "result": "",
            "r_multiple": 0.0
        }
        return

    while True:
        price_input = input("Close price: ").strip()
        try:
            close_price = float(price_input)
            if close_price > 0:
                break
            print("Price must be greater than zero.")
        except ValueError:
            print("Please enter a valid number.")

    while True:
        pnl_input = input("Profit/Loss (use - for a loss, e.g. -25.50): ").strip()
        try:
            pnl = float(pnl_input)
            break
        except ValueError:
            print("Please enter a valid number.")

    if pnl > 0:
        result = "Win"
    elif pnl < 0:
        result = "Loss"
    else:
        result = "Break-even"

    planned_risk = execution.get("planned", {}).get("risk_amount", 0)
    r_multiple = round(pnl / planned_risk, 2) if planned_risk else 0.0

    close_time = datetime.now().isoformat(timespec="seconds")

    profile["journal"]["current_trade"]["outcome"] = {
        "applicable": True,
        "close_price": close_price,
        "close_time": close_time,
        "pnl": pnl,
        "result": result,
        "r_multiple": r_multiple
    }

    print("\n=== Outcome Recorded ===")
    print(f"Result    : {result}")
    print(f"P&L       : {pnl}")
    print(f"R Multiple: {r_multiple}")
