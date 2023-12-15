import requests
from open_file import open_bare, listdir_fullpath
from APIs import brno_tagger
import sys
import time

def error(error_msg: str):
    """
    Prints a specified error message to stderr.
    """
    print(error_msg, file=sys.stderr)

def get_conllu(data: str) -> str:
    # De facto je to stejná funkce jako 'get_sentence_list' v 'parse_text.py'. Nepřetváří ale získaný vertikál z řetězce na nějakou strukturu, to dělají až obalující funkce. 
    parameters: dict[str, str] = {"data": data,
                                  "input": "horizontal",
                                  "model": "czech-pdt-ud-2.12-230717",
                                  "tokenizer": "normalized_spaces",
                                  "tagger": "",
                                  "parser": "",
                                  "output": "conllu"}
    api_url: str = "https://lindat.mff.cuni.cz/services/udpipe/api/process"
    response: str = requests.get(api_url, params=parameters).json()["result"]
    return response

def main():
    input_folder_path: str = sys.argv[1]
    output_folder_path: str = sys.argv[2]
    for short_filename, long_filename in listdir_fullpath(input_folder_path):
        output_filename = output_folder_path + short_filename
        sys.stdout = open(output_filename, "wt")
        
        # print(f"{short_filename}\t{long_filename}\t{output_filename}")
        
        data: str = open_bare(long_filename)
        vertical = brno_tagger(data)
        time.sleep(3)
        if vertical == None:
            error(f"Error: Server did not return a vertical for the file {long_filename}.")
            return 1
        else:
            for line in vertical:
                for item in line:
                    print(item, end="\t")
                print()
            
    return 0

if __name__ == "__main__":
    main()