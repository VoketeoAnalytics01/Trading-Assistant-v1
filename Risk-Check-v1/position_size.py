def position_size(profile):

    print("\n=== Position Size Calculation ===")

    balance = profile["risk"]["account"]["balance"]

    risk_percent = profile["risk"]["settings"]["risk_per_trade"]

    trade = profile["risk"]["current_trade"]

    entry = trade["entry"]
    stop = trade["stop_loss"]
    target = trade["take_profit"]
    direction = trade.get("direction", "")

    # Risk amount ($)
    risk_amount = balance * (risk_percent / 100)

    # Price distances
    stop_distance = abs(entry - stop)
    reward_distance = abs(target - entry)

    # Prevent division by zero
    if stop_distance == 0:
        print("Stop Loss cannot equal Entry Price.")
        trade["status"] = "Invalid"
        return

    # Sanity check: stop/target should be on the correct side of entry for the direction.
    # Doesn't block the calculation -- same soft-warning philosophy as risk_validation --
    # but a backwards stop/target means the numbers below don't represent a real setup.
    if direction == "Buy" and (stop >= entry or target <= entry):
        print("Warning: Stop Loss/Take Profit don't look right for a Buy (expected stop below entry, target above).")
    elif direction == "Sell" and (stop <= entry or target >= entry):
        print("Warning: Stop Loss/Take Profit don't look right for a Sell (expected stop above entry, target below).")

    # Position size (generic units) -- renamed from `position_size` to avoid
    # shadowing this function's own name inside its own body.
    computed_size = risk_amount / stop_distance

    # Risk : Reward
    rr = reward_distance / stop_distance

    # Save calculations
    trade["risk_amount"] = round(risk_amount, 2)
    trade["reward_amount"] = round(reward_distance, 5)
    trade["position_size"] = round(computed_size, 2)
    trade["rr"] = round(rr, 2)
    trade["status"] = "Calculated"

    print(f"Risk Amount : ${trade['risk_amount']}")
    print(f"Position Size : {trade['position_size']}")
    print(f"Risk : Reward : 1 : {trade['rr']}")

