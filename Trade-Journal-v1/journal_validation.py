def journal_validation(profile):
    """Checks this trade against the trader's own stated conditions from Setup-Check,
    producing a per-condition adherence score. This is the core metric the whole
    app is built around -- consistency of execution, not just win/loss.
    """
    print("\n=== Plan Adherence ===")

    conditions = profile.get("trading_plan", {}).get("conditions", [])

    if not conditions:
        print("No trading plan conditions found -- skipping adherence check.")
        profile["journal"]["current_trade"]["adherence"] = {
            "applicable": False,
            "results": [],
            "conditions_met": 0,
            "conditions_total": 0,
            "adherence_pct": 0.0,
            "warnings": []
        }
        return

    print("For each condition from your trading plan, did you follow it on this trade?\n")

    results = []
    warnings = []

    for condition in conditions:
        while True:
            answer = input(f'"{condition}" -- followed? (y/n): ').strip().lower()
            if answer in ("y", "n"):
                break
            print("Please enter y or n.")

        followed = (answer == "y")
        results.append({"condition": condition, "followed": followed})
        if not followed:
            warnings.append(condition)

    conditions_met = sum(1 for r in results if r["followed"])
    conditions_total = len(results)
    adherence_pct = round((conditions_met / conditions_total) * 100, 1)

    profile["journal"]["current_trade"]["adherence"] = {
        "applicable": True,
        "results": results,
        "conditions_met": conditions_met,
        "conditions_total": conditions_total,
        "adherence_pct": adherence_pct,
        "warnings": warnings
    }

    print(f"\nAdherence: {conditions_met}/{conditions_total} conditions followed ({adherence_pct}%)")
    if warnings:
        print("Not followed:")
        for w in warnings:
            print(f"  - {w}")
