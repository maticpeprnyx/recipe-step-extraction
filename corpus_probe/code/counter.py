import sys

def clean_string(unclean_string: str) -> str:
    clean_string = unclean_string.strip()
    return clean_string

def print_dict(dictionary: dict, sort_items: bool):
    #print(f'{atribute_name}\tČet.\tRel. čet.')
    #print('-' * (len(f'{atribute_name}\tČetnost\tRel. četnost') + 4))
    items = sorted(dictionary.keys(), key=lambda key: dictionary[key], reverse=True) if sort_items == True else dictionary.keys()

    values_sum = sum(dictionary.values())
    for key in items:
        print(f'{key}\t{dictionary[key]}\t{(dictionary[key]/values_sum) * 100:.2f} %')

def main():
    with sys.stdin as input_stream:
        atribute: dict = dict()
        for line in input_stream:
            line = clean_string(line)
            if line in atribute:
                atribute[line] += 1
            else:
                atribute[line] = 1

        print_dict(atribute, False)

    return 0

if __name__ == '__main__':
    main()
