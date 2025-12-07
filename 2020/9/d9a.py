"""
Advent of Code 2020 - Day 9a - 26796446
"""

from pathlib import Path
import re

def main(file_name, preamble_size):
    """Main function
    """

    path = Path(__file__).with_name(file_name)
    data = [int(row) for row in path.read_text(encoding='UTF-8').strip().split('\n')]
    
    current_index = preamble_size
    window_start = 0
    window_end = 1

    while window_start < len(data) - preamble_size:
        while window_end < current_index:
            calc = data[window_start] + data[window_end]
            if calc == data[current_index]:
                current_index += 1
                window_start = current_index - preamble_size
                window_end = window_start + 1
            else:
                window_end += 1
        window_start += 1
        window_end = window_start + 1

    return data[current_index]

ANSWER_EXAMPLE = main('example.txt', 5)
ANSWER_INPUT = main('input.txt', 25)

print(f'Example Input: {ANSWER_EXAMPLE}')
print(f'Puzzle Input: {ANSWER_INPUT}')
