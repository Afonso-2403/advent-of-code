from pathlib import Path

INPUT_FILE_PATH = f"{Path(__file__).parent}/../input_files/day_2_input.txt"

def part_1():

    def process_report(line):
        splitted_line = [int(number) for number in line.split()]

        if splitted_line != sorted(splitted_line) and splitted_line != sorted(splitted_line, reverse=True):
            return 0
        
        previous_element = splitted_line[0]
        for i in range(1, len(splitted_line)):
            if abs(previous_element - splitted_line[i]) > 3 or abs(previous_element - splitted_line[i]) == 0:
                return 0

            previous_element = splitted_line[i]

        return 1
    
    report_list = []

    with open("day_2_input.txt") as f:
        report_list = f.readlines()

    print(sum(map(process_report, report_list)))
            
    
def part_2():

    def process_report_with_tolerance(line, tolerance=1):
        # print(line, tolerance)
        if type(line) == str:
            splitted_line = [int(number) for number in line.split()]

        else:
            splitted_line = line

        if tolerance and process_report_with_tolerance(splitted_line[1:], 0):
            return 1

        if splitted_line[1] - splitted_line[0] == 0:
            if tolerance == 0:
                return 0
            
            copied_line = splitted_line.copy()
            copied_line.pop(1)
            return process_report_with_tolerance(splitted_line, 0)

        if splitted_line[1] - splitted_line[0] > 0:
            ascending = True
        else:
            ascending = False


        previous_element = splitted_line[0]
        for i in range(1, len(splitted_line)):
            if (
                abs(previous_element - splitted_line[i]) > 3 or abs(previous_element - splitted_line[i]) == 0
                or (ascending and splitted_line[i] - previous_element < 0)
                or (not ascending and splitted_line[i] - previous_element > 0)
            ):
                if tolerance == 0:
                    return 0
                else:
                    if i == len(splitted_line) - 1:
                        return 1
                    
                    copied_line = splitted_line.copy()
                    copied_line.pop(i-1)
                    # print(f"splitted_line: {splitted_line}")
                    # print(f"copied_line: {copied_line}")
                    if process_report_with_tolerance(copied_line, 0):
                        return 1
                    else:
                        splitted_line.pop(i)
                        return process_report_with_tolerance(splitted_line, 0)

            previous_element = splitted_line[i]

        return 1

    report_list = []

    with open(INPUT_FILE_PATH) as f:
        report_list = f.readlines()
    
    print(sum(map(process_report_with_tolerance, report_list)))


if __name__ == "__main__":
    part_2()