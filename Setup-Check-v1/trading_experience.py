def trading_experience(profile):
    """Prompts for trader experience level from a fixed menu."""
    experience_levels = {
        "1": "Beginner",
        "2": "Intermediate",
        "3": "Advanced",
        "4": "Professional"
    }
    print("\nExperience Level:")
    for key, value in experience_levels.items():
        print(f"  {key}. {value}")

    while True:
        choice = input("Select 1-4: ").strip()
        if choice in experience_levels:
            profile["trading"]["experience"] = experience_levels[choice]
            break
        print("Invalid choice. Please select between 1 and 4.")
