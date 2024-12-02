INPUT_FILE = "../input_files/day_4_input.txt"


def exercise_1():

    total_contained_pairs = 0

    with open(INPUT_FILE) as input_file:
        for line in input_file:
            split_line = line.rstrip().split(",")
            range_1 = split_line[0].split("-")
            range_2 = split_line[1].split("-")

            if (
                (int(range_1[0]) <= int(range_2[0]) and int(range_1[1]) >= int(range_2[1])) 
                or (int(range_2[0]) <= int(range_1[0]) and int(range_2[1]) >= int(range_1[1]))
            ):
                total_contained_pairs += 1

    print(total_contained_pairs)

def exercise_2():

    total_overlap_pairs = 0

    with open(INPUT_FILE) as input_file:
        for line in input_file:
            split_line = line.rstrip().split(",")
            range_1 = split_line[0].split("-")
            range_2 = split_line[1].split("-")

            if (
                (int(range_1[0]) <= int(range_2[0]) and int(range_1[1]) >= int(range_2[0])) 
                or (int(range_2[0]) <= int(range_1[0]) and int(range_2[1]) >= int(range_1[0]))
            ):
                total_overlap_pairs += 1

    print(total_overlap_pairs)


def main():
    # exercise_1()
    exercise_2()


if __name__ == "__main__":
    main()