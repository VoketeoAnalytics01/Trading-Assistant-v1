def load_profile(username):
    """
    Load a user's profile.

    Returns:
        dict: Existing profile.

    Raises:
        FileNotFoundError: If the profile does not exist.
        json.JSONDecodeError: If the profile file exists but is corrupted.
            The corrupted file is backed up (renamed with a .corrupted suffix)
            before the error is raised, so no data is silently lost.
    """
    path = _profile_path(username)

    if not path.exists():
        raise FileNotFoundError(f"No profile found for username '{username}'.")

    with path.open("r", encoding="utf-8") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            backup_path = path.with_suffix(".json.corrupted")
            path.replace(backup_path)
            print(f"(Corrupted profile backed up to {backup_path.name})")
            raise
