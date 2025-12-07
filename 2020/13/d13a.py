"""
Advent of Code 2020 - Day 13a - 104
"""

from pathlib import Path
import math

def main(file_name):
    """Main function
    """

    path = Path(__file__).with_name(file_name)
    data = [row for row in path.read_text(encoding='UTF-8').strip().split('\n')]
    
    buses = [int(b) for b in data[1].split(',') if b != 'x']
    your_arrival_time = int(data[0])
    next_buses = []
    best_bus_id = 0
    min_wait_time = float('inf')

    for bus_id in buses:
        multiplier = math.ceil(your_arrival_time / bus_id)
        next_departure_time = multiplier * bus_id

        wait_time = next_departure_time - your_arrival_time
        if wait_time < min_wait_time:
            min_wait_time = wait_time
            best_bus_id = bus_id

    return best_bus_id * min_wait_time

ANSWER_EXAMPLE = main('example.txt')
ANSWER_INPUT = main('input.txt')

print(f'Example Input: {ANSWER_EXAMPLE}')
print(f'Puzzle Input: {ANSWER_INPUT}')
