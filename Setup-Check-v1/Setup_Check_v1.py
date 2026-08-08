from summary_display import summary_display
from create_profile import create_profile
from basic_identity import basic_identity
from trading_style import trading_style
from trading_experience import trading_experience
from trading_sessions import trading_sessions
from trading_markets import trading_markets
from trading_asset import trading_asset
from trading_plan import trading_plan


def setup_check():

    profile = create_profile()

    basic_identity(profile)
    trading_style(profile)
    trading_experience(profile)
    trading_sessions(profile)
    trading_markets(profile)
    trading_asset(profile)
    trading_plan(profile)
    summary_display(profile)

    return profile


if __name__ == "__main__":

    print("=== Trading Assistant V1 ===\n")

    profile = setup_check()

    print("\nProfile Created Successfully!")
    print(profile)
