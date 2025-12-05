from pathlib import Path
import platform

INPUT_FILE_PATH = f"{Path(__file__).parent}/../input_files/day_03_input.txt"

def part_1():
    joltage_counter = 0

    with open(INPUT_FILE_PATH) as f:
        for battery_bank in f:
            battery_bank = battery_bank.rstrip()
            (max, index) = find_maximum_cell(battery_bank)
            if index != len(battery_bank) - 1:
                (second_max, _) = find_maximum_cell(battery_bank[index + 1:])
            else:
                second_max = max
                (max, _) = find_maximum_cell(battery_bank[:-1])
            
            joltage_counter += int(str(max) + str(second_max))

    print(joltage_counter)

def part_2():
    if platform.architecture()[0] == '32bit':
        raise OverflowError("This code can only run on 64bit systems")

    BATTERY_SIZE = 12
    joltage_counter = 0

    with open(INPUT_FILE_PATH) as f:
        for battery_bank in f:
            battery_bank = battery_bank.rstrip()

            current_battery = battery_bank[-BATTERY_SIZE:]
            current_max = int(current_battery[0])
            for index in range(-BATTERY_SIZE - 1, -len(battery_bank) - 1, -1):
                if int(battery_bank[index]) >= current_max:
                    for i in range(1,12):
                        if int(current_battery[i]) <= current_max:
                            temp = int(current_battery[i])
                            current_battery = current_battery[:i] + str(current_max) + current_battery[i+1:]
                            current_max = temp
                        else:
                            break
                    
                    current_battery =  battery_bank[index] + current_battery[1:]
                    current_max = int(battery_bank[index])

            joltage_counter += int(current_battery)

        #     # Alternative approach by Github Copilot:
        #     # Build the lexicographically largest subsequence of length BATTERY_SIZE
        #     # using a greedy stack algorithm.
        #     s = battery_bank
        #     n = len(s)
        #     k = BATTERY_SIZE
        #     to_remove = n - k
        #     stack: list[str] = []
        #     for ch in s:
        #         while stack and to_remove > 0 and stack[-1] < ch:
        #             stack.pop()
        #             to_remove -= 1
        #         stack.append(ch)

        #     # The result is the first k elements of the stack
        #     result = ''.join(stack[:k])
        #     joltage_counter += int(result)

    print(joltage_counter)


def find_maximum_cell(battery_bank: str) -> tuple[int, int]:
    max = 0
    max_index = 0

    for index, cell in enumerate(battery_bank):
        if int(cell) > max:
            max = int(cell)
            max_index = index

    return max, max_index

if __name__ == "__main__":
    part_2()