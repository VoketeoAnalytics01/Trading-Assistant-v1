def new_entry(profile):
    """Starts a new journal entry while preserving the Risk Check trade data."""

    risk_trade = profile.get("risk", {}).get("current_trade", {})

    profile["journal"]["current_trade"] = {
        "trade_info": {
            "market": risk_trade.get("market", ""),
            "symbol": risk_trade.get("asset", ""),
            "session": "",
            "direction": risk_trade.get("direction", ""),
            "date": ""
        },
        "execution": {},
        "outcome": {},
        "psychology": [],
        "lesson": {},
        "screenshots": [],
        "adherence": {}
    }
