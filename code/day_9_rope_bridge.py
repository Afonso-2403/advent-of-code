INPUT_FILE = "../input_files/day_9_input.txt"

def move_head(head_x, head_y, head_move_direction):
  if head_move_direction == "L":
    head_x -= 1

  if head_move_direction == "R":
    head_x += 1

  if head_move_direction == "U":
    head_y += 1

  if head_move_direction == "D":
    head_y -= 1

  return (head_x, head_y)

def move_knot(previous_knot_x, previous_knot_y, knot_x, knot_y):
  if knot_x - previous_knot_x == 2:
    knot_x -= 1
    if abs(previous_knot_y - knot_y) == 1:
      knot_y = previous_knot_y
    else:
      if previous_knot_y - knot_y == 2:
        knot_y += 1

      if knot_y - previous_knot_y == 2:
        knot_y -= 1

  if previous_knot_x - knot_x == 2:
    knot_x += 1
    if abs(previous_knot_y - knot_y) == 1:
      knot_y = previous_knot_y
    else:
      if previous_knot_y - knot_y == 2:
        knot_y += 1

      if knot_y - previous_knot_y == 2:
        knot_y -= 1

  if previous_knot_y - knot_y == 2:
    knot_y += 1
    knot_x = previous_knot_x

  if knot_y - previous_knot_y == 2:
    knot_y -= 1
    knot_x = previous_knot_x    

  return (knot_x, knot_y)

def exercise_1():
  head_x = 0
  head_y = 0

  tail_x = head_x
  tail_y = head_y

  tail_positions = set()
  tail_positions.add((tail_x, tail_y))

  with open(INPUT_FILE) as input_file:
    for line in input_file:  
      [head_move_direction, number_of_moves] = line.rstrip().split()
      for i in range(int(number_of_moves)):
        (head_x, head_y) = move_head(head_x, head_y, head_move_direction)
        (tail_x, tail_y) = move_knot(head_x, head_y, tail_x, tail_y)
        tail_positions.add((tail_x, tail_y))

  print(f"Number of positions tail visited = {len(tail_positions)}")

def exercise_2():
  head_x = 0
  head_y = 0

  knots = [(head_x, head_y)] * 9

  tail_positions = set()
  tail_positions.add(knots[8])

  with open(INPUT_FILE) as input_file:
    for line in input_file:  
      [head_move_direction, number_of_moves] = line.rstrip().split()
      for i in range(int(number_of_moves)):
        (head_x, head_y) = move_head(head_x, head_y, head_move_direction)
        reference_x = head_x
        reference_y = head_y

        for knot_index, (knot_x, knot_y) in enumerate(knots):
          if knot_index == 8:
            previous_head_position = knots[knot_index]

          knots[knot_index] = move_knot(reference_x, reference_y, knot_x, knot_y)
          reference_x = knots[knot_index][0]
          reference_y = knots[knot_index][1]

        tail_positions.add(knots[8])

  print(f"Number of positions tail visited = {len(tail_positions)}")


def main():
  # exercise_1()
  exercise_2()

if __name__ == "__main__":
  main()