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

        for i in range(start_location, end_location + 1):

            if i == 0:
                check belwo

            if index != len(lines) - 1:
                below_line = list(lines[index + 1])

                if not below_line[i] == '.' or below_line[i].isdigit():
                    print('valid part, break')
                    total += int(number)
                    break
                else:
                    print('not sure')

            if index != 0:
                above_line = list(lines[index - 1])

                if not above_line[i] == '.' or above_line[i].isdigit():
                    print('valid part, break')
                    total += int(number)
                    break
                else:
                    print('not sure')

            if i == end_location:
                check after



    # if line index 0, check below
    # elif line index n, check above
    # else, check above and below

print(total)
