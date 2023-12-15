import requests
import conllu.models
from conllu import parse

def udpipe_parser(text: str) -> list[conllu.models.TokenList]:
    """
    Calls the UDPipe REST API on input text.
    Takes plain Czech text and returns CoNLL-U format, i.e. performs
    morphological analysis, lemmatization and dependency parsing.
    Returns a list of TokenLists, each representing a sentence.
    Parse imported from conllu. https://pypi.org/project/conllu/
    """
    parameters: dict[str, str] = {"data": text,
                                  "model": "czech-cltt-ud-2.12-230717",                                  
                                  "input": "horizontal",
                                  "tokenizer": "normalized_spaces",
                                  "tagger": "",
                                  "parser": "",
                                  "output": "conllu"}
    api_url: str = "https://lindat.mff.cuni.cz/services/udpipe/api/process"
    response: str = requests.get(api_url, params=parameters).json()["result"]
    udpipe_parsed_sentences: list[conllu.models.TokenList] = parse(response)
    return udpipe_parsed_sentences

def brno_tagger(text: str) -> list[list[str]]:
    """
    Calls the NLP Centre's tagger API on input text. 
    Takes plain Czech text and returns a list of lists with word forms, lemmas and tags.
    Segments and marks sentence boundaries with <s> and </s> tags and
    puts a <g/> (glue) tag before directly adjacent punctuation.
    """
    api_url: str = "https://nlp.fi.muni.cz/languageservices/service.py?call=tagger&lang=cs&output=json&text=" + text
    response = requests.get(api_url).json()
    if "vertical" in response:
        vertical = response["vertical"]
        return vertical
    else:
        return None
