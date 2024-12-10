"""
Advent of Code 2015 - Day 18
"""

from pathlib import Path
import logging
from collections import Counter

logging.basicConfig(level=logging.WARN)

def change_light(check_list, change_list, count, part, coords):
    """Changes the light according to the state of the surrounding lights

    Args:
        check_list (list): A nested list of lights to check against
        change_list (list): A nested list of lights to modify
        count (int): The number of surrounding lights that are on
        part (int): The part of the challenge
        coords (list): X, Y coordinates of the light in question
    """
    x = coords[0]
    y = coords[1]
    if (
        check_list[y][x] == '#' and
        count not in (2, 3) and
        not (
            part == 2 and
            x in (0, len(check_list[y])-1) and
            y in (0, len(check_list)-1)
        )
    ):
        change_list[y][x] = '.'
    elif (
        check_list[y][x] == '.' and
        count == 3 and
        not (
            part == 2 and
            x in (0, len(check_list[y])-1)
            and y in (0, len(check_list)-1)
        )
    ):
        change_list[y][x] = '#'

def check_surrounding_lights(deltas, data, coords):
    """Checks the state of the surrounding lights and returns the count

    Args:
        deltas (list): A list of delta coordinate values to check
        data (list): A nested list of lights to check against
        coords (list): X, Y coordinates of the light in question

    Returns:
        _type_: _description_
    """
    count = 0
    x = coords[0]
    y = coords[1]
    for dx, dy in deltas:
        if (
            0 <= x + dx < len(data[0]) and
            0 <= y + dy < len(data[0]) and
            data[y + dy][x + dx] == '#'
        ):
            count += 1
    return count


def main(file_name, part):
    """Main function

    :param file_name: The file that contexts the puzzle input
    :param part: The part of the challenge
    """

    steps = 100
    data = []
    deltas = [
        (-1, -1), (-1, 0), (-1, 1),
        ( 0, -1),          ( 0, 1),
        ( 1, -1), ( 1, 0), ( 1, 1)
    ]

    path = Path(__file__).with_name(file_name)
    with path.open('r', encoding='UTF-8') as file:
        lines = file.readlines()
        for line in lines:
            data.append(list(line.strip()))

    for _ in range(steps):
        data_copy = [row[:] for row in data]
        for y, value in enumerate(data):
            for x in range(len(value)):
                surround_count = check_surrounding_lights(deltas, data, [x, y])
                change_light(data, data_copy, surround_count, part, [x, y])
        data = [row[:] for row in data_copy]

    return sum(Counter(x)['#'] for x in data)

ANSWER_A = main('input.txt', 1)
ANSWER_B = main('input.txt', 2)
print(f'Part 1 - Puzzle Input: {ANSWER_A}')
print(f'Part 2 - Puzzle Input: {ANSWER_B}')
