from pathlib import Path
import re

INPUT_FILE_PATH = f"{Path(__file__).parent}/../input_files/day_3_input.txt"

def part_1():
    pattern = r"mul\(\d+,\d+\)"
    digit_pattern = r"\d+"

    total = 0
    with open(INPUT_FILE_PATH) as f:
        for line in f:
            occurences = re.findall(pattern, line)

            for occurence in occurences:
                digits = re.findall(digit_pattern, occurence)
                total += int(digits[0]) * int(digits[1])
    
    print(total)

def part_2():
    enabled = True
    total = 0
    multiplications_pattern = r"mul\(\d+,\d+\)"
    digit_pattern = r"\d+"

    def find_all_valid_instructions_in_one_line(line, enabled=True, total=0):
        if len(line)== 0:
            return enabled, total
        
        if enabled:
            splitted_line = line.split("don't()", 1)

            occurences = re.findall(multiplications_pattern, splitted_line[0])
            for occurence in occurences:
                digits = re.findall(digit_pattern, occurence)
                total += int(digits[0]) * int(digits[1])
            
            if len(splitted_line) == 1:
                return enabled, total
            else:
                return find_all_valid_instructions_in_one_line(splitted_line[1], False, total)
        else:
            splitted_line = line.split("do()", 1)
            
            if len(splitted_line) == 1:
                return enabled, total
            else:
                return find_all_valid_instructions_in_one_line(splitted_line[1], True, total)

    with open(INPUT_FILE_PATH) as f:
        for line in f:
            enabled, total = find_all_valid_instructions_in_one_line(line, enabled, total)

    print(total)


if __name__ == "__main__":
    part_2()