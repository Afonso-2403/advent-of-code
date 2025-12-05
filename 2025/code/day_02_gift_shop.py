from pathlib import Path

INPUT_FILE_PATH = f"{Path(__file__).parent}/../input_files/day_02_input.txt"

def part_1():
    counter = 0

    with open(INPUT_FILE_PATH) as f:
        list_of_ranges = f.readline().split(',')
        for num_range in list_of_ranges:
            for number in range(int(num_range.split('-')[0]), int(num_range.split('-')[1]) + 1):
                string_number = str(number)
                if len(string_number) % 2 == 0 and string_number[:len(string_number) // 2] == string_number[len(string_number) // 2:]:
                    counter += number

    print(counter)

def part_2():
    counter = 0

    with open(INPUT_FILE_PATH) as f:
        list_of_ranges = f.readline().split(',')
        for num_range in list_of_ranges:
            for number in range(int(num_range.split('-')[0]), int(num_range.split('-')[1]) + 1):
                string_number = str(number)

                for i in range(1, len(string_number) // 2 + 1):
                    pattern = string_number[:i]
                    index = i
                    while string_number[index:].find(pattern) == 0:
                        index = index + i
                    if index == len(string_number):
                        counter += number
                        break
    print(counter)


if __name__ == "__main__":
    part_2()