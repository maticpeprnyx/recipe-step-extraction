from pathlib import Path
import os

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
    Načte obsah souboru 'file_name' jako jeden řetězec.
    """
    with open(file_name, 'r', encoding="utf8") as f:
        file_contents = f.read()
    return file_contents


def open_lines(file_name: str) -> list[str]:
    """
    Načte obsah souboru 'file_name' řádek po řádku. Vrací seznam řádku (tj. seznam řetězců).
    """
    with open(file_name, 'r', encoding="utf8") as f:
        file_contents = f.readlines()
    return file_contents


def open_tokens(file_name: str) -> list[str]:
    """
    Načte obsah souboru 'file_name' jako seznam slov/tokenů. Prostě a sprostě dělí po mezerách.
    """
    tokens: list[str] = list()
    with open(file_name, 'r', encoding="utf8") as f:
        for line in f.readlines():
            tokens += line.split()
    return tokens 

def listdir_fullpath(d):
    return [(f, os.path.join(d, f)) for f in os.listdir(d)]
