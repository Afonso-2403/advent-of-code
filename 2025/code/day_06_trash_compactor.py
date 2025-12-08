from pathlib import Path
from functools import reduce
from operator import mul

INPUT_FILE_PATH = f"{Path(__file__).parent}/../input_files/day_06_input.txt"

def part_1():
    operands_lists: list[list[int]] = []
    is_first_line = True
    operators_list = []
    grand_total = 0

    with open(INPUT_FILE_PATH) as f:
        for line in f:
            operands_line = line.rstrip().split()
            if '+' in operands_line or '*' in operands_line:
                operators_list = operands_line
                break
            if is_first_line:
                for index, operand in enumerate(operands_line):
                    operands_lists.append([int(operand)])
                is_first_line = False
            else:
                for index, operand in enumerate(operands_line):
                    operands_lists[index].append(int(operand))
            
        
    if not operators_list:
        raise Exception("There were no operators in the file")
    
    for index, operands_list in enumerate(operands_lists):
        if operators_list[index] == '+':
            grand_total += sum(operands_list)
        if operators_list[index] == '*':
            grand_total += reduce(mul, operands_list)
    
    print(grand_total)


def part_2():
    result = solve_cephalopod_math()
    print(result)

def solve_cephalopod_math():
    # Read the input file
    with open(INPUT_FILE_PATH) as f:
        lines = f.readlines()
    
    lines = [line.rstrip("\n") for line in lines]    
    height = len(lines)
    width = len(lines[0])
    op_row_idx = height - 1
    
    total = 0
    
    # Find all operator positions (left-to-right in the operator row)
    operator_positions = []
    for col in range(width):
        if lines[op_row_idx][col] in '+*':
            operator_positions.append((col, lines[op_row_idx][col]))
    
    # For each operator, find the problem's extent (columns to the right)
    for op_idx, (op_col, op_char) in enumerate(operator_positions):
        # Find right boundary: either next operator's column or end of input
        if op_idx + 1 < len(operator_positions):
            right_bound = operator_positions[op_idx + 1][0]
        else:
            right_bound = width
        
        # Extract all columns from op_col to right_bound (exclusive)
        problem_cols = list(range(op_col, right_bound))
        
        # Extract numbers from these columns (read top-to-bottom in each column)
        numbers = []
        for col in problem_cols:
            # Build the number from this column (top-to-bottom)
            num_str = ""
            for row in range(op_row_idx):
                ch = lines[row][col]
                if ch == " ":
                    # Space breaks the number
                    if num_str:
                        numbers.append(int(num_str))
                        num_str = ""
                else:
                    num_str += ch
            # Don't forget the last number in this column
            if num_str:
                numbers.append(int(num_str))
                
        # Compute the result
        if op_char == '+':
            result = sum(numbers)
        else:  # '*'
            result = 1
            for n in numbers:
                result *= n
        
        total += result
    
    return total


if __name__ == "__main__":
    part_2()