from pathlib import Path

INPUT_FILE_PATH = f"{Path(__file__).parent}/../input_files/day_05_input.txt"

def part_1():
    fresh_counter = 0
    ranges_list: list[tuple[int, int]] = []
    processing_ranges = True

    with open(INPUT_FILE_PATH) as f:
        for line in f:
            line = line.rstrip()

            if not line:
                processing_ranges = False
                continue

            if processing_ranges and '-' in line:
                num_range = line.split('-')
                range_begin = int(num_range[0])
                range_end = int(num_range[1])

                if not ranges_list or range_begin > ranges_list[-1][1]:
                    ranges_list.append((range_begin, range_end))
                    continue

                for index, (begin, end) in enumerate(ranges_list):
                    if range_begin < begin or range_begin <= end:
                        range_begin = min(range_begin, begin)

                        if range_end < begin:
                            ranges_list = ranges_list[:index] + [(range_begin, range_end)] + ranges_list[index:]
                            break
                        elif range_end <= end or index == len(ranges_list) - 1 or range_end < ranges_list[index + 1][0]:
                            ranges_list[index] = (range_begin, max(range_end, end))
                            break
                        else:
                            stop_index = index + 1
                            while range_end > ranges_list[stop_index][1]:
                                stop_index += 1
                            if range_end >= ranges_list[stop_index][0]:
                                ranges_list[stop_index] = (range_begin, ranges_list[stop_index][1])
                                ranges_list = ranges_list[:index] + ranges_list[stop_index:]
                                break
                            else: 
                                ranges_list = ranges_list[:index] + [(range_begin, range_end)] + ranges_list[stop_index:]
                                break

            if not processing_ranges:
                ingredient_id = int(line)
                fresh = False
                for range_begin, range_end in ranges_list:
                    if range_begin <= ingredient_id <= range_end:
                        fresh = True                          
                        break
                if fresh:
                    fresh_counter += 1

    print(fresh_counter)

    return ranges_list

def part_2():
    ranges_list = part_1()
    total_fresh_ingredients = 0

    for range_start, range_end in ranges_list:
        total_fresh_ingredients += range_end - range_start + 1
    
    print(total_fresh_ingredients)

if __name__ == "__main__":
    part_2()