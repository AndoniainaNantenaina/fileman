class File:
    def __init__(self, file: str):
        if file == "":
            raise ValueError("File name cannot be empty")

class Folder:
    def __init__(self, folder: str | list[str]) -> None:
        """
        Create folder object.

        Params:
            folder (str | list[str]): Folder path or list of folder paths.
        """
        if type(folder) == list[str]:
            self.fd = folder
        else:
            self.fd = [folder]
            
    def files(self, rec: bool = False, ext: str = "") -> list[str]:
        """
        Return list of files in folder.

        Params:
            rec (bool): Recursive, if True, return files in subfolders (default: False).
            ext (str): File extension to filter files (empty by default).

        Returns:
            list[str]: List of files complete path in the main folder
        """
        return []
