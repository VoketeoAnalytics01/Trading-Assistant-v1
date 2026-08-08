def psychology(profile):
    """Captures the trader's emotional state during the trade (multi-select).
    Runs regardless of whether the trade was executed -- emotions around
    NOT taking a trade are just as relevant as emotions during one.
    """
    print("\n=== Psychology ===")

    emotions = {
        "1": "Confident",
        "2": "Calm / Disciplined",
        "3": "Anxious / Nervous",
        "4": "Fear",
        "5": "Greed",
        "6": "FOMO",
        "7": "Revenge Trading",
        "8": "Impatient",
        "9": "Hesitant",
        "10": "Overconfident",
        "11": "Bored",
        "12": "Frustrated"
    }

    selected = []

    while True:
        print("\nHow did you feel around this trade?")
        for key, val in emotions.items():
            marker = " (selected)" if val in selected else ""
            print(f"  {key}. {val}{marker}")
        print("  0. Done")

        choice = input("Select emotion: ").strip()

        if choice == "0":
            if selected:
                break
            print("Select at least one before finishing.")
            continue

        if choice in emotions:
            emotion = emotions[choice]
            if emotion not in selected:
                selected.append(emotion)
                print(f"✓ {emotion} added.")
            else:
                print("Already selected.")
        else:
            print("Invalid choice.")

    profile["journal"]["current_trade"]["psychology"] = selected
