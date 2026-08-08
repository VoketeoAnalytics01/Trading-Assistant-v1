def new_entry(profile):
    """Resets the current journal entry to fresh defaults before logging a new trade."""
    profile["journal"]["current_trade"] = {
        "trade_info": {},
        "execution": {},
        "outcome": {},
        "psychology": [],
        "lesson": {},
        "screenshots": [],
        "adherence": {}
    }
