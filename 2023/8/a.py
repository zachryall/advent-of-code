# file = open('example2.txt', 'r')
file = open('input.txt', 'r')
lines = file.readlines()
file.close()


def get_next_node(node, direction):
    line = lines[node]
    if lines[0][direction].rstrip() == "L":
        next_start_point = line[7:10]
    else:
        next_start_point = line[12:15]
    return [index for index, line in enumerate(lines) if line.startswith(next_start_point)][0]


current_node_index = 2
current_direction_index = 0
steps = 0
directions_length = len(lines[0].rstrip())

print(f'Directions are {lines[0].rstrip()}, length = {directions_length}')

while not lines[current_node_index].startswith('ZZZ'):
    print(f'node: {lines[current_node_index].rstrip()}, direction: {lines[0][current_direction_index].rstrip()}')
    current_node_index = get_next_node(current_node_index, current_direction_index)
    steps += 1
    current_direction_index += 1
    if current_direction_index + 1 > directions_length:
        current_direction_index = 0
    print(f'Current Step: {steps}')

print(f'Steps: {steps}')
