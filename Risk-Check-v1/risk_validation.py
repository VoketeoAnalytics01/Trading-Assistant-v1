def risk_validation(profile):

    print("\n=== Risk Validation ===")

    trade = profile["risk"]["current_trade"]
    settings = profile["risk"]["settings"]
    validation = profile["risk"]["validation"]

    # Reset previous results
    validation["warnings"] = []
    validation["errors"] = []
    validation["approved"] = False

    # -------- Entry / Stop Loss --------
    if trade["entry"] == trade["stop_loss"]:
        validation["errors"].append(
            "Entry price and Stop Loss cannot be the same."
        )

    # -------- Position Size --------
    if trade["position_size"] <= 0:
        validation["errors"].append(
            "Position size must be greater than zero."
        )

    # -------- Risk Amount --------
    if trade["risk_amount"] <= 0:
        validation["errors"].append(
            "Risk amount must be greater than zero."
        )

    # -------- Risk : Reward --------
    if trade["rr"] < settings["minimum_rr"]:
        validation["warnings"].append(
            f"Risk:Reward ({trade['rr']:.2f}) is below your minimum "
            f"({settings['minimum_rr']:.2f})."
        )

    # -------- Daily Loss Limit --------
    if trade["risk_amount"] > settings["daily_loss_limit"]:
        validation["warnings"].append(
            "Risk exceeds your daily loss limit."
        )

    # -------- Weekly Loss Limit --------
    if trade["risk_amount"] > settings["weekly_loss_limit"]:
        validation["warnings"].append(
            "Risk exceeds your weekly loss limit."
        )

    # -------- Final Decision --------
    if len(validation["errors"]) == 0:

        validation["approved"] = True
        trade["status"] = "Approved"

        print("\n✓ Trade Approved")

        if validation["warnings"]:
            print("\nWarnings:")
            for warning in validation["warnings"]:
                print(f"- {warning}")

    else:

        trade["status"] = "Rejected"

        print("\n✗ Trade Rejected")

        print("\nErrors:")
        for error in validation["errors"]:
            print(f"- {error}")

        if validation["warnings"]:
            print("\nWarnings:")
            for warning in validation["warnings"]:
                print(f"- {warning}")

    return profile
