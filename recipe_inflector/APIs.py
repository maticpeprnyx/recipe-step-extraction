import requests
import conllu.models
from conllu import parse
import json

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
    response: list[list[str]] = requests.get(api_url).json()["vertical"]
    return response


def brno_inflector(text: str, inflective_tags: str) -> dict:
    """
    Calls the NLP Centre's inflector API on input text and tags.
    """
    api_url: str = "https://nlp.fi.muni.cz/languageservices/service.py?call=inflection&lang=cs&output=json&text=" + text + "&tag=" + inflective_tags
    response: dict = requests.get(api_url).json()
    return response

def inflected_verb(lemma: str, inflective_tags: str) -> str:
    response = brno_inflector(lemma, inflective_tags)
    if is_inflected(response):
        inflected_token = response[0]['Lemma'][0]['Word']
        return inflected_token
    else:
        return ""

def get_lemma_list(inflector_output: dict) -> list[dict]:
    """
    Returns the first item of the lemma list in the inflector API output.
    """
    return inflector_output[0].get('Lemma')


def is_inflected(inflector_output: dict) -> bool:
    """
    Returns True if the inflector API output is not empty.
    """
    return inflector_output[0].get('Lemma') != []
