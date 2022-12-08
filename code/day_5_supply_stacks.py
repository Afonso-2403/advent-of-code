INPUT_FILE = "../input_files/day_5_input_instructions.txt"


def exercise_1():

    stacks = {
        '1': ['W','D', 'G', 'B', 'H', 'R', 'V'],
        '2': ['J', 'N', 'G', 'C', 'R', 'F'],
        '3': ['L', 'S', 'F', 'H', 'D', 'N', 'J'],
        '4': ['J', 'D', 'S', 'V'],
        '5': ['S', 'H', 'D', 'R', 'Q', 'W', 'N', 'V'],
        '6': ['P', 'G', 'H', 'C', 'M'],
        '7': ['F', 'J', 'B', 'G', 'L', 'Z', 'H', 'C'],
        '8': ['S', 'J', 'R'],
        '9': ['L', 'G', 'S', 'R', 'B', 'N', 'V', 'M']
    }

    with open(INPUT_FILE) as input_file:
        for line in input_file:
            parsed_line = line.strip().split(' ')
            for i in range(int(parsed_line[1])):
                stacks[parsed_line[5]].append(stacks[parsed_line[3]].pop())


    for stack in stacks:
        print(stacks[stack][-1], end='')

def exercise_2():

    stacks = {
        '1': ['W','D', 'G', 'B', 'H', 'R', 'V'],
        '2': ['J', 'N', 'G', 'C', 'R', 'F'],
        '3': ['L', 'S', 'F', 'H', 'D', 'N', 'J'],
        '4': ['J', 'D', 'S', 'V'],
        '5': ['S', 'H', 'D', 'R', 'Q', 'W', 'N', 'V'],
        '6': ['P', 'G', 'H', 'C', 'M'],
        '7': ['F', 'J', 'B', 'G', 'L', 'Z', 'H', 'C'],
        '8': ['S', 'J', 'R'],
        '9': ['L', 'G', 'S', 'R', 'B', 'N', 'V', 'M']
    }

    with open(INPUT_FILE) as input_file:
        for line in input_file:
            parsed_line = line.strip().split(' ')

            stacks[parsed_line[5]] = stacks[parsed_line[5]] + stacks[parsed_line[3]][-int(parsed_line[1]):]
            stacks[parsed_line[3]] = stacks[parsed_line[3]][:-int(parsed_line[1])]

    for stack in stacks:
        print(stacks[stack][-1], end='')


def main():
    # exercise_1()
    exercise_2()


if __name__ == "__main__":
    main()