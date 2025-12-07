"""
Advent of Code 2020 - Day 11a - 2354
"""

from pathlib import Path

def seat_rule_checker(array, row, col, num_rows, num_cols):

    if array[row][col] == '.':
        return '.', False

    adjacent_seats_occupied = 0
    deltas = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1),
    ]

    for dr, dc in deltas:
        nr, nc = row + dr, col + dc

        if 0 <= nr < num_rows and 0 <= nc < num_cols:
            if array[nr][nc] == '#':
                adjacent_seats_occupied += 1

    if adjacent_seats_occupied == 0 and array[row][col] == 'L':
        return '#', True
    elif adjacent_seats_occupied >= 4 and array[row][col] == '#':
        return 'L', True
    
    return array[row][col], False

def main(file_name):
    """Main function
    """

    path = Path(__file__).with_name(file_name)
    data = [list(row) for row in path.read_text(encoding='UTF-8').strip().split('\n')]
    row_count = len(data)
    col_count = len(data[0])

    has_changed = True
    while has_changed:
        has_changed = False
        data_modified = [row[:] for row in data]
        for i in range(len(data)):
            for j in range(len(data[0])):
                data_modified[i][j], changed = seat_rule_checker(data, i, j, row_count, col_count)
                if changed:
                    has_changed = True
        data = data_modified

    answer = sum(item == '#' for sublist in data for item in sublist)
    return answer

ANSWER_EXAMPLE = main('example.txt')
ANSWER_INPUT = main('input.txt')

print(f'Example Input: {ANSWER_EXAMPLE}')
print(f'Puzzle Input: {ANSWER_INPUT}')
