# Run like this:
# python transform_text.py /path/to/recipe_in_paintext.txt 'nP,mR,p2,eA'
#                                                           ^ list of comma separated tag-values (see https://nlp.fi.muni.cz/languageservices/)
import sys
from open_file import open_bare
from APIs import brno_tagger
from tag import is_structural
from verb_tags import get_action_verb_tags, transform_verbs_in_vertical

def linearize_vertical(vertical: list[list[str]]) -> str:
    """
    Creates plain text, i.e. a a single continuous string, from a vertical.
    """
    output_text: list = list()
    for token in vertical:
        if not is_structural(token):    # get rid of structural tokens
            output_text.append(token[0])

    output_string = " ".join(output_text)
    # Could work with glue, this is way easier
    output_string = output_string.replace(" ,", ",")
    output_string = output_string.replace(" .", ".")
    output_string = output_string.replace(" ?", "?")
    output_string = output_string.replace(" !", "!")
    output_string = output_string.replace(" :", ":")
    output_string = output_string.replace(" ;", ";")

    return output_string

def main():
    if len(sys.argv) != 3:
        sys.stderr.write("Error: Too many or too few parameters have been given to the program.")
        return 1
    else:
        filepath: str = sys.argv[1]
        desired_verb_tag: str = sys.argv[2] # e.g. "nP,mR,p2,eA"

        # Open specified recipe and add morfological tags.
        text: str = open_bare(filepath)
        if len(text) > 90000:    # I am being nice to NLP Centre, real limit is 100000
            sys.stderr.write("Error: The text is too long.")
            return 1

        tagged_text: list[list[str]] = brno_tagger(text)

        # Find the most frequent tag of verbs. These verbs are most likely "action verbs".
        action_verb_tags: list[str] = get_action_verb_tags(tagged_text)

        # Transform "action verbs" into the desired form and print output.
        better_verbs: list[list[str]] = transform_verbs_in_vertical(tagged_text, action_verb_tags, desired_verb_tag)
        print(linearize_vertical(better_verbs))

        return 0

if __name__ == "__main__":
    main()
