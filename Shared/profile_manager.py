import json
from pathlib import Path


# Project root:
# ~/Trade-Assistant-v1/
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Profile storage:
# ~/Trade-Assistant-v1/Data/profiles/
PROFILES_DIR = PROJECT_ROOT / "Data" / "profiles"


def _ensure_profiles_directory():
    """Create the profiles directory if it does not exist."""
    PROFILES_DIR.mkdir(parents=True, exist_ok=True)


def _profile_path(username):
    """Return the JSON path for a user's profile."""
    safe_username = username.strip()

    if not safe_username:
        raise ValueError("Username cannot be empty.")

    return PROFILES_DIR / f"{safe_username}.json"


def profile_exists(username):
    """Check whether a saved profile exists for the username."""
    return _profile_path(username).exists()


def save_profile(username, profile):
    """Save a user's complete profile as JSON."""
    _ensure_profiles_directory()

    path = _profile_path(username)

    with path.open("w", encoding="utf-8") as file:
        json.dump(profile, file, indent=4, ensure_ascii=False)

    return True


def load_profile(username):
    """
    Load a user's profile.

    Returns:
        dict: Existing profile.

    Raises:
        FileNotFoundError: If the profile does not exist.
    """
    path = _profile_path(username)

    if not path.exists():
        raise FileNotFoundError(
            f"No profile found for username '{username}'."
        )

    with path.open("r", encoding="utf-8") as file:
        profile = json.load(file)

    return profile


def delete_profile(username):
    """Delete a user's saved profile."""
    path = _profile_path(username)

    if path.exists():
        path.unlink()
        return True

    return False
