def trade_summary_display(profile):

    print("\n")
    print("=" * 50)
    print("          RISK CHECK SUMMARY")
    print("=" * 50)

    # ----------------------------------------
    # Trader Information
    # ----------------------------------------

    print("\nTRADER")

    print(f"Username      : {profile['username']}")

    account = profile["risk"]["account"]

    print(f"Account Type  : {account['account_type']}")
    print(f"Broker        : {account['broker']}")
    print(f"Balance       : {account['currency']} {account['balance']:.2f}")

    # ----------------------------------------
    # Trade Information
    # ----------------------------------------

    trade = profile["risk"]["current_trade"]

    print("\nTRADE")

    print(f"Market        : {trade['market']}")
    print(f"Asset         : {trade['asset']}")
    print(f"Direction     : {trade['direction']}")

    print(f"Entry         : {trade['entry']}")
    print(f"Stop Loss     : {trade['stop_loss']}")
    print(f"Take Profit   : {trade['take_profit']}")

    # ----------------------------------------
    # Risk Metrics
    # ----------------------------------------

    print("\nRISK METRICS")

    print(f"Risk Amount   : ${trade['risk_amount']}")
    print(f"Position Size : {trade['position_size']}")
    print(f"Risk : Reward : 1 : {trade['rr']}")

    # ----------------------------------------
    # Validation
    # ----------------------------------------

    validation = profile["risk"]["validation"]

    print("\nVALIDATION")

    if validation["approved"]:
        print("Status        : APPROVED")
    else:
        print("Status        : REJECTED")

    if validation["errors"]:

        print("\nErrors:")

        for error in validation["errors"]:
            print(f"  • {error}")

    if validation["warnings"]:

        print("\nWarnings:")

        for warning in validation["warnings"]:
            print(f"  • {warning}")

    if not validation["errors"] and not validation["warnings"]:
        print("No errors or warnings.")

    # ----------------------------------------
    # Trade Checklist
    # ----------------------------------------

    checklist = profile["risk"]["checklist"]

    print("\nTRADE CHECKLIST")

    print(
        f"Conditions Met : "
        f"{checklist['conditions_met']} / {checklist['total_conditions']}"
    )

    print(
        f"Setup Score    : "
        f"{checklist['setup_score']}%"
    )

    if checklist["passed"]:
        print("Checklist      : PASSED")
    else:
        print("Checklist      : FAILED")

    # ----------------------------------------
    # Final Decision
    # ----------------------------------------

    print("\nFINAL DECISION")

    if validation["approved"] and checklist["passed"]:

        print("READY TO EXECUTE TRADE")
        print("Your trade satisfies your risk rules and trading plan.")

    elif validation["approved"]:

        print("USE CAUTION")
        print("Risk rules passed, but your trading checklist failed.")

    else:

        print("DO NOT EXECUTE")
        print("Trade failed risk validation.")

    print("\n" + "=" * 50)

    return profile
