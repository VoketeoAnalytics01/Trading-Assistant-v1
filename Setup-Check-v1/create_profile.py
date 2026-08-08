def create_profile():
    """Creates and returns a blank profile dict with all default fields."""
    return {
        "username": "",
        "full_name": "",
        "email": "",
        "country": "",
        "timezone": "",
        "account_type": "Free",
        "trading": {
            "style": "",
            "experience": "",
            "sessions": [],
            "markets": [],
            "assets": []
        },
        "trading_plan": {
            "rules_count": 0,
            "minimum_conditions": 0,
            "setup_threshold": 75
        },
        "performance": {},
        "goals": [],
        "preferences": {},
        "premium": {}
    }
