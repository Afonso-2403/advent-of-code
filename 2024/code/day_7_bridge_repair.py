from pathlib import Path
from functools import reduce
from operator import mul, add

INPUT_FILE_PATH = f"{Path(__file__).parent}/../input_files/day_7_input.txt"

def part_1():
    test_values = []
    operands = []

    with open(INPUT_FILE_PATH, 'r') as f:
        for line in f:
            splitted_line = line.split(":")
            test_values.append(int(splitted_line[0])) 
            operands.append([int(x) for x in splitted_line[1].strip().split(" ")])

    total_calibration_result = 0
    for test_value, operands in zip(test_values, operands):
        if search_all_possible_combinations(test_value, operands):
            total_calibration_result += test_value
    print(f"Total calibration result: {total_calibration_result}")

def search_all_possible_combinations(test_value, operands, part_2=False):
    if len(operands) == 1:
        return test_value == operands[0]
    
    new_test_value = test_value - operands[-1]
    if search_all_possible_combinations(new_test_value, operands[:-1]):
        return True

    new_test_value = test_value / operands[-1]
    if int(new_test_value) == new_test_value:
        if search_all_possible_combinations(new_test_value, operands[:-1]):
            return True
    
    return False

def eivind_solution(nums, test):
    if len(nums) == 0:
        return set()
    if len(nums) == 1:
        return {nums[0]}

    rest = nums[0:-1]
    n = nums[-1]
    r = eivind_solution(rest, test)
    r = {c for c in r if c <= test}
    return {n * c for c in r}.union({n + c for c in r}).union({int(str(c) + str(n)) for c in r})

def part_2():
    test_values = []
    operands = []

    with open(INPUT_FILE_PATH, 'r') as f:
        for line in f:
            splitted_line = line.split(":")
            test_values.append(int(splitted_line[0])) 
            operands.append([int(x) for x in splitted_line[1].strip().split(" ")])

    total_calibration_result = 0
    for test_value, operands in zip(test_values, operands):
        if test_value in eivind_solution(operands, test_value):
            total_calibration_result += test_value
    print(f"Total calibration result: {total_calibration_result}")

if __name__ == "__main__":
    part_2()