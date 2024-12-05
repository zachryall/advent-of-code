"""
Advent of Code 2024 - Day 5
"""

from pathlib import Path

def find_middle_value_total(list_to_search):
    result = 0
    for x in list_to_search:
        middle_index = int((len(x) - 1)/2)
        result += int(x[middle_index])
    return result

def main(file_name, part):
    """Main function

    :param file_name: The file that contexts the puzzle input
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
        valid_update = True
        for x in range(len(pages)-1):
            for y in range(x+1, len(pages)):
                if f'{pages[x]}|{pages[y]}' not in rules:
                    valid_update = False
                    break
            if not valid_update:
                invalid_updates.append(pages)
                break
        if valid_update:
            valid_updates.append(pages)

    if part == 1:
        answer = find_middle_value_total(valid_updates)
    elif part == 2:
        for i, pages in enumerate(invalid_updates):
            change_made = True
            while change_made is True:
                change_made = False
                for x in range(len(pages)-1):
                    for y in range(x+1, len(pages)):
                        if f'{pages[y]}|{pages[x]}' in rules:
                            invalid_updates[i].append(invalid_updates[i].pop(x))
                            change_made = True
                            break
                    if change_made:
                        break
            if not change_made:
                sorted_updates.append(pages)

        answer = find_middle_value_total(sorted_updates)

    return answer


ANSWER_EXAMPLE_A = main('example.txt', 1)
ANSWER_INPUT_A = main('input.txt', 1)
ANSWER_EXAMPLE_B = main('example.txt', 2)
ANSWER_INPUT_B = main('input.txt', 2)

print(f'A Example Input: {ANSWER_EXAMPLE_A}')
print(f'A Puzzle Input: {ANSWER_INPUT_A}')
print(f'B Example Input: {ANSWER_EXAMPLE_B}')
print(f'B Puzzle Input: {ANSWER_INPUT_B}')
