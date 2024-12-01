import re
file = open('example.txt', 'r')
lines = file.readlines()
file.close()

pattern = r'\d+'
total = 0

for index, line in enumerate(lines):

    numbers = re.findall(pattern, line)
    print(numbers)

    for number in numbers:
        start_location = line.find(number)
        end_location = start_location + len(number)

        # check before

        # loop, check above and below
        # check after

        chars = list(line)

    # if line index 0, check below
    # elif line index n, check above
    # else, check above and below

print(total)
