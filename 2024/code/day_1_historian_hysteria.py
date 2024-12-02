from pathlib import Path

INPUT_FILE_PATH = f"{Path(__file__).parent}/../input_files/day_1_input.txt"

def part_1():
    left_list = []
    right_list = []

    with open("day_1_input.txt") as f:
        for line in f:
            splitted_line = line.split()
            left_list.append(int(splitted_line[0]))
            right_list.append(int(splitted_line[1]))

    left_list.sort()
    right_list.sort()

    total_difference = 0
    for left_element, right_element in zip(left_list, right_list):
        total_difference += abs(right_element - left_element)
    
    print(total_difference)
        
    
def part_2():
    left_list = []
    right_list_dict = {}

    with open(INPUT_FILE_PATH) as f:
        for line in f:
            splitted_line = line.split()
            left_list.append(int(splitted_line[0]))
            if right_list_dict.get(int(splitted_line[1])):
                right_list_dict[int(splitted_line[1])] += 1
            else:
                right_list_dict[int(splitted_line[1])] = 1

    similarity_score = 0
    for left_element in left_list:
        if right_list_dict.get(left_element):
            similarity_score += left_element * right_list_dict[left_element]

    print(similarity_score)

if __name__ == "__main__":
    part_2()