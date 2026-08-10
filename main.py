import sys
from pathlib import Path


# ==============================
# PROJECT PATH
# ==============================

PROJECT_ROOT = Path(__file__).resolve().parent

sys.path.append(str(PROJECT_ROOT / "Login-System-v1"))
sys.path.append(str(PROJECT_ROOT / "Setup-Check-v1"))
sys.path.append(str(PROJECT_ROOT / "Risk-Check-v1"))
sys.path.append(str(PROJECT_ROOT / "Trade-Journal-v1"))
sys.path.append(str(PROJECT_ROOT / "Shared"))


# ==============================
# MODULE IMPORTS
# ==============================

from login_system_v1 import login_system
from Setup_Check_v1 import setup_check
from main_dashboard import main_dashboard

from profile_manager import (
    load_profile,
    save_profile,
    profile_exists
)


# ==============================
# APPLICATION START
# ==============================

print("=== Trading Assistant V1 Beta ===\n")


# ==============================
# AUTHENTICATION
# ==============================

username = login_system()

if not username:

    print("\nAuthentication failed.")
    print("Returning to login menu.")

    sys.exit()


print(f"\nAuthenticated user: {username}")


# ==============================
# TRADING PROFILE
# ==============================

if profile_exists(username):

    print("\nExisting trading profile found.")

    profile = load_profile(username)

else:

    print("\nNo trading profile found.")
    print("Let's create your Trading Profile.\n")

    profile = setup_check(username)

    save_profile(username, profile)

    print("\nTrading profile saved successfully.")


# ==============================
# MAIN DASHBOARD
# ==============================

profile = main_dashboard(profile)


# ==============================
# FINAL SAVE
# ==============================

save_profile(username, profile)


# ==============================
# SESSION COMPLETE
# ==============================

print("\n========================================")
print("   TRADING ASSISTANT V1 SESSION COMPLETE")
print("========================================")
