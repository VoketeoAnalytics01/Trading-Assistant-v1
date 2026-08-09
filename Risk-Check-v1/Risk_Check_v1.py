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
    print("(Standalone test only -- the real app supplies a Setup-Check profile via main.py)\n")

    # Minimal fixture -- only "username" matters here, since risk_profile()
    # builds its own "risk" section regardless of what else is in profile.
    profile = {"username": "john"}

    risk_check(profile)

    print("\nRisk Check Completed Successfully!\n")
    print(profile)
