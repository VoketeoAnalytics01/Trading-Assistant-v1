def lessons_learned(profile):
    """Captures free-text reflection on the trade. At least one field must be filled --
    otherwise entries tend to end up completely blank and add nothing to review later.
    """
    print("\n=== Lessons Learned ===")

    while True:
        went_well = input("What went well?: ").strip()
        to_improve = input("What would you do differently next time?: ").strip()
        key_takeaway = input("One key takeaway from this trade: ").strip()

        if went_well or to_improve or key_takeaway:
            break
        print("\nAdd at least a quick note in one of these before moving on.\n")

    profile["journal"]["current_trade"]["lesson"] = {
        "went_well": went_well,
        "to_improve": to_improve,
        "key_takeaway": key_takeaway
    }
