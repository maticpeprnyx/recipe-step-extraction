# Run like this:
# python success_rate.py /path/to/file_1.py /path/to/file_2.py
# (Every entry should be on its own line.)
import sys
from difflib import Differ
from open_file import open_lines

def jaccard_similarity(list_1: list, list_2: list) -> float:
    """
    Calculates the Jaccard Similarity between 'list_1' and 'list_2':
    JS = |A ∩ B| / |A ∪ B|
    """
    manual_set: set = set(list_1)
    automatic_set: set = set(list_2)
    intersection: set = manual_set.intersection(automatic_set)
    union: set = manual_set.union(automatic_set)
    return len(intersection) / len(union)

def calculate_success_rate(list_1: list[str], list_2: list[str]) -> tuple[float, float]:
    """
    Calculates the rate of true positives and false positives of two lists.
    Returns a tuple of (true_positive_rate, false_positive_rate).
    """
    total_words = len(list_1)
    true_positives = 0  # True Positives
    false_positives = 0  # False Positives

    # align the two lists
    aligned_words: list[tuple[str, str]] = align_lists(list_1, list_2)
    
    for pair in aligned_words:
        # print(f"{pair[0]} ?= {pair[1]}")
        if pair[0] == pair[1]:
            true_positives += 1
        else:
            false_positives += 1
    
    true_positive_rate: float = (true_positives / total_words) * 100
    false_positive_rate: float = (false_positives / total_words) * 100
    
    return true_positive_rate, false_positive_rate

def align_lists(list_1: list[str], list_2: list[str]) -> list[tuple[str, str]]:
    """
    Aligns two lists (e.g. ["b", "a", "c", "f", "e", "c"] and ["a", "c", "e", "z"]) like this:
    b       -
    a       a
    c       c
    f       -
    e       e
    c       -
    -       z
    """
    # Compare the two lists using differ.
    differ = Differ()
    differ_comparison: list[str] = list(differ.compare(list_1, list_2))

    # create the side-by-side comparison list by parsing output of differ 🤢
    aligned: list[tuple[str, str]] = list()
    for line in differ_comparison:
        prefix = line[:2]
        value = line[2:].strip()
        
        if prefix == '  ':
            aligned.append((value, value))
            # print(f"{value}\t{value}")
        elif prefix == '- ':
            aligned.append((value, ""))
            # print(f"{value}\t-")
        elif prefix == '+ ':
            aligned.append(("", value))
            # print(f"-\t{value}") 

    return aligned

def print_aligned_lists(aligned: list[tuple[str, str]]):
    for items in aligned:
        item_1 = items[0] if items[0] else "-"
        item_2 = items[1] if items[1] else "-"

        print(f"{item_1} | {item_2}")

def main():
    if len(sys.argv) != 3:
        sys.stderr.write("Error: Too many or too few parameters have been given to the program.")
        return 1
    else:
        filepath_1: str = sys.argv[1]
        filepath_2: str = sys.argv[2]

        word_list_a = open_lines(filepath_1)
        word_list_b = open_lines(filepath_2)

        # remove empty strings and hanging whitespace
        word_list_a = [i.strip() for i in word_list_a if i]
        word_list_b = [i.strip() for i in word_list_b if i]

        print_aligned_lists(align_lists(word_list_a, word_list_b))
        print()

        # calculate the measures
        js = jaccard_similarity(word_list_a, word_list_b)
        tp, fp = calculate_success_rate(word_list_a, word_list_b)

        print(f"JS:\t{js*100:.2f} %")
        print(f"TP:\t{tp:.2f} %")
        print(f"FP:\t{fp:.2f} %")
        return 0

if __name__ == "__main__":
    main()