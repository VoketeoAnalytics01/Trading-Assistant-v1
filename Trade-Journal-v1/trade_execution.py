from datetime import datetime


def trade_execution(profile):
    """Pulls the planned trade from Risk-Check, then records whether/how it was actually executed."""

    print("\n=== Trade Execution ===")

    # Pull planned data from Risk-Check (if available)
    risk_trade = profile.get("risk", {}).get("current_trade", {})

    planned = {
        "entry_price": risk_trade.get("entry_price", 0),
        "stop_loss": risk_trade.get("stop_loss", 0),
        "take_profit": risk_trade.get("take_profit", 0),
        "position_size": risk_trade.get("position_size", 0),
        "risk_amount": risk_trade.get("risk_amount", 0),
        "reward_amount": risk_trade.get("reward_amount", 0),
        "risk_reward_ratio": risk_trade.get("risk_reward_ratio", 0)
    }

    if risk_trade:
        print("\nPlanned trade (from Risk Check):")
        print(f"  Entry        : {planned['entry_price']}")
        print(f"  Stop Loss    : {planned['stop_loss']}")
        print(f"  Take Profit  : {planned['take_profit']}")
        print(f"  Position Size: {planned['position_size']}")
    else:
        print("\nNo Risk-Check data found for this trade -- planned values left blank.")

    print("\nWas this trade executed?")
    print("1. Yes")
    print("2. No")

    while True:
        choice = input("Select 1-2: ").strip()
        if choice == "1":
            executed = True
            break
        elif choice == "2":
            executed = False
            break
        print("Invalid choice. Please select 1 or 2.")

    actual = {
        "entry_price": 0,
        "stop_loss": 0,
        "take_profit": 0,
        "position_size": 0,
        "slippage": 0
    }
    not_executed_reason = ""
    not_executed_note = ""
    execution_time = None

    if not executed:
        print("\nWhy was the trade not executed?")

        reasons = {
            "1": "Setup disappeared",
            "2": "Risk was too high",
            "3": "Changed my mind",
            "4": "Missed entry",
            "5": "Emotional decision",
            "6": "Technical/platform issue",
            "7": "Other"
        }

        for key, value in reasons.items():
            print(f"  {key}. {value}")

        while True:
            choice = input("Select reason: ").strip()
            if choice in reasons:
                not_executed_reason = reasons[choice]
                break
            print("Invalid choice.")

        if not_executed_reason == "Other":
            not_executed_note = input("Describe briefly: ").strip()

    else:
        while True:
            price_input = input("Actual execution price: ").strip()
            try:
                execution_price = float(price_input)
                if execution_price > 0:
                    break
                print("Price must be greater than zero.")
            except ValueError:
                print("Please enter a valid number.")

        actual["entry_price"] = execution_price
        actual["stop_loss"] = planned["stop_loss"]
        actual["take_profit"] = planned["take_profit"]
        actual["position_size"] = planned["position_size"]

        if planned["entry_price"]:
            actual["slippage"] = round(execution_price - planned["entry_price"], 5)

        execution_time = datetime.now().isoformat(timespec="seconds")

    profile["journal"]["current_trade"]["execution"] = {
        "executed": executed,
        "planned": planned,
        "actual": actual,
        "execution_time": execution_time,
        "not_executed_reason": not_executed_reason,
        "not_executed_note": not_executed_note
    }

    print("\n=== Execution Recorded ===")

    if executed:
        print("Status          : Executed")
        print(f"Execution Price : {actual['entry_price']}")
        if planned["entry_price"]:
            print(f"Slippage        : {actual['slippage']}")
        print(f"Execution Time  : {execution_time}")
    else:
        print("Status          : Not Executed")
        print(f"Reason          : {not_executed_reason}")
        if not_executed_note:
            print(f"Note            : {not_executed_note}")
