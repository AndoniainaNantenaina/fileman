import os
import glob


def f_extension(file: str) -> str:
    """
    Get the extension of a file.

    Args:
        file (str): The file name.

    Returns:
        extension (str): The extension of the file.
    """
    return file.split(".")[-1]


def f_name(file: str) -> str:
    """
    Get the name of a file.

    Args:
        file (str): The file name.

    Returns:
        name (str): The name of the file.
    """
    return file.split(".")[0]


def exists(file: str) -> bool:
    """
    Check if a file exists.

    Args:
        file (str): The file name.

    Returns:
        exists (bool): True if the file exists, False otherwise.
    """
    if os.path.isfile(file):
        return True

    return False


def by_ext(ext: str, folder: str) -> list:
    """
    Get all files with a specific extension.

    Args:
        ext (str): The extension of the files to get.
        folder (str): The folder where the files are located

    Returns:
        files (list): The list of files with the specified extension.
    """
    files = []

    files = glob.glob(pathname=os.path.join(folder, f"*.{ext}"))

    return files
