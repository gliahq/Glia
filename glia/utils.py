from pathlib import Path

from glia.definitions import ROOT_DIR


def get_theme_contents(theme, file: str) -> str:
    """
    :param theme: Name of theme
    :param file: File in theme folder
    :return: Contents as str
    """
    with open(Path(ROOT_DIR, f"resources/themes/{theme}/{file}")) as f:
        return f.read()
