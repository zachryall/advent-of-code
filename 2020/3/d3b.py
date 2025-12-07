"""
Advent of Code 2020 - Day 3b - 4723283400
"""

from pathlib import Path
import math




def main(file_name):
    """Main function
    """

    array = []
    slopes = [[1,1], [3,1], [5,1], [7,1], [1,2]]
    max_slope_x = max([sublist[0] for sublist in slopes])
    answer = 1


    path = Path(__file__).with_name(file_name)
    with path.open('r', encoding='UTF-8') as file:
        lines = file.readlines() 
        modifier = math.ceil((len(lines) * max_slope_x) / (len(lines[0].rstrip())))
        for line in lines:
            tmp_string = ''
            for i in range(int(modifier)):
                tmp_string += line.rstrip()
            array.append(tmp_string)

    for slope in slopes:
        answer *= slope_check(array, slope)

    return answer

def slope_check(array, slope):
    tree_counter = 0
    x = slope[0]
    y = slope[1]

    while y < len(array) and x < len(array[0]):
        if array[y][x] == '#':
            tree_counter += 1
        x += slope[0]
        y += slope[1]

    return tree_counter

ANSWER_EXAMPLE = main('example.txt')
ANSWER_INPUT = main('input.txt')

print(f'Example Input: {ANSWER_EXAMPLE}')
print(f'Puzzle Input: {ANSWER_INPUT}')
