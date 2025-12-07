"""
Advent of Code 2020 - Day 11b - 2072
"""

from pathlib import Path

def seat_rule_checker(array, row, col, num_rows, num_cols):

    if array[row][col] == '.':
        return '.', False

    visible_occupied_count = 0
    deltas = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1),
    ]

    for dr, dc in deltas:
        nr, nc = row, col

        while True:
            nr += dr
            nc += dc

            if not (0 <= nr < num_rows and 0 <= nc < num_cols):
                break

            if array[nr][nc] == '#':
                visible_occupied_count += 1
                break

            if array[nr][nc] == 'L':
                break

    if visible_occupied_count == 0 and array[row][col] == 'L':
        return '#', True
    elif visible_occupied_count >= 5    and array[row][col] == '#':
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
