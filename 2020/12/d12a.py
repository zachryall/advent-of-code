"""
Advent of Code 2020 - Day 12a - 2270
"""

from pathlib import Path

def main(file_name):
    """Main function
    """

    path = Path(__file__).with_name(file_name)
    data = [row for row in path.read_text(encoding='UTF-8').strip().split('\n')]

    distance_x = 0
    distance_y = 0
    direction = 1
    # N = 0, E = 1, S = 2, W = 3

    for instruction in data:
        action = instruction[0]
        distance = int(instruction[1:])
        if action == 'F':
            if direction == 0:
                distance_y += distance
            elif direction == 1:
                distance_x += distance
            elif direction == 2:
                distance_y -= distance
            elif direction == 3:
                distance_x -= distance
        elif action == 'R':
            direction = (direction + distance // 90) % 4
        elif action == 'L':
            direction = (direction - distance // 90) % 4
        elif action == 'N':
            distance_y += distance
        elif action == 'E':
            distance_x += distance
        elif action == 'S':
            distance_y -= distance
        elif action == 'W':
            distance_x -= distance
    
    print(distance_x, distance_y)

    return abs(distance_x) + abs(distance_y)

ANSWER_EXAMPLE = main('example.txt')
ANSWER_INPUT = main('input.txt')

print(f'Example Input: {ANSWER_EXAMPLE}')
print(f'Puzzle Input: {ANSWER_INPUT}')
