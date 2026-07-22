"""
Advent of Code 2025 - Day 4
"""

from pathlib import Path
import re

SURROUNDINGS = [
    (-1, -1), (-1, 0), (-1, 1),
    ( 0, -1)         , ( 0, 1),
    ( 1, -1), ( 1, 0), ( 1, 1)
]

def get_neighbors(grid, r, c):
    rows = len(grid)
    cols = len(grid[0])
    neighbours = []

    for dr, dc in SURROUNDINGS:
        nr, nc = r + dr, c + dc

        # Boundary check: make sure the neighbor is inside the grid
        if 0 <= nr < rows and 0 <= nc < cols:
            neighbours.append(grid[nr][nc])
    return neighbours

def main(file_name, part):
    """Main function

    :param file_name: The file that contexts the puzzle input
    :param part: The part of the challenge
    """
    # answer = 0

    # path = Path(__file__).with_name(file_name)
    # with path.open('r', encoding='UTF-8') as file:
    #     lines = file.read().splitlines() 
        
    #     for y in range(len(lines)):
    #         for x in range(len(lines[0])):
    #             if lines[y][x] == '@':
    #                 output = get_neighbors(lines, y, x)
    #                 if output.count('@') < 4:
    #                     answer += 1
    #                     temp[y][x] = 'X'
    # return answer

    answer = 0
    removed = 1

    path = Path(__file__).with_name(file_name)
    with path.open('r', encoding='UTF-8') as file:
        lines = file.read().splitlines() 
        mirror = [list(line) for line in lines]
        
        while removed > 0:
            removed = 0
            for y in range(len(lines)):
                for x in range(len(lines[0])):
                    if lines[y][x] == '@':
                        output = get_neighbors(lines, y, x)
                        if output.count('@') < 4:
                            removed += 1
                            mirror[y][x] = '.'
                            
            lines = [list(m) for m in mirror]
            answer += removed
            
            if part == 1:
                removed = 0
    return answer

ANSWER_A = main('input.txt', 1)
ANSWER_B = main('input.txt', 2)
print(f'Part 1 - Puzzle Input: {ANSWER_A}')
print(f'Part 2 - Puzzle Input: {ANSWER_B}')