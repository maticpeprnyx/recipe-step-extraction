def get_attribute_value(tag: str, attribute: str) -> str:
    """
    Returns the value of the attribute in the tag.
    """
    index = tag.find(attribute)
    if index != -1:
        return tag[index:index + 2]
    else:
        return ""

def is_structural(tagger_output_item: list[str]) -> bool:
    """
    Returns True if the item is a structural token.
    """
    return len(tagger_output_item) == 1
    
def is_verb(tag: str) -> bool:
    """
    Returns True if the tag is that of a verb.
    """
    return get_attribute_value(tag, "k") == "k5"


def is_infinitive(tag: str) -> bool:
    """
    Returns True if the tag is that of an infinitive.
    """
    return get_attribute_value(tag, "m") == "mF"


def is_third_person(tag: str) -> bool:
    """
    Returns True if the tag is that of a verb in third person.
    """
    return get_attribute_value(tag, "p") == "p3" 

def same_mood(tag_1: str, tag_2: str) -> bool:
    """
    Returns true if both tags have the same mood.
    """
    mood_1 = get_attribute_value(tag_1, "m")
    mood_2 = get_attribute_value(tag_2, "m")
    return mood_1 == mood_2

def same_person(tag_1: str, tag_2: str) -> bool:
    """
    Returns true if both tags have the same person.
    """
    person_1 = get_attribute_value(tag_1, "p")
    person_2 = get_attribute_value(tag_2, "p")
    return person_1 == person_2

def same_number(tag_1: str, tag_2: str) -> bool:
    """
    Returns true if both tags have the same number.
    """
    number_1 = get_attribute_value(tag_1, "n")
    number_2 = get_attribute_value(tag_2, "n")
    return number_1 == number_2

# def len(tag) -> bool:
#     """
#     Returns True when there are more tags than one.
#     Example tagged item with multiple tags: 
#     ["který", "který", "k3yIgInSc1,k3yRgInSc1,k3yQgInSc1"]
#     """
#     tags: list[str] = tag.split(",")
#     return len(tags) > 1
