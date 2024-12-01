file = open('input.txt', 'r')
lines = file.readlines()
file.close()

x_counter = 0
y_counter = 0
x_max = 0
y_max = 0
volume = 0

outline = []

# calculate max lagoon size
for line in lines:
    segments = line.split(' ')
    if segments[0] == 'R':
        x_counter += int(segments[1])
        if x_counter > x_max:
            x_max = x_counter
    elif segments[0] == 'L':
        x_counter -= int(segments[1])
    elif segments[0] == 'D':
        y_counter += int(segments[1])
        if y_counter > y_max:
            y_max = y_counter
    elif segments[0] == 'U':
        y_counter -= int(segments[1])

print(f'Max lagoon size is {x_max} x {y_max}')

# reset counters
x_counter = 0
y_counter = 0

# create blank outline list
outline_line = "." * (x_max + 1)
outline = [outline_line] * (y_max + 1)

# draw the outline
for i, line in enumerate(lines):
    segments = line.split(' ')
    
    if segments[0] == 'R':
        line_list = list(outline[y_counter])
        for index in range(x_counter, x_counter + int(segments[1]) + 1):
            line_list[index] = '#'
        outline[y_counter] = ''.join(line_list)
        x_counter += int(segments[1])
    elif segments[0] == 'L':
        line_list = list(outline[y_counter])
        for index in range(x_counter, x_counter - int(segments[1]) - 1, -1):
            line_list[index] = '#'
        outline[y_counter] = ''.join(line_list)
        x_counter -= int(segments[1])
    elif segments[0] == 'D':
        for index in range(y_counter, y_counter + int(segments[1]) + 1):
            down_list = list(outline[index])
            down_list[x_counter] = '#'
            outline[index] = ''.join(down_list)
        y_counter += int(segments[1])
    elif segments[0] == 'U':
        for index in range(y_counter, y_counter - int(segments[1]) - 1, -1):
            print(index)
            up_list = list(outline[index])
            up_list[x_counter] = '#'
            outline[index] = ''.join(up_list)
        y_counter -= int(segments[1])

# create the lagoon list
lagoon = outline.copy()

# fill in the lagoon and calculate the volume
for i, line in enumerate(lagoon):
    start_index = line.find('#')
    end_index = line.rfind('#')

    lagoon_line_list = list(line)
    for index in range(start_index, end_index + 1):
        lagoon_line_list[index] = '#'
        volume += 1
    lagoon[i] = ''.join(lagoon_line_list)

for line in lagoon:
    print(line)

print(f'Volume = {volume}')

