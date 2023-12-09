from pathlib import Path

def open_folder(folder_name: str) -> list[str]:
    """
    Reads the contents of all files in 'folder_name'. 
    Each file is loaded as a single continuous string and is an entry in the output list.
    """
    source_dir = Path(folder_name)
    filepaths = source_dir.iterdir()

    contents_of_files: list[str] = list()

    for filepath in filepaths:
        contents_of_files.append(open_bare(str(filepath)))
    
    return contents_of_files

def open_bare(file_name: str) -> str:
    """
    Reads the contents of the file 'file_name' as a single continuous string.
    """
    with open(file_name, "r", encoding="utf8") as f:
        file_contents = f.read()
    return file_contents


def open_lines(file_name: str) -> list[str]:
    """
    Reads the contents of the file 'file_name' line by line. Returns a line list (i.e. a list of strings).
    """
    with open(file_name, "r", encoding="utf8") as f:
        file_contents = f.readlines()
    return file_contents


def open_tokens(file_name: str) -> list[str]:
    """
    Reads the contents of the file 'file_name' as a list of words/tokens. It only crudely splits after spaces.
    """
    tokens: list[str] = list()
    with open(file_name, "r", encoding="utf8") as f: #open the file
        for line in f.readlines():
            tokens += line.split() #put the lines to a variable (list).
    return tokens