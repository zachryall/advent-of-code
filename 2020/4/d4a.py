"""
Advent of Code 2020 - Day 4a - 206
"""

from pathlib import Path
import re

def main(file_name):
    """Main function
    """
    answer = 0
    array = []
    search_strings = ['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt']

    path = Path(__file__).with_name(file_name)
    with path.open('r', encoding='UTF-8') as file:
        lines = file.readlines() 
        record = ''
        for line in lines:
            if line == '\n':
                array.append(record)
                record = ''
            else:
                record = f'{record} {line.rstrip()}'
        array.append(record)

    for passport in array:
        found = all(s in passport for s in search_strings)
        if found:
            answer += 1

    return answer

ANSWER_EXAMPLE = main('example.txt')
ANSWER_INPUT = main('input.txt')

print(f'Example Input: {ANSWER_EXAMPLE}')
print(f'Puzzle Input: {ANSWER_INPUT}')
