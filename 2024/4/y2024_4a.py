"""
Advent of Code 2024 - Day 4a - 2618
"""

from pathlib import Path

def search(direction: str, search_list: list):
    """Searches the 'wordsearch' for XMAS

    Args:
        direction (string): Which direction to search in
        search_list (string): A nested list to search

    Returns:
        int: Number of matches found
    """
    i_mod_1, i_mod_2, i_mod_3 = 0, 0, 0
    j_mod_1, j_mod_2, j_mod_3 = 0, 0, 0
    i_range_mod, j_range_mod = 0, 0
    start = 0
    total = 0
    if direction in ('horizontal', 'diagonal-down'):
        j_mod_1, j_mod_2, j_mod_3 = 1, 2, 3
        j_range_mod = -3
    if direction in ('vertical', 'diagonal-down', 'diagonal-up'):
        i_mod_1, i_mod_2, i_mod_3 = 1, 2, 3
        i_range_mod = -3
    if direction == 'diagonal-up':
        j_mod_1, j_mod_2, j_mod_3 = -1, -2, -3
        start = 3

    for i in range(len(search_list) + i_range_mod):
        for j in range(start ,len(search_list[0]) + j_range_mod):
            to_check = (
                search_list[i][j] +
                search_list[i + i_mod_1][j + j_mod_1] +
                search_list[i + i_mod_2][j + j_mod_2] +
                search_list[i + i_mod_3][j + j_mod_3]
            )
            if to_check in ('XMAS', 'SAMX'):
                total += 1
    return total

def main(file_name):
    """Main function

    :param file_name: The file that contexts the puzzle input
    """
    data = []
    answer = 0
    path = Path(__file__).with_name(file_name)
    with path.open('r', encoding='UTF-8') as file:
        lines = file.readlines()
        for line in lines:
            data.append(list(line.rstrip()))

    answer += search('horizontal', data)
    answer += search('vertical', data)
    answer += search('diagonal-down', data)
    answer += search('diagonal-up', data)

    return answer

ANSWER_EXAMPLE = main('example.txt')
ANSWER_INPUT = main('input.txt')

print(f'Example Input: {ANSWER_EXAMPLE}')
print(f'Puzzle Input: {ANSWER_INPUT}')
