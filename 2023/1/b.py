from word2number import w2n

# file = open('file.txt', 'r')
file = open('test.txt', 'r')
lines = file.readlines()

numbers_list = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]

total = 0
for line in lines:
    count = "blank"
    for i, c in enumerate(line):
        checker = 0
        found_word = 0
        if c.isdigit():
            count = c
            break
        for item in numbers_list:
            index = line.find(item, i, i + 5)
            print(index)
            if index != -1:
                checker = 1
                found_word = item
                break
        if checker == 1:
            count = w2n.word_to_num(found_word)
            print("1st", count)
            break

    for c in reversed(line):
        checker = 0
        found_word = 0
        i = line.find(c)
        if c.isdigit():
            count = count + c
            break
        for item in numbers_list:
            reversed_number = reversed(item)
            print("number", item)
            print("backwards", item[::-1])
            index = line.find(item[::-1], i, i - 5)
            if index != -1:
                checker = 1
                found_word = item
                break
        if checker == 1:
            print("1st again", count)
            count = count + w2n.word_to_num(found_word)
            print("2nd", count)
            break
    print(count)
    # total = total + int(count)

# print(f"Sum of Calibration Value: {total}")
