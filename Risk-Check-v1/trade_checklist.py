def trade_checklist(profile):

    print("\n=== Trade Checklist ===")

    conditions = profile["trading_plan"]["conditions"]
    threshold = profile["trading_plan"]["setup_threshold"]

    checklist = {
        "answers": {},
        "conditions_met": 0,
        "total_conditions": len(conditions),
        "setup_score": 0.0,
        "passed": False
    }

    print("\nConfirm each trading condition (y/n):\n")

    for condition in conditions:

        while True:

            answer = input(f"{condition}? (y/n): ").strip().lower()

            if answer in ("y", "n"):
                break

            print("Invalid input. Please enter y or n.")

        confirmed = (answer == "y")

        checklist["answers"][condition] = confirmed

        if confirmed:
            checklist["conditions_met"] += 1

    # Calculate setup score
    if checklist["total_conditions"] > 0:

        checklist["setup_score"] = round(
            (checklist["conditions_met"] /
             checklist["total_conditions"]) * 100,
            2
        )

    # Determine if checklist passes
    checklist["passed"] = (
        checklist["setup_score"] >= threshold
    )

    # Store results
    profile["risk"]["checklist"] = checklist

    print("\n========== Checklist Summary ==========")
    print(f"Conditions Met : {checklist['conditions_met']}/{checklist['total_conditions']}")
    print(f"Setup Score    : {checklist['setup_score']}%")
    print(f"Threshold      : {threshold}%")

    if checklist["passed"]:
        print("Status         : ✓ PASSED")
    else:
        print("Status         : ✗ FAILED")

    print("=======================================\n")

    return profile
