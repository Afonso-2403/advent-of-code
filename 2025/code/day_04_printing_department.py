from pathlib import Path
import os

INPUT_FILES_DIR = f"{Path(__file__).parent}/../input_files/"
INPUT_FILE_PATH = INPUT_FILES_DIR + "day_04_input.txt"

def part_1():
    queue_of_rows = []
    num_accessible_rolls = 0

    with open(INPUT_FILE_PATH) as f:
        for line in f:
            line = line.rstrip()
            queue_of_rows.append(line)

            if len(queue_of_rows) == 2:    
                row_total, _ = process_row(queue_of_rows, 0)
                num_accessible_rolls += row_total
            
            if len(queue_of_rows) == 3:
                row_total, _ = process_row(queue_of_rows, 1)
                num_accessible_rolls += row_total
                queue_of_rows.pop(0)

    row_total, _ = process_row(queue_of_rows, 1)
    num_accessible_rolls += row_total

    print(num_accessible_rolls)

def count_adjacent(rows, x, y):
    """Count '@' around (r, c) including horizontal, vertical and diagonal."""
    offsets = [
        (-1, -1), (-1, 0), (-1, 1),
        (0,  -1),          (0,  1),
        (1,  -1), (1,  0), (1,  1),
    ]

    count = 0
    for dx, dy in offsets:
        pos_x, pos_y = x + dx, y + dy
        if 0 <= pos_x < len(rows) and 0 <= pos_y < len(rows[pos_x]):
            if rows[pos_x][pos_y] == "@":
                count += 1
    return count

def process_row(rows, row_index) -> tuple[int, set[int]]:
    """Count accessible rolls in a given row."""
    total = 0
    accessible_cols = set()
    for col, char in enumerate(rows[row_index]):
        if char == "@":
            neighbors = count_adjacent(rows, row_index, col)
            if neighbors < 4:
                total += 1
                accessible_cols.add(col)
                
    return total, accessible_cols

def part_2():
    file_number = 0
    file_to_write = INPUT_FILES_DIR + "temp_map_" + str(file_number) + ".txt"
    file_to_read = INPUT_FILE_PATH

    removed_rolls = 0

    while True:
        queue_of_rows: list[str] = []
        num_accessible_rolls = 0

        with open(file_to_read) as f:
            for line in f:
                line = line.rstrip()
                queue_of_rows.append(line)

                if len(queue_of_rows) == 2:    
                    row_total, cols_to_alter = process_row(queue_of_rows, 0)
                    num_accessible_rolls += row_total

                    row_to_write: str = ""
                    for col, char in enumerate(queue_of_rows[0]):
                        if col in cols_to_alter:
                            row_to_write += '.'
                        else:
                            row_to_write += char

                    with open(file_to_write, "w") as f:
                        f.write(row_to_write + '\n')
    
                if len(queue_of_rows) == 3:
                    row_total, cols_to_alter = process_row(queue_of_rows, 1)
                    num_accessible_rolls += row_total

                    row_to_write: str = ""
                    for col, char in enumerate(queue_of_rows[1]):
                        if col in cols_to_alter:
                            row_to_write += '.'
                        else:
                            row_to_write += char

                    queue_of_rows.pop(0)
                
                    with open(file_to_write, "a") as f:
                        f.write(row_to_write + '\n')

        row_total, cols_to_alter = process_row(queue_of_rows, 1)
        num_accessible_rolls += row_total

        row_to_write: str = ""
        for col, char in enumerate(queue_of_rows[1]):
            if col in cols_to_alter:
                row_to_write += '.'
            else:
                row_to_write += char

        with open(file_to_write, "a") as f:
            f.write(row_to_write + '\n')

        removed_rolls += num_accessible_rolls

        if num_accessible_rolls == 0:
            break

        file_to_read = file_to_write
        file_number = (file_number + 1) % 2
        file_to_write = INPUT_FILES_DIR + "temp_map_" + str(file_number) + ".txt"

    print(removed_rolls)

    if os.path.exists(INPUT_FILES_DIR + "temp_map_0.txt"):
        os.remove(INPUT_FILES_DIR + "temp_map_0.txt")
    else:
        print("The temp file 0 does not exist")

    if os.path.exists(INPUT_FILES_DIR + "temp_map_1.txt"):
        os.remove(INPUT_FILES_DIR + "temp_map_1.txt")
    else:
        print("The temp file 1 does not exist")

if __name__ == "__main__":
    part_2()


