def new_trade(profile):

    profile["risk"]["current_trade"] = {
        "asset": "",
        "market": "",
        "direction": "",
        "entry": 0.0,
        "stop_loss": 0.0,
        "take_profit": 0.0,
        "position_size": 0.0,
        "risk_amount": 0.0,
        "reward_amount": 0.0,
        "rr": 0.0,
        "status": "Pending"
    }
