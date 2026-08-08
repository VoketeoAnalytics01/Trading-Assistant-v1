def risk_profile(profile):

    if "risk" not in profile:

        profile["risk"] = {

            "setup_complete": False,

            "account": {
                "balance": 0.0,
                "currency": "",
                "broker": "",
                "account_type": ""
            },

            "settings": {
                "risk_per_trade": 0.0,
                "daily_loss_limit": 0.0,
                "weekly_loss_limit": 0.0,
                "max_open_trades": 0,
                "minimum_rr": 0.0
            },

            "current_trade": {

                "market": "",
                "asset": "",

                "entry": 0.0,
                "stop_loss": 0.0,
                "take_profit": 0.0,

                "stop_loss_pips": 0.0,
                "take_profit_pips": 0.0,

                "risk_amount": 0.0,
                "reward_amount": 0.0,

                "rr": 0.0,
                "position_size": 0.0,

                "status": "Pending"
            },

            "validation": {

                "approved": False,

                "warnings": [],

                "errors": []

            },

            "history": []

        }

    return profile
