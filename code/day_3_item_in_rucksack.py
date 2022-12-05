INPUT_FILE = "day_3_input.txt"


def exercise_1():

    total_points = 0

    with open(INPUT_FILE) as input_file:
        for line in input_file:
            character_dict = {}
            parsed_line = line.rstrip()

            first_half = line[:(len(parsed_line)//2)]
            second_half = line[(len(parsed_line)//2):]

            for character in first_half:
                character_dict[character] = True

            for character in set(second_half):
                if character in character_dict:
                    distance_from_A = ord(character) - ord('A')
                    if distance_from_A < 26:
                        total_points += distance_from_A + 27
                    else:
                        total_points += ord(character) - ord('a') + 1
                    
                    break

    print(total_points)

def exercise_2():

    line_number=0
    total_points = 0
    character_dict = {}

    with open(INPUT_FILE) as input_file:
        for line in input_file:
            parsed_line = line.rstrip()

            for character in set(parsed_line):
                if character not in character_dict:
                    character_dict[character] = 1
                else:
                    character_dict[character] += 1
                    if character_dict[character] == 3:
                        distance_from_A = ord(character) - ord('A')
                        if distance_from_A < 26:
                            total_points += distance_from_A + 27
                        else:
                            total_points += ord(character) - ord('a') + 1

            if(line_number % 3 == 2):
                character_dict = {}

            line_number += 1

    print(total_points)


def main():
    # exercise_1()
    exercise_2()


if __name__ == "__main__":
    main()