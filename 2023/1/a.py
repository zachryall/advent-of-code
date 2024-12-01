file = open('file.txt', 'r')
lines = file.readlines()

total = 0
for line in lines:
    count = "blank"
    for i, c in enumerate(line):
        if c.isdigit():
            count = c
            break

    for c in reversed(line):
        if c.isdigit():
            count = count + c
            break

    total = total + int(count)

print(f"Sum of Calibration Value: {total}")
