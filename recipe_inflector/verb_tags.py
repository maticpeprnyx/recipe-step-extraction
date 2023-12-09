from APIs import inflected_verb
from tag import is_infinitive, is_structural, is_verb, same_mood, same_person
from time import sleep

def get_verb_tag_frequency(vertical: list[list[str]]) -> dict[str, int]:
    """
    Returns a dictionary that contains the frequencies of all verb tags in a text tagged by the Brno tagger.
    """
    frequency_dict: dict[str, int] = dict()
    for line in vertical:
        if not is_structural(line): # Token is not a structural tag, e.g. <g/>.
            tag: str = line[2]
            if not is_verb(tag):
                continue
            else:
                if tag in frequency_dict.keys():
                    frequency_dict[tag] += 1
                else:
                    frequency_dict[tag] = 0

    return frequency_dict

def get_most_frequent_verb_tag(vertical: list[list[str]]) -> str:
    """
    Returns the most frequent verbs tag in a text tagged by the Brno tagger.
    """
    verb_tag_frequency = get_verb_tag_frequency(vertical)
    most_frequent_verb_tag = max(verb_tag_frequency, key=lambda k: verb_tag_frequency.get(k, 0))
    return most_frequent_verb_tag

def get_action_verb_tags(vertical: list[list[str]]) -> list[str]:
    """
    Returns a list of tags that match 'action verbs' in a text tagged by the Brno tagger.
    These tags should match in mood and person.
    """
    action_verb_tags: list = list()
    cannonical_action_verb_tag = get_most_frequent_verb_tag(vertical)

    if is_infinitive(cannonical_action_verb_tag):
        action_verb_tags.append(cannonical_action_verb_tag)
        return action_verb_tags
    else:
        verb_tag_frequency = get_verb_tag_frequency(vertical)
        for verb_tag in verb_tag_frequency.keys():
            if same_mood(verb_tag, cannonical_action_verb_tag) and same_person(verb_tag, cannonical_action_verb_tag):
                action_verb_tags.append(verb_tag)

        return action_verb_tags

def transform_verbs_in_vertical(vertical: list[list[str]], original_verb_forms: list[str], desired_verb_form: str) -> list[list[str]]:
    for i in range(len(vertical)):
        if not is_structural(vertical[i]): # Token is not a structural tag, e.g. <g/>.
            current_tag: str = vertical[i][2]
            current_lemma: str = vertical[i][1]
            if current_tag in original_verb_forms:
                vertical[i][2] = desired_verb_form
                vertical[i][0] = inflected_verb(current_lemma, desired_verb_form)
                sleep(1.5)  # Wait a bit because only one request per second is permited.
    return vertical 
