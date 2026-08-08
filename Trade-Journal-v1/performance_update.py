def performance_update(profile):
    """Saves the current journal entry to permanent history, then recomputes
    all aggregate statistics from scratch across the full history.
    """
    journal = profile["journal"]

    # Save the entry we just built into permanent history
    journal["entries"].append(journal["current_trade"])

    entries = journal["entries"]

    # Adherence stats: every entry with conditions checked counts, executed or not --
    # adherence measures analysis quality, separate from whether you pulled the trigger.
    adherence_entries = [e for e in entries if e.get("adherence", {}).get("applicable")]
    if adherence_entries:
        avg_adherence = round(
            sum(e["adherence"]["adherence_pct"] for e in adherence_entries) / len(adherence_entries),
            1
        )
        fully_adherent = sum(
            1 for e in adherence_entries
            if e["adherence"]["conditions_met"] == e["adherence"]["conditions_total"]
        )
    else:
        avg_adherence = 0.0
        fully_adherent = 0

    # P&L / win-rate stats: only trades actually executed count
    executed_entries = [e for e in entries if e.get("outcome", {}).get("applicable")]

    total_trades = len(executed_entries)
    wins = sum(1 for e in executed_entries if e["outcome"]["result"] == "Win")
    losses = sum(1 for e in executed_entries if e["outcome"]["result"] == "Loss")
    break_even = sum(1 for e in executed_entries if e["outcome"]["result"] == "Break-even")

    win_rate = round((wins / total_trades) * 100, 1) if total_trades else 0.0

    pnls = [e["outcome"]["pnl"] for e in executed_entries]
    gross_profit = round(sum(p for p in pnls if p > 0), 2)
    gross_loss = round(sum(-p for p in pnls if p < 0), 2)
    net_profit = round(gross_profit - gross_loss, 2)

    r_multiples = [e["outcome"]["r_multiple"] for e in executed_entries]
    average_rr = round(sum(r_multiples) / len(r_multiples), 2) if r_multiples else 0.0

    best_trade = round(max(pnls), 2) if pnls else 0.0
    worst_trade = round(min(pnls), 2) if pnls else 0.0

    # Streaks, computed in chronological order over executed trades only.
    # Break-even resets both streaks -- it's neither a win nor a loss.
    running_win = 0
    running_loss = 0
    best_win_streak = 0
    best_loss_streak = 0

    for e in executed_entries:
        result = e["outcome"]["result"]
        if result == "Win":
            running_win += 1
            running_loss = 0
        elif result == "Loss":
            running_loss += 1
            running_win = 0
        else:
            running_win = 0
            running_loss = 0

        best_win_streak = max(best_win_streak, running_win)
        best_loss_streak = max(best_loss_streak, running_loss)

    journal["statistics"] = {
        "total_trades": total_trades,
        "wins": wins,
        "losses": losses,
        "break_even": break_even,
        "win_rate": win_rate,
        "gross_profit": gross_profit,
        "gross_loss": gross_loss,
        "net_profit": net_profit,
        "average_rr": average_rr,
        "best_trade": best_trade,
        "worst_trade": worst_trade,
        "current_win_streak": running_win,
        "current_loss_streak": running_loss,
        "best_win_streak": best_win_streak,
        "best_loss_streak": best_loss_streak,
        "average_adherence_pct": avg_adherence,
        "fully_adherent_trades": fully_adherent
    }
