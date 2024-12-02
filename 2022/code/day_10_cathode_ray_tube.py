INPUT_FILE = "../input_files/day_10_input.txt"

def exercise_1():
  cycle_number = 1
  register_value = 1 
  sum = 0
  threshold = 20

  with open(INPUT_FILE) as input_file:
    for line in input_file:
      current_add = 0

      operation = line.rstrip().split()
      if len(operation) == 1:
        cycle_number += 1
      
      if len(operation) == 2:
        cycle_number += 2
        current_add = int(operation[1])
      
      if cycle_number > threshold:
        sum += threshold * register_value
        threshold += 40
        if threshold > 220:
          break

      register_value += current_add


  print(f"Sum of values in cycles = {sum}")

def exercise_2():
  current_CRT_position = 0
  sprite_position = 1
  drawing = [[]]
  row_number = 0
  number_columns = 40

  with open(INPUT_FILE) as input_file:
    for line in input_file:
      operation = line.rstrip().split()

      if abs(current_CRT_position - sprite_position) <= 1:
        drawing[row_number].append('#')     
      else:
        drawing[row_number].append('.')

      current_CRT_position += 1

      if current_CRT_position == number_columns:
        current_CRT_position = 0
        row_number += 1
        drawing.append([])
      
      if len(operation) == 2:
        if abs(current_CRT_position - sprite_position) <= 1:
          drawing[row_number].append('#')     
        else:
          drawing[row_number].append('.')

        current_CRT_position += 1

        if current_CRT_position == number_columns:
          current_CRT_position = 0
          row_number += 1
          drawing.append([])
          
        sprite_position += int(operation[1])

  for row in drawing:
    for entry in row:
      print(entry, end='')
    print('')

def main():
  # exercise_1()
  exercise_2()

if __name__ == "__main__":
  main()