"""
Advent of Code 2020 - Day 3a - 187
"""

from pathlib import Path
import math




def main(file_name):
    """Main function
    """
    array = []
    answer = 0
    slope = [3, 1]
    x = slope[0]
    y = slope[1]

    path = Path(__file__).with_name(file_name)
    with path.open('r', encoding='UTF-8') as file:
        lines = file.readlines() 
        modifier = math.ceil((len(lines) * x) / (len(lines[0].rstrip())))
        for line in lines:
            tmp_string = ''
            for i in range(int(modifier)):
                tmp_string += line.rstrip()
            array.append(tmp_string)

    while y < len(array) and x < len(array[0]):
        if array[y][x] == '#':
            answer += 1
        x += slope[0]
        y += slope[1]

    return answer

ANSWER_EXAMPLE = main('example.txt')
ANSWER_INPUT = main('input.txt')

print(f'Example Input: {ANSWER_EXAMPLE}')
print(f'Puzzle Input: {ANSWER_INPUT}')
