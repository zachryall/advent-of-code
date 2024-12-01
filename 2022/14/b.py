"""
Advent of Code 2022 - Day 14b - 27566
"""

import re
from pathlib import Path

def create_empty_cave(x_minimum, x_maximum, y_maximum, cave):
    """Create an nested list to represent the cave

    :param x_minimum: The minimum value of the X axis
    :param x_maximum: The maximum value of the X axis
    :param y_maximum: The maximum value of the Y axis
    :param cave: The list containing the cave layout
    :return: The new y_maximum
    """
    for i in range(y_maximum + 2):
        cave.append([])
        for _ in range(x_maximum - x_minimum + 1):
            cave[i].append('.')
    cave[0][500 - x_minimum] = '+'

    y_maximum += 2
    cave.append([])
    for _ in range(x_maximum - x_minimum + 1):
        cave[y_maximum].append('#')
    return y_maximum


def add_walls(x_minimum, cave, walls):
    """Adds the wall corners to the nested layout

    :param x_minimum: The minimum value of the X axis
    :param cave: The list containing the cave layout
    :param walls: The list containing the walls layout
    """
    for wall in walls:
        last_wall_section = '0,0'
        for wall_section in wall:
            coord = wall_section.split(',')
            cave[int(coord[1])][int(coord[0])  - x_minimum] = '#'

            last_coord = last_wall_section.split(',')

            if last_coord[0] == coord[0]:
                wall_filler(last_coord[1], coord, 'vertical', x_minimum, cave)
            elif  last_coord[1] == coord[1]:
                wall_filler(last_coord[0], coord, 'horizontal', x_minimum, cave)

            last_wall_section = wall_section

def wall_filler(last_coordinates, current_coordinates, plane, x_minimum, cave):
    """Fills in the walls between the wall corner in the nested layout

    :param last_coordinates: The last wall corner placed
    :param current_coordinates: The current wall corner to place
    :param other_value: The other coordinate
    :param plane: Whethe the fill vertical or horizontal
    :param x_minimum: The minimum value of the X axis
    :param cave: The list containing the cave layout
    """
    x = current_coordinates[0]
    y = current_coordinates[1]
    if plane == 'vertical':
        x = current_coordinates[1]
        y = current_coordinates[0]
    direction = 1
    last_coordinates = int(last_coordinates)
    x = int(x)
    y = int(y)
    if last_coordinates < x:
        direction = -1
    for i in range(x, last_coordinates, direction):
        if plane == 'horizontal':
            cave[y][i - x_minimum] = '#'
        else:
            cave[i][y - x_minimum] = '#'

def drop_sand(x_minimum, y_maximum, cave):
    """_summary_

    :param x_minimum: The minimum value of the X axis
    :param y_maximum: The maximum value of the Y axis
    :param cave: The list containing the cave layout
    :return: The total number of sand dropped
    """
    sand_landed = 0
    while True:
        position = [500 - x_minimum, 0]
        landed = False
        if cave[0][500 - x_minimum] == 'O':
            break
        while True:
            if position[1] >= y_maximum:
                break

            if cave[position[1] + 1][position[0]] == '.':
                position[1] += 1
            elif cave[position[1] + 1][position[0] - 1] == '.':
                position[0] -= 1
                position[1] += 1
            elif cave[position[1] + 1][position[0] + 1] == '.':
                position[0] += 1
                position[1] += 1
            else:
                cave[position[1]][position[0]] = 'O'
                sand_landed += 1
                landed = True
                break
        if not landed:
            break

    return sand_landed

def main(file_name):
    """Main function

    :param file_name: The file that contexts the puzzle input
    """
    walls = []
    cave_layout = []
    x_max = 500
    x_min = 500
    y_max = 0
    answer = 0
    extend = 1000

    path = Path(__file__).with_name(file_name)
    with path.open('r', encoding='UTF-8') as file:
        lines = file.readlines()

        for line in lines:
            coords = re.split(' -> |\n', line)
            coords = list(filter(None, coords))
            walls.append(coords)
            for coord in coords:
                coord_values = coord.split(',')
                coord_values = [int(item) for item in coord_values]

                y_max = max(y_max, coord_values[1])

                if x_max < coord_values[0]:
                    x_max = coord_values[0]
                elif x_min > coord_values[0]:
                    x_min = coord_values[0]
    x_min -= extend
    x_max += extend
    y_max = create_empty_cave(x_min, x_max, y_max, cave_layout)
    add_walls(x_min, cave_layout, walls)
    answer = drop_sand(x_min, y_max, cave_layout)

    return answer

ANSWER_EXAMPLE = main('example.txt')
ANSWER_INPUT = main('input.txt')

print(f'Example Input: {ANSWER_EXAMPLE}')
print(f'Puzzle Input: {ANSWER_INPUT}')
