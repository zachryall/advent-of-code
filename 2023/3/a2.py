import re
file = open('example.txt', 'r')
lines = file.readlines()
file.close()

pattern = r'[^0-9.]'
total = 0

for index, line in enumerate(lines):

    symbols = re.findall(pattern, line.rstrip())
    print(symbols)

    for symbol in symbols:
        # check left, right
        # check
