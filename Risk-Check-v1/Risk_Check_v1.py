from risk_profile import risk_profile
from account_information import account_information
from risk_setting import risk_setting
from new_trade import new_trade
from trade_calculator import trade_calculator
from position_size import position_size
from risk_validation import risk_validation
from trade_checklist import trade_checklist
from trade_summary_display import trade_summary_display

def risk_check(profile):

    # Create risk structure
    risk_profile(profile)

    # First-time setup
    if not profile["risk"]["setup_complete"]:
        account_information(profile)
        risk_setting(profile)
        profile["risk"]["setup_complete"] = True

    # New trade
    new_trade(profile)

    # Trade workflow
    trade_calculator(profile)
    position_size(profile)
    risk_validation(profile)
    trade_checklist(profile)
    trade_summary_display(profile)

    return profile


if __name__ == "__main__":

    print("=== Trading Assistant V1 : Risk Check ===\n")

    # ==================================================
    # TEMPORARY PROFILE (FOR DEVELOPMENT & TESTING ONLY)
    # Replace this with Setup_Check_v1 profile later.
    # ==================================================

    profile = {

        "username": "john",

        "trading": {

            "markets": [
                "Forex",
                "Crypto",
                "Indices",
                "Commodities",
                "Stocks"
            ],

            "assets": [

                # Forex
                "EURUSD",
                "GBPUSD",
                "USDJPY",
                "AUDUSD",
                "USDCHF",
                "USDCAD",
                "NZDUSD",

                # Crypto
                "BTCUSD",
                "ETHUSD",
                "SOLUSD",
                "XRPUSD",

                # Indices
                "US100",
                "SPX500",
                "GER40",
                "UK100",

                # Commodities
                "XAUUSD",
                "XAGUSD",
                "WTI",
                "Brent",

                # Stocks
                "AAPL",
                "TSLA",
                "NVDA",
                "MSFT"
            ]
        },

        "trading_plan": {

            "rules_count": 4,

            "minimum_conditions": 3,

            "setup_threshold": 75,

            "conditions": [
                "Asian liquidity sweep",
                "High impact news",
                "Low market momentum",
                "Undefined daily bias"
            ]
        }
    }

    profile = risk_check(profile)

    print("\nRisk Check Completed Successfully!\n")
    print(profile)
