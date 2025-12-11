from pathlib import Path

INPUT_FILE_PATH = f"{Path(__file__).parent}/../input_files/day_08_input.txt"

def part_1():
    distance_to_pairs_dict: dict[int, list[tuple[tuple[int, int, int], tuple[int, int, int]]]] = dict()
    boxes_list: list[tuple[int, int, int]] = []

    with open(INPUT_FILE_PATH) as f:
        for line in f:
            current_box = line.strip().split(',')
            current_box_tuple = (int(current_box[0]), int(current_box[1]), int(current_box[2]))
            for box in boxes_list:
                distance_squared = pow(current_box_tuple[0] - box[0], 2) + pow(current_box_tuple[1] - box[1], 2) + pow(current_box_tuple[2] - box[2], 2)
                if distance_squared in distance_to_pairs_dict:
                    distance_to_pairs_dict[distance_squared].append((box, current_box_tuple))
                else:
                    distance_to_pairs_dict[distance_squared] = [(box, current_box_tuple)]

            boxes_list.append(current_box_tuple)

    distance_to_pairs_dict = dict(sorted(distance_to_pairs_dict.items()))
    handled_pairs = 0
    connected_junctions_dict: dict[tuple[int, int, int], int] = dict()
    connections_counts: list[int] = []

    for _, list_of_pairs in distance_to_pairs_dict.items():
        for junction_1, junction_2 in list_of_pairs:
            if junction_1 in connected_junctions_dict:
                set_index = connected_junctions_dict[junction_1]
                connected_junctions_dict[junction_2] = set_index
                connections_counts[set_index] += 1

            elif junction_2 in connected_junctions_dict:
                set_index = connected_junctions_dict[junction_2]
                connected_junctions_dict[junction_1] = set_index
                connections_counts[set_index] += 1
            
            else:
                set_index = len(connections_counts)
                connected_junctions_dict[junction_1] = set_index
                connected_junctions_dict[junction_2] = set_index
                connections_counts.append(2)

            handled_pairs += 1

        if handled_pairs == 1000:
            break

    connections_counts = sorted(connections_counts, reverse=True)

    result = 1
    for i in range(3):
        result *= connections_counts[i]

    print(result)
    

if __name__ == "__main__":
    part_1()