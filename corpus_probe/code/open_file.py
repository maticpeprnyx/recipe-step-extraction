from pathlib import Path

def open_folder(folder_name: str) -> list[str]:
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
    with open(file_name, 'r', encoding="utf8") as f: #open the file
        file_contents = f.read() #put the lines to a variable (list).
    return file_contents


def open_lines(file_name: str) -> list[str]:
    """
    Načte obsah souboru 'file_name' řádek po řádku. Vrací seznam řádku (tj. seznam řetězců).
    """
    with open(file_name, 'r', encoding="utf8") as f: #open the file
        file_contents = f.readlines() #put the lines to a variable (list).
    return file_contents


def open_tokens(file_name: str) -> list[str]:
    """
    Načte obsah souboru 'file_name' jako seznam slov/tokenů. Prostě a sprostě dělí po mezerách.
    """
    tokens: list[str] = list()
    with open(file_name, 'r', encoding="utf8") as f: #open the file
        for line in f.readlines():
            tokens += line.split() #put the lines to a variable (list).
    return tokens 
