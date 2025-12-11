from pathlib import Path

INPUT_FILE_PATH = f"{Path(__file__).parent}/../input_files/day_07_input.txt"

def part_1():
    num_beam_splits = 0

    with open(INPUT_FILE_PATH) as f:
        start_line = f.readline().strip()
        start_col = start_line.find('S')
        beam_col_set = {start_col}

        for line in f:
            line = line.rstrip()            
            new_set = set()
            for beam_col in beam_col_set:
                if line[beam_col] == '^':
                    num_beam_splits += 1
                    if beam_col > 0:
                        new_set.add(beam_col - 1)
                    if beam_col < len(line) - 1:
                        new_set.add(beam_col + 1)
                else:
                    new_set.add(beam_col)
            
            beam_col_set = new_set
    
    print(num_beam_splits)
            
def part_2():

    with open(INPUT_FILE_PATH) as f:
        start_line = f.readline().strip()
        start_col = start_line.find('S')
        beam_col_dict = {start_col: 1}

        for line in f:
            line = line.rstrip()
            
            new_dict = dict()
            for beam_col, number_of_rays in beam_col_dict.items():
                if line[beam_col] == '^':
                    if beam_col > 0:
                        new_dict[beam_col - 1] = new_dict.get(beam_col - 1, 0) + number_of_rays
                    if beam_col < len(line) - 1:
                        new_dict[beam_col + 1] = new_dict.get(beam_col + 1, 0) + number_of_rays
                else:
                    new_dict[beam_col] = new_dict.get(beam_col, 0) + number_of_rays
            
            beam_col_dict = new_dict
        
    num_timelines = 0
    for _, number_of_rays in beam_col_dict.items():
        num_timelines += number_of_rays

    print(num_timelines)        

if __name__ == "__main__":
    part_2()