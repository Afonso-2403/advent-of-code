from pathlib import Path
import re
from itertools import product

INPUT_FILE_PATH = f"{Path(__file__).parent}/../input_files/day_10_input.txt"

def part_1():
    total = solve(INPUT_FILE_PATH)
    print(total)

# ChatGPT solution with Gaussian elimination
def parse_line(line):
    parts = line.strip().split()

    # 1. Pattern
    pattern = parts[0][1:-1]  # remove [ ]
    target = [1 if c == "#" else 0 for c in pattern]

    groups = []
    values = None

    for p in parts[1:]:
        if p.startswith("("):
            nums = tuple(map(int, p[1:-1].split(",")))
            groups.append(nums)
        elif p.startswith("{"):
            values = list(map(int, p[1:-1].split(",")))

    return {
        "target": target,
        "groups": groups,
        "values": values
    }

def parse_line_regex(line):
    tuple_re = re.compile(r"\((.*?)\)")
    brace_re = re.compile(r"\{(.*?)\}")

    pattern = re.search(r"\[(.*?)\]", line).group(1)

    groups = [
        tuple(map(int, t.split(",")))
        for t in tuple_re.findall(line)
    ]

    values = list(
        map(int, brace_re.search(line).group(1).split(","))
    )

    return {
        "pattern": pattern,
        "groups": groups,
        "values": values
    }

def min_presses_gaussian_elimination(target, buttons):
    n = len(target)
    m = len(buttons)

    # Build matrix A (n x m)
    A = [[0]*m for _ in range(n)]
    for j, btn in enumerate(buttons):
        for i in btn:
            A[i][j] ^= 1

    # Augmented matrix
    M = [A[i] + [target[i]] for i in range(n)]

    row = 0
    pivots = []
    for col in range(m):
        # Find pivot
        pivot = None
        for r in range(row, n):
            if M[r][col]:
                pivot = r
                break
        if pivot is None:
            continue

        M[row], M[pivot] = M[pivot], M[row]
        pivots.append(col)

        # Eliminate
        for r in range(n):
            if r != row and M[r][col]:
                for c in range(col, m+1):
                    M[r][c] ^= M[row][c]

        row += 1

    # Check consistency
    for r in range(row, n):
        if M[r][-1]:
            return float("inf")  # No solution

    free_vars = [i for i in range(m) if i not in pivots]
    best = float("inf")

    # Enumerate free variables
    for assignment in product([0,1], repeat=len(free_vars)):
        x = [0]*m
        for idx, val in zip(free_vars, assignment):
            x[idx] = val

        for r, col in enumerate(pivots):
            s = M[r][-1]
            for c in free_vars:
                if M[r][c]:
                    s ^= x[c]
            x[col] = s

        best = min(best, sum(x))

    return best

def solve(input_file_path):
    total = 0
    with open(input_file_path) as f:
        for line in f:
            parsed_line = parse_line(line)

            total += min_presses_gaussian_elimination(parsed_line["target"], parsed_line["groups"])
        return total



if __name__ == "__main__":
    part_1()
