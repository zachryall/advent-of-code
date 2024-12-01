"""
Advent of Code 2022 - Day 5a
"""

with open('input.txt', 'r', encoding='UTF-8') as file:
    lines = file.readlines()

    ROW_COUNT = 0

    for line in lines:
        if line.startswith(' 1   '):
            rows = line.split('   ')
            ROW_COUNT = len(rows)

    print(f'The container row count is {ROW_COUNT}')
    containers = [[] for i in range(ROW_COUNT)]

    for line in lines:
        if line.startswith(' 1'):
            break
        trim = line.rstrip()
        rows = trim.split(' [')

        if len(rows) == ROW_COUNT:
            for x in range(ROW_COUNT):
                containers[x].insert(0, rows[x].strip(']['))
        else:
            COUNTER = 0
            for index, row in enumerate(rows):
                leadingSpaces = len(row) - len(row.lstrip(' '))
                print("Leading spaces", leadingSpaces, row.strip(']['))

                if leadingSpaces > 0:
                    loopCounter = int((leadingSpaces + 1) / 3)
                    for x in range(loopCounter):
                        containers[index].insert(0, '')
                        COUNTER += 1
                elif leadingSpaces == 0:
                    containers[index].insert(0, row.strip(']['))
                    COUNTER += 1
        print(containers)

    for x in range(ROW_COUNT):
        containers[x] = list(filter(None, containers[x]))

    print('=========')
    print(containers)

        # none, row 0
        # 3, row index 1
        # 7, row index 2

    # process starting positions into 2d list
    # loop
    #   understand the text
    #   do the text
    # read off tops
