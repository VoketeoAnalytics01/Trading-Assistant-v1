import sys
from pathlib import Path


# ==============================
# PROJECT PATH
# ==============================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

sys.path.append(str(PROJECT_ROOT / "Risk-Check-v1"))
sys.path.append(str(PROJECT_ROOT / "Trade-Journal-v1"))
sys.path.append(str(PROJECT_ROOT / "Shared"))


# ==============================
# MODULE IMPORTS
# ==============================

from Risk_Check_v1 import risk_check
from Trade_Journal_v1 import trade_journal
from profile_manager import save_profile


# ==============================
# PROFILE STRUCTURE
# ==============================

def ensure_trading_structure(profile):
    """Ensure required trading profile fields exist."""

    if "trading" not in profile:
        profile["trading"] = {}

    trading = profile["trading"]

    if "assets" not in trading:
        trading["assets"] = []

    if "markets" not in trading:
        trading["markets"] = []

    if "sessions" not in trading:
        trading["sessions"] = []

    if "style" not in trading:
        trading["style"] = "N/A"

    if "experience" not in trading:
        trading["experience"] = "N/A"

    return profile


# ==============================
# TRADING PROFILE DISPLAY
# ==============================

def display_trading_profile(profile):
    """Display the user's current trading profile."""

    trading = profile.get("trading", {})

    print("\n========================================")
    print("          TRADING PROFILE")
    print("========================================")

    print("\n--- User Information ---")
    print(f"Username    : {profile.get('username', 'N/A')}")
    print(f"Full Name   : {profile.get('full_name', 'N/A')}")
    print(f"Account     : {profile.get('account_type', 'N/A')}")

    print("\n--- Trading Information ---")
    print(f"Style       : {trading.get('style', 'N/A')}")
    print(f"Experience  : {trading.get('experience', 'N/A')}")

    print("\n--- Trading Preferences ---")

    sessions = trading.get("sessions", [])
    markets = trading.get("markets", [])
    assets = trading.get("assets", [])

    print(f"Sessions    : {', '.join(sessions) if sessions else 'None'}")
    print(f"Markets     : {', '.join(markets) if markets else 'None'}")
    print(f"Assets      : {', '.join(assets) if assets else 'None'}")

    print("\n========================================")


# ==============================
# MAIN DASHBOARD
# ==============================

def main_dashboard(profile):

    # Make sure profile has the required structure.
    profile = ensure_trading_structure(profile)

    username = profile.get("username", "Trader")
    account_type = profile.get("account_type", "Free")
    early_access = profile.get("early_access", False)

    while True:

        print("\n========================================")
        print("       TRADING ASSISTANT V1 BETA")
        print("========================================")

        print(f"Welcome, {username}")
        print(f"Account: {account_type}")

        print("\n[1] Trading Profile")
        print("[2] Risk Check")
        print("[3] Trade Journal")
        print("[4] My Playbook")
        print("[5] Analytics (Coming Soon)")

        if early_access:
            print("[6] AI Trading Assistant")
        else:
            print("[6] AI Trading Assistant (Early Access)")

        print("[7] Settings")
        print("[8] Exit")

        choice = input("\nSelect an option: ").strip()

        # ==============================
        # TRADING PROFILE
        # ==============================

        if choice == "1":

            display_trading_profile(profile)

        # ==============================
        # RISK CHECK
        # ==============================

        elif choice == "2":

            print("\n=== Opening Risk Check ===")

            profile = risk_check(profile)

            save_profile(username, profile)

        # ==============================
        # TRADE JOURNAL
        # ==============================

        elif choice == "3":

            print("\n=== Opening Trade Journal ===")

            profile = trade_journal(profile)

            save_profile(username, profile)

        # ==============================
        # PLAYBOOK
        # ==============================

        elif choice == "4":

            print("\n=== My Playbook ===")
            print("Playbook module is coming soon.")

        # ==============================
        # ANALYTICS
        # ==============================

        elif choice == "5":

            print("\n=== Analytics ===")
            print("Analytics module is coming soon.")

        # ==============================
        # AI ASSISTANT
        # ==============================

        elif choice == "6":

            print("\n=== AI Trading Assistant ===")

            if early_access:

                print("AI Trading Assistant is in active development.")
                print("Early-access features will appear here.")

            else:

                print(
                    "This feature is reserved for early-access members."
                )
                print(
                    "More information will be available before full release."
                )

        # ==============================
        # SETTINGS
        # ==============================

        elif choice == "7":

            print("\n=== Settings ===")
            print("Settings module is coming soon.")

        # ==============================
        # EXIT
        # ==============================

        elif choice == "8":

            save_profile(username, profile)

            print("\nExiting Trading Assistant...")
            break

        # ==============================
        # INVALID OPTION
        # ==============================

        else:

            print("\nInvalid option. Please select 1-8.")

    return profile


# ==============================
# STANDALONE TEST
# ==============================

if __name__ == "__main__":

    print("=== Main Dashboard Standalone Test ===\n")

    test_profile = {
        "username": "Teo",
        "full_name": "Test User",
        "account_type": "Free",
        "early_access": False,
        "trading": {
            "style": "Scalping",
            "experience": "Beginner",
            "sessions": ["New York Session"],
            "markets": ["Options"],
            "assets": ["Stock Options"]
        }
    }

    main_dashboard(test_profile)
