from pathlib import Path
import re

INPUT_FILE_PATH = f"{Path(__file__).parent}/../input_files/day_4_input.txt"


def search_directions_cross(matrix, word):
    total = 0
    direction_southeast = (1, 1)
    direction_southwest = (1, -1)
    direction_northeast = (-1, 1)
    direction_northwest = (-1, -1)

    for i, line in enumerate(matrix[1:-1]):
        for j, character in enumerate(line[1:-1]):
            if character == word[1]:
                if (
                    matrix[i + 1 + direction_northwest[0]][j + 1 + direction_northwest[1]] == word[0]
                    and matrix[i + 1 + direction_southeast[0]][j + 1 + direction_southeast[1]] == word[2]
                    or (
                        matrix[i + 1 + direction_northwest[0]][j + 1 + direction_northwest[1]] == word[2]
                        and matrix[i + 1 + direction_southeast[0]][j + 1 + direction_southeast[1]] == word[0]
                    )
                ):
                    if (
                        matrix[i + 1 + direction_northeast[0]][j + 1 + direction_northeast[1]] == word[0]
                        and matrix[i + 1 + direction_southwest[0]][j + 1 + direction_southwest[1]] == word[2]
                        or (
                            matrix[i + 1 + direction_northeast[0]][j + 1 + direction_northeast[1]] == word[2]
                            and matrix[i + 1 + direction_southwest[0]][j + 1 + direction_southwest[1]] == word[0]
                        )
                    ):
                        total += 1
    return total

def part_1():
    total = 0
    word = "XMAS"
    with open(INPUT_FILE_PATH, 'r') as f:
        matrix = f.read().splitlines()

    total = 0
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    for i, line in enumerate(matrix):
        for j, character in enumerate(line):
            if character == word[0]:
                for direction in directions:
                    for k in range(1, len(word)):
                        if i + direction[0]*k >= len(matrix) or i + direction[0]*k < 0 or j + direction[1]*k >= len(matrix[0]) or j + direction[1]*k < 0:
                            break
                        if matrix[i + direction[0]*k][j + direction[1]*k] != word[k]:
                            break
                        elif k == len(word) - 1:
                            total += 1

    print(total)


def part_2():
    total = 0
    with open(INPUT_FILE_PATH, 'r') as f:
        matrix = f.read().splitlines()

    total = 0
    word = "MAS"
    direction_southeast = (1, 1)
    direction_southwest = (1, -1)
    direction_northeast = (-1, 1)
    direction_northwest = (-1, -1)

    for i, line in enumerate(matrix[1:-1]):
        for j, character in enumerate(line[1:-1]):
            if character == word[1]:
                if (
                    matrix[i + 1 + direction_northwest[0]][j + 1 + direction_northwest[1]] == word[0]
                    and matrix[i + 1 + direction_southeast[0]][j + 1 + direction_southeast[1]] == word[2]
                    or (
                        matrix[i + 1 + direction_northwest[0]][j + 1 + direction_northwest[1]] == word[2]
                        and matrix[i + 1 + direction_southeast[0]][j + 1 + direction_southeast[1]] == word[0]
                    )
                ):
                    if (
                        matrix[i + 1 + direction_northeast[0]][j + 1 + direction_northeast[1]] == word[0]
                        and matrix[i + 1 + direction_southwest[0]][j + 1 + direction_southwest[1]] == word[2]
                        or (
                            matrix[i + 1 + direction_northeast[0]][j + 1 + direction_northeast[1]] == word[2]
                            and matrix[i + 1 + direction_southwest[0]][j + 1 + direction_southwest[1]] == word[0]
                        )
                    ):
                        total += 1

    print(total)


if __name__ == "__main__":
    part_2()