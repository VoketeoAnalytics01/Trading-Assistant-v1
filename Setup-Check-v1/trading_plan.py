def trading_plan(profile):
    """Collects at least 3 trading conditions/rules, then lets the user optionally add more."""
    print("\nTrading Plan - Conditions")
    print("Enter the specific conditions/rules you use when trading.")
    print("You need at least 3.\n")

    conditions = []

    # mandatory first 3 -- no exit possible until this is satisfied
    while len(conditions) < 3:
        condition = input(f"Condition #{len(conditions) + 1}: ").strip()
        if not condition:
            print("Condition can't be empty.")
            continue
        conditions.append(condition)

    # optional additional conditions, asked explicitly instead of via a keyword
    while True:
        add_more = input("Add another condition? (y/n): ").strip().lower()
        if add_more != "y":
            break
        condition = input(f"Condition #{len(conditions) + 1}: ").strip()
        if not condition:
            print("Condition can't be empty.")
            continue
        conditions.append(condition)

    profile["trading_plan"]["conditions"] = conditions
    profile["trading_plan"]["rules_count"] = len(conditions)
    profile["trading_plan"]["minimum_conditions"] = 3


