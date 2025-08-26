import os


def get_asset_path(relative_path: str) -> str:
    """Return absolute path to asset within the installed package.

    Works when running from source and when installed as a package.
    """
    base_dir = os.path.dirname(__file__)
    return os.path.join(base_dir, relative_path)


