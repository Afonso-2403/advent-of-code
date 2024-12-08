from pathlib import Path
from functools import reduce
from operator import mul, add

INPUT_FILE_PATH = f"{Path(__file__).parent}/../input_files/day_7_input.txt"

def part_1():

    test_value_to_operands_dict = {}

    with open(INPUT_FILE_PATH, 'r') as f:
        for line in f:
            splitted_line = line.split(":")
            test_value_to_operands_dict[int(splitted_line[0])] = [int(x) for x in splitted_line[1].strip().split(" ")]

    # print(test_value_to_operands_dict)

    total_calibration_result = 0
    found_keys = set()
    for key, value in test_value_to_operands_dict.items():
        if search_all_possible_combinations(key, value):
            # print(f"Found value {key} with operands {value}")
            total_calibration_result += key
            found_keys.add(key)
    print(f"Total calibration result: {total_calibration_result}")

    total_calibration_result_eivind = 0
    found_keys_eivind = set()
    for key, value in test_value_to_operands_dict.items():
        if key in eivind_solution(value, key):
            # print(f"Found value {key} with operands {value}")
            total_calibration_result_eivind += key
            found_keys_eivind.add(key)

    print(f"Total calibration result_eivind: {total_calibration_result_eivind}")

    for key in found_keys.symmetric_difference(found_keys_eivind):
        print(f"Key {key} not found")

def search_all_possible_combinations(test_value, operands):
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
    return {n * c for c in r}.union({n + c for c in r})

def part_2():
    pass

if __name__ == "__main__":
    part_1()