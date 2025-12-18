from pathlib import Path

INPUT_FILE_PATH = f"{Path(__file__).parent}/../input_files/day_09_input.txt"

def part_1():
    red_tiles_list: list[tuple[int, int]] = []

    max_area = 0
    # Read all red tile locations and compute rectangle areas
    with open(INPUT_FILE_PATH) as f:
        for line in f:
            current_red_tile = line.strip().split(',')
            current_red_tile_tuple = (int(current_red_tile[0]), int(current_red_tile[1]))
            
            for red_tile in red_tiles_list:
                area = (abs(current_red_tile_tuple[0] - red_tile[0]) + 1) * (abs(current_red_tile_tuple[1] - red_tile[1]) + 1)
                if area > max_area:
                    max_area = area 
            
            red_tiles_list.append(current_red_tile_tuple)

    print(max_area)

if __name__ == "__main__":
    part_1()