"""
Advent of Code 2022 - Day 8a
"""

tree_list = []

def tree_check(tree_height_value, row, column, direction):
    """
    To check whether to the tree can be seen from a set direction
    :param tree_height_value:
    :param row:
    :param column:
    :param direction: direction to check | up, down, left, right
    :return: see/blocked
    """
    sight_bool = 0
    start = row - 1
    stop = -1
    step = -1

    if direction == 'up':
        start = row - 1
        stop = -1
        step = -1
    if direction == 'down':
        start = row
        stop = len(tree_list)
        step = 1

    for x in range(start, stop, step):
        print(f'Checking x: {column}, y: {row}, value: {tree_height_value}')
        if tree_height_value <= tree_list[x][column]:
            sight_bool = 1
            break
    if sight_bool == 1:
        print(f'{direction} - x: {column}, y: {row}, value: {tree_height_value} - blocked')
        return 'blocked'

    print(f'{direction} - x: {column}, y: {row}, value: {tree_height_value} - can see')
    return 'see'

with open('example.txt', 'r', encoding='UTF-8') as file:
    lines = file.readlines()

    for line in lines:
        tree_list.append(list(line.rstrip()))

    for row_index, row_context in enumerate(tree_list):
        if row_index in (0, len(tree_list)-1):
            print('-')
        else:
            for column_index, tree_height in enumerate(row_context):
                if column_index not in (0, len(row_context)-1):

                    # check above
                    result = tree_check(tree_height, row_index, column_index, 'up')
                    if result == 'blocked':
                        result = tree_check(tree_height, row_index, column_index, 'down')
                    # check below







            # check up, down, left right
            # skip first and last line
            # skip first and last column
