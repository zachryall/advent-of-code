"""
Advent of Code 2020 - Day 6b - 2947
"""

from pathlib import Path
import collections

def main(file_name):
    """Main function
    """
    answer = 0
    array = []

    path = Path(__file__).with_name(file_name)
    with path.open('r', encoding='UTF-8') as file:
        lines = file.readlines() 
        group = ''
        person_count = 0
        for line in lines:
            if line == '\n':
                array.append(f'{person_count}{group}')
                person_count = 0
                group = ''
            else:
                group += line.rstrip()
                person_count += 1
        array.append(f'{person_count}{group}')

    for entry in array:
        if entry[0] == '1':
            answer += len(entry) - 1
            continue

        letter_counts = collections.Counter(entry)
        for count in letter_counts.values():
            if count >= int(entry[0]):
                answer += 1

    return answer

ANSWER_EXAMPLE = main('example.txt')
ANSWER_INPUT = main('input.txt')

print(f'Example Input: {ANSWER_EXAMPLE}')
print(f'Puzzle Input: {ANSWER_INPUT}')
