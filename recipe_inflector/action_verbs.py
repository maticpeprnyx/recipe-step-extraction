# Run like this:
# python transform_text.py /path/to/recipe_in_paintext.txt

import sys
from open_file import open_bare
from APIs import brno_tagger
from tag import is_structural, is_infinitive
from verb_tags import get_action_verb_tags

def find_closest_infinitive(vertical: list[list[str]], starting_index: int, right_context_size: int) -> list[str]:
    for i in range(starting_index, starting_index + right_context_size):
        if is_infinitive(vertical[i][2]):
            return vertical[i]

    return ["", "", ""]

def main():
    if len(sys.argv) != 2:
        sys.stderr.write("Error: Too many or too few parameters have been given to the program.")
        return 1
    else:
        filepath: str = sys.argv[1]

        # Open specified recipe and add morfological tags.
        text: str = open_bare(filepath)
        if len(text) > 90000:
            sys.stderr.write("Error: The text is too long.")
            return 1

        tagged_text: list[list[str]] = brno_tagger(text)

        action_verb_tags: list[str] = get_action_verb_tags(tagged_text)

        for i in range(len(tagged_text)):
            if not is_structural(tagged_text[i]):
                current_tag: str = tagged_text[i][2]

                current_lemma: str = tagged_text[i][1].lower()
                current_token: str = tagged_text[i][0].lower()

                if current_lemma == "nechat":
                    closest_verb = find_closest_infinitive(tagged_text, i, 3)
                    current_lemma += " " + closest_verb[1].lower()
                    current_token += " " + closest_verb[0].lower()

                    current_lemma = current_lemma.strip()
                    current_token = current_token.strip()

                if current_tag in action_verb_tags:
                    print(f"{current_lemma}\t{current_token}")

if __name__ == "__main__":
    main()