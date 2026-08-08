def summary_display(profile):
    """Displays a clean, human-readable summary of the trader's profile."""
    trading = profile["trading"]
    plan = profile["trading_plan"]

    print("\n=== Trading Profile Summary ===")

    name_line = profile["username"]
    if profile.get("full_name"):
        name_line += f" ({profile['full_name']})"
    print(f"Trader: {name_line}")
    print(f"Account: {profile['account_type']}")

    print(f"\nStyle: {trading['style'] or '-'} | Experience: {trading['experience'] or '-'}")

    sessions = ", ".join(trading["sessions"]) if trading["sessions"] else "None selected"
    print(f"Sessions: {sessions}")

    markets = ", ".join(trading["markets"]) if trading["markets"] else "None selected"
    print(f"Markets: {markets}")

    assets = ", ".join(trading["assets"]) if trading["assets"] else "None selected"
    print(f"Assets: {assets}")

    conditions = plan["conditions"]
    print(f"\nTrading Plan ({plan['rules_count']} conditions, {plan['setup_threshold']}% threshold):")
    if conditions:
        for i, cond in enumerate(conditions, start=1):
            print(f"  {i}. {cond}")
    else:
        print("  No conditions recorded.")

    print("================================")
