INPUT_FILE = "../input_files/day_2_input.txt"


def exercise_1():

    total_points = 0
    possibilities_dict = {"A X": 4, "B X": 1, "C X": 7, "A Y": 8, "B Y": 5, "C Y": 2, "A Z": 3, "B Z": 9, "C Z": 6}

    with open(INPUT_FILE) as input_file:
        for line in input_file:
            total_points += possibilities_dict[line.strip()]

    print(total_points)


def exercise_2():

    total_points = 0
    possibilities_dict = {"A X": 3, "B X": 1, "C X": 2, "A Y": 4, "B Y": 5, "C Y": 6, "A Z": 8, "B Z": 9, "C Z": 7}

    with open(INPUT_FILE) as input_file:
        for line in input_file:
            total_points += possibilities_dict[line.strip()]

    print(total_points)


def main():
    # exercise_1()
    exercise_2()


if __name__ == "__main__":
    main()