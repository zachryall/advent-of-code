"""
Advent of Code 2020 - Day 9b - 3353494
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
    answer = 0

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

    invalid_number = data[current_index]

    invalid_window_start = 0
    invalid_window_end = 1
    found = False
    running_total = []
    while not found:
        running_total.append(data[invalid_window_end])
        if sum(running_total) < invalid_number:
            invalid_window_end += 1
        elif sum(running_total) == invalid_number:
            running_total.sort()
            found = True
        elif sum(running_total) > invalid_number:
            invalid_window_start += 1
            invalid_window_end = invalid_window_start + 1
            running_total.clear()


    return running_total[0] + running_total[-1]

ANSWER_EXAMPLE = main('example.txt', 5)
ANSWER_INPUT = main('input.txt', 25)

print(f'Example Input: {ANSWER_EXAMPLE}')
print(f'Puzzle Input: {ANSWER_INPUT}')
