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

    journal_profile(profile)
    new_entry(profile)

    trade_information(profile)
    trade_execution(profile)
    trade_outcome(profile)
    psychology(profile)
    lessons_learned(profile)
    screenshots(profile)

    journal_validation(profile)
    performance_update(profile)

    journal_summary_display(profile)

    return profile

if __name__ == "__main__":
    print("=== Trade Journal V1 ===\n")
    # Placeholder profile for standalone testing.
    # In the real app, this same shared profile comes from Setup-Check + Risk-Check.
    profile = {"username": "Teo"}
    trade_journal(profile)

