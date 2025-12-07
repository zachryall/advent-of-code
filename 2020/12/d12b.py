"""
Advent of Code 2020 - Day 12b - 138669
"""

from pathlib import Path

def main(file_name):
    """Main function
    """

    path = Path(__file__).with_name(file_name)
    data = [row for row in path.read_text(encoding='UTF-8').strip().split('\n')]

    distance_x = 0
    distance_y = 0
    waypoint_x = 10
    waypoint_y = 1
    movements = {
        'N': (0, 1), 
        'E': (1, 0), 
        'S': (0, -1), 
        'W': (-1, 0)
    }

    for instruction in data:
        action = instruction[0]
        distance = int(instruction[1:])
        if action == 'F':
            distance_x += waypoint_x * distance
            distance_y += waypoint_y * distance
        elif action == 'R' or action == 'L':
            if action == 'L':
                distance = 360 - distance
            count = distance // 90
            for i in range(count):
                waypoint_x, waypoint_y = waypoint_y, -waypoint_x  
            continue

        if action in movements:
            dx, dy = movements[action]
            waypoint_x += dx * distance
            waypoint_y += dy * distance

    return abs(distance_x) + abs(distance_y)

ANSWER_EXAMPLE = main('example.txt')
ANSWER_INPUT = main('input.txt')

print(f'Example Input: {ANSWER_EXAMPLE}')
print(f'Puzzle Input: {ANSWER_INPUT}')
