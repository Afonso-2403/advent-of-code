INPUT_FILE = "../input_files/day_8_input.txt"

def exercise_1():
  count = 0
  number_columns = 0
  grid = {}
  visible_trees = 0

  row_max = 0
  column_max = []
  current_row = 0
  current_column = 0

  with open(INPUT_FILE) as input_file:
    for line in input_file:    
      row_max = 0
      current_column = 0

      for tree_string in line.rstrip():
        tree_height = int(tree_string)
        position_in_grid = count

        grid[position_in_grid] = [tree_height, False, False, False, False]
        if tree_height > row_max or current_column == 0:
          row_max = tree_height
          grid[position_in_grid][1] = True

        if current_row == 0:
          column_max.append(tree_height)
          number_columns += 1
          grid[position_in_grid][2] = True

        elif tree_height > column_max[current_column]:
          column_max[current_column] = tree_height
          grid[position_in_grid][2] = True

        current_column += 1
        count += 1       

      current_row += 1

  number_rows = int(len(grid.keys()) / number_columns)
  row_max = 0
  column_max = [0] * number_columns
  current_row = number_rows - 1
  current_column = number_columns - 1

  for position_in_grid in sorted(grid.keys(), reverse=True):
    tree_height = grid[position_in_grid][0]

    if tree_height > row_max or current_column == number_columns - 1:
        row_max = tree_height
        grid[position_in_grid][3] = True

    if tree_height > column_max[current_column] or current_row == number_rows - 1:
      column_max[current_column] = tree_height
      grid[position_in_grid][4] = True

    if (number_columns - current_column) == number_columns:
      current_column = number_columns - 1
      current_row -= 1
      row_max = 0

    else:
      current_column -= 1

  for position_in_grid in grid:
    if True in grid[position_in_grid][1:]:
      visible_trees += 1

  print(f"Visible trees = {visible_trees}")

def exercise_2():
  count = 0
  number_columns = 0
  number_rows = 0
  grid = {}

  current_row = 0
  current_column = 0

  with open(INPUT_FILE) as input_file:
    for line in input_file:    
      current_column = 0

      for tree_string in line.rstrip():
        tree_height = int(tree_string)
        position_in_grid = count
        grid[position_in_grid] = [tree_height, 0, 0, 0, 0]

        if current_column != 0 and current_row != 0:
          for lookup_index in range(position_in_grid - 1, current_row * number_columns - 1, -1):
            
            grid[position_in_grid][1] += 1 
            if tree_height <= grid[lookup_index][0]:
              break

          for lookup_index in range(position_in_grid - number_columns, current_column - number_columns, -number_columns):
            grid[position_in_grid][2] += 1 
            if tree_height <= grid[lookup_index][0]:
              break

        current_column += 1
        count += 1       

      number_columns = current_column
      current_row += 1

    number_rows = current_row

  for current_row in range(number_rows - 2, 0, -1):
    for current_column in range(number_columns - 2, 0, -1):
      position_in_grid = current_row * number_columns + current_column
      tree_height = grid[position_in_grid][0]

      for lookup_index in range(position_in_grid + 1, current_row * number_columns + number_columns + 1):
        grid[position_in_grid][3] += 1 
        if tree_height <= grid[lookup_index][0]:
          break

      for lookup_index in range(position_in_grid + number_columns, number_rows * number_columns, number_columns):
        grid[position_in_grid][4] += 1 
        if tree_height <= grid[lookup_index][0]:
          break

  highest_scenic_score = 0
  for position_in_grid in grid:
    scenic_score = grid[position_in_grid][1] * grid[position_in_grid][2] * grid[position_in_grid][3] * grid[position_in_grid][4]
    if scenic_score > highest_scenic_score:
      highest_scenic_score = scenic_score

  print(f"Highest Scenic Score = {highest_scenic_score}")



def main():
  # exercise_1()
  exercise_2()

if __name__ == "__main__":
  main()