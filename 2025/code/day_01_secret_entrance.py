from pathlib import Path

INPUT_FILE_PATH = f"{Path(__file__).parent}/../input_files/day_01_input.txt"

def part_1():
    position = 50
    counter = 0

    with open(INPUT_FILE_PATH) as f:
        for line in f:
            direction = line[0]
            amplitude = int(line[1:]) if direction == 'R' else -int(line[1:])

            position += amplitude
            while position < 0:
                position += 100
            if position >= 100:
                position %= 100
            if position == 0:
                counter += 1

    print(counter)

def part_2():
    position = 50
    prev_position_was_0 = False
    counter = 0

    with open(INPUT_FILE_PATH) as f:
        for line in f:
            direction = line[0]
            amplitude = int(line[1:]) if direction == 'R' else -int(line[1:])

            end = (position + amplitude) % 100

            # number of times we pass zero:
            laps = abs(amplitude) // 100

            # check if we cross zero once more within the partial lap
            crossed = 0

            if amplitude > 0:   # R
                if end < position and position != 0:
                    crossed = 1
            
            else:              # L
                if position != 0:
                    if end > position or end == 0:
                        crossed = 1

            position = end
            counter += laps + crossed

    print(counter)


if __name__ == "__main__":
    part_2()