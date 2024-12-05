"""
Advent of Code 2024 - Day 5
"""

from pathlib import Path

def find_middle_value_total(list_to_search):
    """Finds the middle value of each nested list and adds it to a total

    Args:
        list_to_search (list): Nested list of numbers

    Returns:
        int: Total of middle values
    """
    result = 0
    for x in list_to_search:
        middle_index = int((len(x) - 1)/2)
        result += int(x[middle_index])
    return result

def sort(list_to_sort, sorted_list, rules_list):
    """Sorts a list according to a set of rules

    Args:
        list_to_sort (list): The list to sort
        sorted_list (list): The list to append sorted lists to
        rules_list (list): The list of rules
    """
    change_made = True
    while change_made is True:
        change_made = False
        for x in range(len(list_to_sort)-1):
            for y in range(x+1, len(list_to_sort)):
                if f'{list_to_sort[y]}|{list_to_sort[x]}' in rules_list:
                    list_to_sort.append(list_to_sort.pop(x))
                    change_made = True
                    break
            if change_made:
                break
    if not change_made:
        sorted_list.append(list_to_sort)

def find_valid_list(list_to_check, valid_list, invalid_list, rules_list):
    """Checks if a list is valid according to a set of rules

    Args:
        list_to_check (list): The list to check
        valid_list (list): The list to append valid lists to
        invalid_list (list): The list to append invalid list to
        rules_list (list): The list of rules to follows
    """
    valid_update = True
    for x in range(len(list_to_check)-1):
        for y in range(x+1, len(list_to_check)):
            if f'{list_to_check[x]}|{list_to_check[y]}' not in rules_list:
                valid_update = False
                break
        if not valid_update:
            invalid_list.append(list_to_check)
            break
    if valid_update:
        valid_list.append(list_to_check)

def main(file_name, part):
    """Main function

    Args:
        file_name (str): The input file to use
        part (int): Whether to process for part 1 or 2

    Returns:
        _type_: _description_
    """

    answer = 0
    rules = []
    updates = []
    valid_updates = []
    invalid_updates = []
    sorted_updates = []

    path = Path(__file__).with_name(file_name)
    with path.open('r', encoding='UTF-8') as file:
        lines = file.readlines()
        for line in lines:
            if '|' in line:
                rules.append(line.rstrip())
            elif ',' in line:
                updates.append(line.rstrip().split(','))

    for pages in updates:
        find_valid_list(pages, valid_updates, invalid_updates, rules)

    if part == 1:
        answer = find_middle_value_total(valid_updates)
        return answer

    for pages in invalid_updates:
        sort(pages, sorted_updates, rules)

    return find_middle_value_total(sorted_updates)

ANSWER_EXAMPLE_A = main('example.txt', 1)
ANSWER_INPUT_A = main('input.txt', 1)
ANSWER_EXAMPLE_B = main('example.txt', 2)
ANSWER_INPUT_B = main('input.txt', 2)

print(f'A Example Input: {ANSWER_EXAMPLE_A}')
print(f'A Puzzle Input: {ANSWER_INPUT_A}')
print(f'B Example Input: {ANSWER_EXAMPLE_B}')
print(f'B Puzzle Input: {ANSWER_INPUT_B}')
