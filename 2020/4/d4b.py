"""
Advent of Code 2020 - Day 4b - 123
"""

from pathlib import Path
import re

def main(file_name):
    """Main function
    """
    answer = 0
    array = []
    search_strings = ['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt']

    path = Path(__file__).with_name(file_name)
    with path.open('r', encoding='UTF-8') as file:
        lines = file.readlines() 
        record = ''
        for line in lines:
            if line == '\n':
                array.append(record)
                record = ''
            else:
                record = f'{record} {line.rstrip()}'
        array.append(record)

    for passport in array:
        if not all(s in passport for s in search_strings):
            continue

        try:
            byr = re.search(r'byr:(\d{4})\b', passport).group(1)
            iyr = re.search(r'iyr:(\d{4})\b', passport).group(1)
            eyr = re.search(r'eyr:(\d{4})\b', passport).group(1)
            hgt = re.search(r'hgt:(\d{2,3})(cm|in)\b', passport)
            hcl = re.search(r'hcl:(#[\d\w]{6})\b', passport).group(1)
            ecl = re.search(r'ecl:(amb|blu|brn|gry|grn|hzl|oth)\b', passport).group(1)
            pid = re.search(r'pid:(\d{9})\b', passport).group(1)

            if int(byr) < 1920 or 2002 < int(byr):
                continue
            
            if int(iyr) < 2010 or 2020 < int(iyr):
                continue
            
            if int(eyr) < 2020 or 2030 < int(eyr):
                continue

            if hgt.group(2) == 'cm' and (int(hgt.group(1)) < 150 or 193 < int(hgt.group(1))):
                continue 
            elif hgt.group(2) == 'in' and (int(hgt.group(1)) < 59 or 76 < int(hgt.group(1))):
                continue

        except AttributeError:
            continue

        answer += 1

    return answer

ANSWER_EXAMPLE = main('example.txt')
ANSWER_INPUT = main('input.txt')

print(f'Example Input: {ANSWER_EXAMPLE}')
print(f'Puzzle Input: {ANSWER_INPUT}')
