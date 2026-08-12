# ==============================
# TRADE JOURNAL V1
# ==============================

from journal_profile import journal_profile
from new_entry import new_entry
from trade_information import trade_information
from trade_execution import trade_execution
from trade_outcome import trade_outcome
from psychology import psychology
from lessons_learned import lessons_learned
from screenshots import screenshots
from journal_validation import journal_validation
from performance_update import performance_update
from journal_summary_display import journal_summary_display


def trade_journal(profile):
    """
    Main Trade Journal V1 workflow.

    All journal modules operate on the same shared profile.
    The profile is returned after the complete journal workflow.
    """

    # ==============================
    # JOURNAL PROFILE
    # ==============================

    journal_profile(profile)

    # ==============================
    # NEW JOURNAL ENTRY
    # ==============================

    new_entry(profile)

    # ==============================
    # TRADE INFORMATION
    # ==============================

    trade_information(profile)

    # ==============================
    # TRADE EXECUTION
    # ==============================

    trade_execution(profile)

    # ==============================
    # TRADE OUTCOME
    # ==============================

    trade_outcome(profile)

    # ==============================
    # TRADER PSYCHOLOGY
    # ==============================

    psychology(profile)

    # ==============================
    # LESSONS LEARNED
    # ==============================

    lessons_learned(profile)

    # ==============================
    # SCREENSHOTS
    # ==============================

    screenshots(profile)

    # ==============================
    # JOURNAL VALIDATION
    # ==============================

    journal_validation(profile)

    # ==============================
    # PERFORMANCE UPDATE
    # ==============================

    performance_update(profile)

    # ==============================
    # JOURNAL SUMMARY
    # ==============================

    journal_summary_display(profile)

    return profile


# ==============================
# STANDALONE TEST
# ==============================

if __name__ == "__main__":

    print("=== Trade Journal V1 ===\n")

    profile = {
        "username": "Teo",
        "account_type": "Free",
        "trading": {
            "assets": [],
            "markets": [],
            "sessions": [],
            "style": "N/A",
            "experience": "N/A"
        }
    }

    trade_journal(profile)
