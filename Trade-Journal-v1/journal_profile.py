def journal_profile(profile):

    if "journal" not in profile:

        profile["journal"] = {

            "current_trade": {
                "trade_info": {},
                "execution": {},
                "outcome": {},
                "psychology": {},
                "lesson": {},
                "screenshots": [],
                "adherence": {}
            },

            "entries": [],

            "statistics": {
                "total_trades": 0,
                "wins": 0,
                "losses": 0,
                "break_even": 0,
                "win_rate": 0.0,
                "gross_profit": 0.0,
                "gross_loss": 0.0,
                "net_profit": 0.0,
                "average_rr": 0.0,
                "best_trade": 0.0,
                "worst_trade": 0.0,
                "current_win_streak": 0,
                "current_loss_streak": 0,
                "best_win_streak": 0,
                "best_loss_streak": 0,
                "average_adherence_pct": 0.0,
                "fully_adherent_trades": 0
            }
        }
