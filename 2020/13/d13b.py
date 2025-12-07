"""
Advent of Code 2020 - Day 13b - 842186186521918
"""

from pathlib import Path
import math

def main(file_name):
    """Main function
    """

    path = Path(__file__).with_name(file_name)
    data = [row for row in path.read_text(encoding='UTF-8').strip().split('\n')]
    buses = data[1].split(',')
    print(buses)

    values = []

    for index, bus_id in enumerate(buses):
        if bus_id != 'x':
            bus_id = int(bus_id)
            values.append((bus_id, (bus_id - index) % bus_id))
    print(values)

    time, step = 0, 1

    for bus_id, remainder in values:
        bus_id = int(bus_id)
        while (time % bus_id) != remainder:
            time += step
        step *= bus_id

    return time

ANSWER_EXAMPLE = main('example.txt')
ANSWER_INPUT = main('input.txt')

print(f'Example Input: {ANSWER_EXAMPLE}')
print(f'Puzzle Input: {ANSWER_INPUT}')
