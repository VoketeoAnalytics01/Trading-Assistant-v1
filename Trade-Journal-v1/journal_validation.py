def screenshots(profile):
    """Attaches optional chart screenshots to the journal entry: file path + required description.
    AI-generated descriptions are reserved for premium (per the original spec) -- not built yet,
    just leaving the field in place so that feature has somewhere to land later.
    """
    print("\n=== Screenshots ===")

    entries = []

    while True:
        add = input("Add a screenshot? (y/n): ").strip().lower()
        if add != "y":
            break

        while True:
            path = input("File path (e.g. /sdcard/Pictures/chart1.png): ").strip()
            if path:
                break
            print("File path can't be empty.")

        while True:
            description = input("Brief description of this screenshot: ").strip()
            if description:
                break
            print("A description is required.")

        entries.append({
            "path": path,
            "description": description,
            "ai_description": None
        })
        print(f"✓ Screenshot added ({len(entries)} total).")

    profile["journal"]["current_trade"]["screenshots"] = entries
