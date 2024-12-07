from pathlib import Path
import re

INPUT_FILE_PATH = f"{Path(__file__).parent}/../input_files/day_5_input.txt"

def part_1_and_part_2(part_1: bool = True):
    total = 0
    looking_for_rules = True
    rules_forward: dict[int, set[int]] = dict()
    rules_backward: dict[int, set[int]] = dict()

    with open(INPUT_FILE_PATH, 'r') as f:
        for index, line in enumerate(f):
            if line == '\n':
                print(f"Found a blank line at index {index}")
                # print(rules_forward)
                # print(rules_backward)
                looking_for_rules = False
                continue

            if looking_for_rules:
                splitted_line = line.split('|')
                rules_forward[int(splitted_line[0])] = rules_forward.get(int(splitted_line[0]), set())
                rules_forward[int(splitted_line[0])].add(int(splitted_line[1]))
                rules_backward[int(splitted_line[1])] = rules_backward.get(int(splitted_line[1]), set())
                rules_backward[int(splitted_line[1])].add(int(splitted_line[0]))

            else:
                valid_update = True
                
                previous_numbers = set()
                splitted_line = line.split(',')

                for number in splitted_line:
                    previous_numbers.add(int(number))
                    if rules_forward.get(int(number)) and rules_forward.get(int(number)).intersection(previous_numbers):
                        valid_update = False
                        break

                if valid_update:
                    if part_1:
                        total += int(splitted_line[len(splitted_line) // 2])

                else:
                    if not part_1:
                        correctly_ordered = [int(splitted_line[0])]
                        for number_to_insert in splitted_line[1:]:
                            for index_to_insert in range(len(correctly_ordered)):
                                if not rules_backward.get(int(number_to_insert)):
                                    correctly_ordered.insert(index_to_insert, int(number_to_insert))
                                    break
                                if correctly_ordered[index_to_insert] in rules_backward[int(number_to_insert)]:
                                    if index_to_insert == len(correctly_ordered) - 1:
                                        correctly_ordered.insert(index_to_insert + 1, int(number_to_insert))
                                        break
                                    else:
                                        index_to_insert += 1
                                else:
                                    correctly_ordered.insert(index_to_insert, int(number_to_insert))
                                    break

                        total += int(correctly_ordered[len(correctly_ordered) // 2])


    print(total)

if __name__ == "__main__":
    part_1_and_part_2(False)