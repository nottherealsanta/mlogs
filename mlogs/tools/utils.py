from pathlib import Path

# get project root
def get_project_root() -> Path:
    """Returns project root folder."""
    return Path(__file__).parent.parent.parent
