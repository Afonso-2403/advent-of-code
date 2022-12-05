import requests


INPUT_FILE = "../input_files/day_1_input.txt"

def exercise_1():
    # puzzle_input = requests.get("https://adventofcode.com/2022/day/1/input")

    # with open("output.txt", "w") as teste:
    #     teste.write(puzzle_input.text)

    elf_number = 1
    elf_number_calories = [0, 0]
    current_sum = 0

    with open(INPUT_FILE) as input_file:
        for line in input_file:
            if line == "\n":
                if current_sum > elf_number_calories[1]:
                    elf_number_calories[0] = elf_number
                    elf_number_calories[1] = current_sum

                elf_number += 1
                current_sum = 0

            else:
                current_sum += int(line)

        if current_sum > elf_number_calories[1]:
            elf_number_calories[0] = elf_number
            elf_number_calories[1] = current_sum

    print(f"Elf with most calories is number {elf_number_calories[0]} with {elf_number_calories[1]}")

def exercise_2():

    elf_number = 1
    top_3_number_calories = [0, 0, 0]
    current_sum = 0

    with open(INPUT_FILE) as input_file:
        for line in input_file:
            if line == "\n":
                if current_sum >= top_3_number_calories[0]:
                    top_3_number_calories[2] = top_3_number_calories[1]
                    top_3_number_calories[1] = top_3_number_calories[0]
                    top_3_number_calories[0] = current_sum

                elif current_sum >= top_3_number_calories[1]:
                    top_3_number_calories[2] = top_3_number_calories[1]
                    top_3_number_calories[1] = current_sum

                elif current_sum > top_3_number_calories[2]:
                    top_3_number_calories[2] = current_sum

                elf_number += 1
                current_sum = 0

            else:
                current_sum += int(line)

        if current_sum >= top_3_number_calories[0]:
            top_3_number_calories[2] = top_3_number_calories[1]
            top_3_number_calories[1] = top_3_number_calories[0]
            top_3_number_calories[0] = current_sum

        elif current_sum >= top_3_number_calories[1]:
            top_3_number_calories[2] = top_3_number_calories[1]
            top_3_number_calories[1] = current_sum

        elif current_sum > top_3_number_calories[2]:
            top_3_number_calories[2] = current_sum

    print(f"Top 3 are {top_3_number_calories[0]}, {top_3_number_calories[1]} and {top_3_number_calories[2]}")
    print(f"Sum of the 3 is {top_3_number_calories[0] + top_3_number_calories[1] + top_3_number_calories[2]}")

def main():
    # exercise_1()
    exercise_2()

if __name__ == "__main__":
    main()