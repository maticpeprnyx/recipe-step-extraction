# Run like this:
# python transform_text.py /path/to/recipe_in_paintext.txt

import sys
from open_file import open_bare
from APIs import brno_tagger
from tag import is_structural
from verb_tags import get_action_verb_tags

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

        for token in tagged_text:
            if not is_structural(token):
                current_tag: str = token[2]

                current_lemma: str = token[1].lower()
                current_token: str = token[0].lower()

                if current_tag in action_verb_tags:
                    print(f"{current_lemma}\t{current_token}")

if __name__ == "__main__":
    main()