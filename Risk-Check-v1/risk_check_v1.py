def risk_check(profile):

    # Create risk structure if it doesn't exist
    risk_profile(profile)

    # First-time setup only
    if not profile["risk"]["setup_complete"]:

        account_information(profile)
        risk_settings(profile)

        profile["risk"]["setup_complete"] = True

    # Reset current trade before each new analysis
    new_trade(profile)

    # Trade-specific inputs
    trade_calculator(profile)
    position_size(profile)

    # Validation
    risk_validation(profile)
    trade_checklist(profile)

    # Display results
    risk_summary_display(profile)

    return profile
