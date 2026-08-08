def journal_summary_display(profile):
    """Displays a clean, human-readable summary of the journal entry just logged,
    plus a quick snapshot of updated aggregate stats.
    """
    trade = profile["journal"]["current_trade"]
    stats = profile["journal"]["statistics"]

    print("\n=== Journal Entry Summary ===")

    info = trade.get("trade_info", {})
    print(f"\n{info.get('symbol', '-')} | {info.get('market', '-')} | {info.get('session', '-')} | {info.get('direction', '-')}")
    print(f"Date: {info.get('date', '-')}")

    execution = trade.get("execution", {})
    if execution.get("executed"):
        planned = execution.get("planned", {})
        actual = execution.get("actual", {})
        if planned.get("entry_price"):
            print(f"\nExecuted at {actual.get('entry_price', '-')} (planned {planned['entry_price']}, slippage {actual.get('slippage', 0)})")
        else:
            print(f"\nExecuted at {actual.get('entry_price', '-')}")
    else:
        print(f"\nNot executed -- {execution.get('not_executed_reason', '-')}")
        if execution.get("not_executed_note"):
            print(f"  Note: {execution['not_executed_note']}")

    outcome = trade.get("outcome", {})
    if outcome.get("applicable"):
        print(f"\nResult: {outcome['result']} | P&L: {outcome['pnl']} | R: {outcome['r_multiple']}")

    psychology = trade.get("psychology", [])
    print(f"\nEmotions: {', '.join(psychology) if psychology else 'None recorded'}")

    lesson = trade.get("lesson", {})
    lesson_lines = [f"  {label}: {text}" for label, text in [
        ("Went well", lesson.get("went_well")),
        ("To improve", lesson.get("to_improve")),
        ("Takeaway", lesson.get("key_takeaway"))
    ] if text]
    if lesson_lines:
        print("\nLessons:")
        print("\n".join(lesson_lines))

    screenshots = trade.get("screenshots", [])
    if screenshots:
        print(f"\nScreenshots ({len(screenshots)}):")
        for s in screenshots:
            print(f"  - {s['description']}")

    adherence = trade.get("adherence", {})
    if adherence.get("applicable"):
        print(f"\nAdherence: {adherence['conditions_met']}/{adherence['conditions_total']} ({adherence['adherence_pct']}%)")
        if adherence.get("warnings"):
            print("  Not followed:")
            for w in adherence["warnings"]:
                print(f"    - {w}")

    print("\n--- Overall Stats ---")
    print(f"Total trades: {stats['total_trades']} | Win rate: {stats['win_rate']}% | Net P&L: {stats['net_profit']}")
    print(f"Avg adherence: {stats['average_adherence_pct']}% | Entries logged: {len(profile['journal']['entries'])}")
    print("================================")
