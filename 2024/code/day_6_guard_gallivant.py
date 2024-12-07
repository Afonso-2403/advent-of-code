from pathlib import Path

INPUT_FILE_PATH = f"{Path(__file__).parent}/../input_files/day_6_input.txt"

DIRECTION_NORTH = (-1, 0)
DIRECTION_EAST = (0, 1)
DIRECTION_SOUTH = (1, 0)
DIRECTION_WEST = (0, -1)

DIRECTIONS_ROTATION_INDEX = [DIRECTION_NORTH, DIRECTION_EAST, DIRECTION_SOUTH, DIRECTION_WEST]

def part_1():

    with open(INPUT_FILE_PATH, 'r') as f:
        matrix = f.read().splitlines()

    current_position, current_direction, current_direction_index = find_current_position_and_direction(matrix)

    covered_positions = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

    while True:
        covered_positions[current_position[0]][current_position[1]] = 1
        current_position, current_direction, current_direction_index = move_or_rotate(current_position, current_direction, current_direction_index, matrix)
        
        if not (0 <= current_position[0] < len(matrix) and 0 <= current_position[1] < len(matrix[0])):
            break

    print(f"part_1 answer: {sum([sum(row) for row in covered_positions])}")
    return covered_positions

def part_2():
    covered_positions_part_1 = part_1()
    with open(INPUT_FILE_PATH, 'r') as f:
        matrix = f.read().splitlines()

    starting_position, starting_direction, starting_direction_index = find_current_position_and_direction(matrix)

    found_loops = 0
    for row, line in enumerate(matrix):
        for column, character in enumerate(line):
            if covered_positions_part_1[row][column] == 0:
                continue

            covered_positions = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

            current_position = starting_position
            current_direction = starting_direction
            current_direction_index = starting_direction_index

            if character == '#' or (row,column) == current_position:
                continue

            temp_list = list(matrix[row])
            temp_list[column] = '#'
            matrix[row] = "".join(temp_list)

            portential_loop = False
            while True:
                if covered_positions[current_position[0]][current_position[1]] > 2:
                    portential_loop = True

                covered_positions[current_position[0]][current_position[1]] += 1
                current_position, current_direction, current_direction_index = move_or_rotate(current_position, current_direction, current_direction_index, matrix)
                
                if not (0 <= current_position[0] < len(matrix) and 0 <= current_position[1] < len(matrix[0])):
                    break

                # Assume it is a loop if the nodes in this order have been visited more than 2 times
                if covered_positions[current_position[0]][current_position[1]] > 2 and portential_loop:
                    found_loops += 1
                    break
                
                else:
                    portential_loop = False

            temp_list = list(matrix[row])
            temp_list[column] = '.'
            matrix[row] = "".join(temp_list)

    print(f"part_2 answer: {found_loops}")

def find_current_position_and_direction(matrix) -> tuple[tuple[int, int], tuple[int, int], int]:
    for row, line in enumerate(matrix):
        for column, character in enumerate(line):
            match character:
                case '^':
                    current_position = (row, column)
                    current_direction = DIRECTION_NORTH
                    return current_position, current_direction, 0
                case '>':
                    current_position = (row, column)
                    current_direction = DIRECTION_EAST
                    return current_position, current_direction, 1
                case 'v':
                    current_position = (row, column)
                    current_direction = DIRECTION_SOUTH
                    return current_position, current_direction, 2
                case '<':
                    current_position = (row, column)
                    current_direction = DIRECTION_WEST
                    return current_position, current_direction, 3

def move_or_rotate(current_position, current_direction, current_direction_index, matrix):
    next_position = (current_position[0] + current_direction[0], current_position[1] + current_direction[1])
    next_direction = current_direction
    next_direction_index = current_direction_index

    if 0 <= next_position[0] < len(matrix) and 0 <= next_position[1] < len(matrix):    
        if matrix[next_position[0]][next_position[1]] == '#':
            next_direction_index = (current_direction_index+1)%len(DIRECTIONS_ROTATION_INDEX)
            next_direction = DIRECTIONS_ROTATION_INDEX[next_direction_index]
            next_position = current_position
    
    return next_position, next_direction, next_direction_index



if __name__ == "__main__":
    part_2()