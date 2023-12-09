import requests
from open_file import open_bare
from conllu import parse_tree, parse
from conllu.models import TokenList, Token, SentenceList
import sys

def get_conllu(data: str) -> str:
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

def get_tree_list(data: str):
    vertical = get_conllu(data)
    trees = parse_tree(vertical)
    return trees

def get_sentence_list(data: str) -> SentenceList:
    vertical = get_conllu(data)
    sentences = parse(vertical)
    return sentences

if __name__ == "__main__":
    path = sys.argv[1]
    data: str = open_bare(path)
    conllu: str = get_conllu(data)
    print(conllu)