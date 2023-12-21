import sys
from open_file import open_lines, listdir_fullpath

def clean_string(unclean_string: str) -> str:
    """
    Removes hanging whitespace from string.
    """
    clean_string = unclean_string.strip()
    return clean_string

def print_dict(dictionary: dict, sort_items: bool):
    """
    Prints out a frequency dictionary.
    """
    items = sorted(dictionary.keys(), key=lambda key: dictionary[key], reverse=True) if sort_items == True else dictionary.keys()

    values_sum = sum(dictionary.values())
    for key in items:
        print(f'{key}\t{dictionary[key]}\t{(dictionary[key]/values_sum) * 100:.2f} %')

def clean_sl(input_line: list[str]) -> list[str]:
    """
    Removes newlines from a list of characters.
    """
    output_line: list[str] = list()

    for item in input_line:
        if item != "\n":
            output_line.append(item)

    return output_line

def fill_frequency_dict(freq_dict: dict[str, int], new_item: str) -> dict[str, int]:
    """
    Adds an item into a frequency dictionary.
    """
    if new_item in freq_dict:
        freq_dict[new_item] += 1
    else:
        freq_dict[new_item] = 1

    return freq_dict

def main():
    input_folder_path: str = sys.argv[1]
    output_folder_path: str = sys.argv[2]
    for short_filename, long_filename in listdir_fullpath(input_folder_path):
        output_filename: str = output_folder_path + short_filename
        sys.stdout = open(output_filename, "wt")

        vertical: list[str] = open_lines(long_filename)

        verb_frequencies: dict[str, int] = dict()

        for line in vertical:
            split_line: list[str] = [split_part for split_part in line.split("\t") if split_part]
            split_line = clean_sl(split_line)
            if len(split_line) > 1:
                current_tag: str = split_line[2]
                if current_tag[:2] == "k5":
                    verb_frequencies = fill_frequency_dict(verb_frequencies, current_tag)

        print_dict(verb_frequencies, True)

if __name__ == '__main__':
    main()
