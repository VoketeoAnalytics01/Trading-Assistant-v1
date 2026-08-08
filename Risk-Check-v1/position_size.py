def position_size(profile):

    print("\n=== Position Size Calculation ===")

    balance = profile["risk"]["account"]["balance"]

    risk_percent = profile["risk"]["settings"]["risk_per_trade"]

    trade = profile["risk"]["current_trade"]

    entry = trade["entry"]
    stop = trade["stop_loss"]
    target = trade["take_profit"]

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

    # Position size (generic units)
    position_size = risk_amount / stop_distance

    # Risk : Reward
    rr = reward_distance / stop_distance

    # Save calculations
    trade["risk_amount"] = round(risk_amount, 2)

    trade["reward_amount"] = round(reward_distance, 5)

    trade["position_size"] = round(position_size, 2)

    trade["rr"] = round(rr, 2)

    trade["status"] = "Calculated"

    print(f"Risk Amount : ${trade['risk_amount']}")
    print(f"Position Size : {trade['position_size']}")
    print(f"Risk : Reward : 1 : {trade['rr']}")

