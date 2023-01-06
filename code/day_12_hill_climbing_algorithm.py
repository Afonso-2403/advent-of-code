INPUT_FILE = "../input_files/day_12_input_example.txt"

class Node():
  def __init__(self, x, y, height, start_node=False, destination_node=False):
    self.x = x
    self.y = y
    self.height = height
    self.explored = False
    self.start_node = start_node
    self.destination_node = destination_node
    self.parent_coordinates = None
    self.distance_to_current_node = 0

    # find out how to make print(Node()) be this
    def __str__(self):
      return f"Position: ({self.x},{self.y}) height = {self.height}"

def bread_first_search(destination_coordinates, terrain_map, number_rows, number_columns):
  coordinates_nodes_to_expand = [destination_coordinates]
  coordinates_expanded_nodes = set()
  while True:
    for current_node_coordinates in coordinates_expanded_nodes:
      if terrain_map[current_node_coordinates[0] * number_columns + current_node_coordinates[1]].start_node == True:
        return current_node_coordinates
      coordinates_nodes_to_expand.append(current_node_coordinates)
    coordinates_expanded_nodes = set()
    
    for node_to_expand_coordinates in coordinates_nodes_to_expand:
      if node_to_expand_coordinates[0] > 0:
        if (
          terrain_map[
            (node_to_expand_coordinates[0] - 1) * number_columns + node_to_expand_coordinates[1]
          ].height >= terrain_map[node_to_expand_coordinates[0] * number_columns + node_to_expand_coordinates[1]].height - 1
        ):
          if terrain_map[(node_to_expand_coordinates[0] - 1) * number_columns + node_to_expand_coordinates[1]].explored == False:
            terrain_map[(node_to_expand_coordinates[0] - 1) * number_columns + node_to_expand_coordinates[1]].explored = True
            terrain_map[(node_to_expand_coordinates[0] - 1) * number_columns + node_to_expand_coordinates[1]].parent_coordinates = node_to_expand_coordinates
            terrain_map[
              (node_to_expand_coordinates[0] - 1) * number_columns + node_to_expand_coordinates[1]
            ].distance_to_current_node = terrain_map[node_to_expand_coordinates[0] * number_columns + node_to_expand_coordinates[1]].distance_to_current_node + 1
            coordinates_expanded_nodes.add(((node_to_expand_coordinates[0] - 1), node_to_expand_coordinates[1]))

          if (
            terrain_map[(node_to_expand_coordinates[0] - 1) * number_columns + node_to_expand_coordinates[1]].explored == True
            and terrain_map[
              node_to_expand_coordinates[0] * number_columns + node_to_expand_coordinates[1]
            ].distance_to_current_node + 1 < terrain_map[(node_to_expand_coordinates[0] - 1) * number_columns + node_to_expand_coordinates[1]].distance_to_current_node
          ):
            terrain_map[(node_to_expand_coordinates[0] - 1) * number_columns + node_to_expand_coordinates[1]].parent_coordinates = node_to_expand_coordinates
            terrain_map[
              (node_to_expand_coordinates[0] - 1) * number_columns + node_to_expand_coordinates[1]
            ].distance_to_current_node = terrain_map[node_to_expand_coordinates[0] * number_columns + node_to_expand_coordinates[1]].distance_to_current_node + 1
            coordinates_expanded_nodes.add(((node_to_expand_coordinates[0] - 1), node_to_expand_coordinates[1]))

      if node_to_expand_coordinates[0] < number_rows - 1:
        if (
          terrain_map[
            (node_to_expand_coordinates[0] + 1) * number_columns + node_to_expand_coordinates[1]
          ].height >= terrain_map[node_to_expand_coordinates[0] * number_columns + node_to_expand_coordinates[1]].height - 1
        ):
          if terrain_map[(node_to_expand_coordinates[0] + 1) * number_columns + node_to_expand_coordinates[1]].explored == False:
            terrain_map[(node_to_expand_coordinates[0] + 1) * number_columns + node_to_expand_coordinates[1]].explored = True
            terrain_map[(node_to_expand_coordinates[0] + 1) * number_columns + node_to_expand_coordinates[1]].parent_coordinates = node_to_expand_coordinates
            terrain_map[
              (node_to_expand_coordinates[0] + 1) * number_columns + node_to_expand_coordinates[1]
            ].distance_to_current_node = terrain_map[node_to_expand_coordinates[0] * number_columns + node_to_expand_coordinates[1]].distance_to_current_node + 1
            coordinates_expanded_nodes.add(((node_to_expand_coordinates[0] + 1), node_to_expand_coordinates[1]))

          if (
            terrain_map[(node_to_expand_coordinates[0] + 1) * number_columns + node_to_expand_coordinates[1]].explored == True
            and terrain_map[
              node_to_expand_coordinates[0] * number_columns + node_to_expand_coordinates[1]
            ].distance_to_current_node + 1 < terrain_map[(node_to_expand_coordinates[0] + 1) * number_columns + node_to_expand_coordinates[1]].distance_to_current_node
          ):
            terrain_map[(node_to_expand_coordinates[0] + 1) * number_columns + node_to_expand_coordinates[1]].parent_coordinates = node_to_expand_coordinates
            terrain_map[
              (node_to_expand_coordinates[0] + 1) * number_columns + node_to_expand_coordinates[1]
            ].distance_to_current_node = terrain_map[node_to_expand_coordinates[0] * number_columns + node_to_expand_coordinates[1]].distance_to_current_node + 1
            coordinates_expanded_nodes.add(((node_to_expand_coordinates[0] + 1), node_to_expand_coordinates[1]))

      if node_to_expand_coordinates[1] > 0:
        if (
          terrain_map[
            node_to_expand_coordinates[0] * number_columns + (node_to_expand_coordinates[1] - 1)
          ].height >= terrain_map[node_to_expand_coordinates[0] * number_columns + node_to_expand_coordinates[1]].height - 1
        ):
          if terrain_map[node_to_expand_coordinates[0] * number_columns + (node_to_expand_coordinates[1] - 1)].explored == False:
            terrain_map[node_to_expand_coordinates[0] * number_columns + (node_to_expand_coordinates[1] - 1)].explored = True
            terrain_map[node_to_expand_coordinates[0] * number_columns + (node_to_expand_coordinates[1] - 1)].parent_coordinates = node_to_expand_coordinates
            terrain_map[
              node_to_expand_coordinates[0] * number_columns + (node_to_expand_coordinates[1] - 1)
            ].distance_to_current_node = terrain_map[node_to_expand_coordinates[0] * number_columns + node_to_expand_coordinates[1]].distance_to_current_node + 1
            coordinates_expanded_nodes.add((node_to_expand_coordinates[0], (node_to_expand_coordinates[1] - 1)))

          if (
            terrain_map[node_to_expand_coordinates[0] * number_columns + (node_to_expand_coordinates[1] - 1)].explored == True
            and terrain_map[
              node_to_expand_coordinates[0] * number_columns + node_to_expand_coordinates[1]
            ].distance_to_current_node + 1 < terrain_map[node_to_expand_coordinates[0] * number_columns + (node_to_expand_coordinates[1] - 1)].distance_to_current_node
          ):
            terrain_map[node_to_expand_coordinates[0] * number_columns + (node_to_expand_coordinates[1] - 1)].parent_coordinates = node_to_expand_coordinates
            terrain_map[
              node_to_expand_coordinates[0] * number_columns + (node_to_expand_coordinates[1] - 1)
            ].distance_to_current_node = terrain_map[node_to_expand_coordinates[0] * number_columns + node_to_expand_coordinates[1]].distance_to_current_node + 1
            coordinates_expanded_nodes.add((node_to_expand_coordinates[0], (node_to_expand_coordinates[1] - 1)))

      if node_to_expand_coordinates[1] > number_columns - 1:
        if (
          terrain_map[
            node_to_expand_coordinates[0] * number_columns + (node_to_expand_coordinates[1] + 1)
          ].height >= terrain_map[node_to_expand_coordinates[0] * number_columns + node_to_expand_coordinates[1]].height - 1
        ):
          if terrain_map[node_to_expand_coordinates[0] * number_columns + (node_to_expand_coordinates[1] + 1)].explored == False:
            terrain_map[node_to_expand_coordinates[0] * number_columns + (node_to_expand_coordinates[1] + 1)].explored = True
            terrain_map[node_to_expand_coordinates[0] * number_columns + (node_to_expand_coordinates[1] + 1)].parent_coordinates = node_to_expand_coordinates
            terrain_map[
              node_to_expand_coordinates[0] * number_columns + (node_to_expand_coordinates[1] + 1)
            ].distance_to_current_node = terrain_map[node_to_expand_coordinates[0] * number_columns + node_to_expand_coordinates[1]].distance_to_current_node + 1
            coordinates_expanded_nodes.add((node_to_expand_coordinates[0], (node_to_expand_coordinates[1] + 1)))

          if (
            terrain_map[node_to_expand_coordinates[0] * number_columns + (node_to_expand_coordinates[1] + 1)].explored == True
            and terrain_map[
              node_to_expand_coordinates[0] * number_columns + node_to_expand_coordinates[1]
            ].distance_to_current_node + 1 < terrain_map[node_to_expand_coordinates[0] * number_columns + (node_to_expand_coordinates[1] + 1)].distance_to_current_node
          ):
            terrain_map[node_to_expand_coordinates[0] * number_columns + (node_to_expand_coordinates[1] + 1)].parent_coordinates = node_to_expand_coordinates
            terrain_map[
              node_to_expand_coordinates[0] * number_columns + (node_to_expand_coordinates[1] + 1)
            ].distance_to_current_node = terrain_map[node_to_expand_coordinates[0] * number_columns + node_to_expand_coordinates[1]].distance_to_current_node + 1
            coordinates_expanded_nodes.add((node_to_expand_coordinates[0], (node_to_expand_coordinates[1] + 1)))
    coordinates_nodes_to_expand = []

def exercise_1():

  terrain_map = {}
  
  current_row = 0
  current_column = 0
  number_columns = 0
  number_rows = 0

  with open(INPUT_FILE) as input_file:
    for line in input_file:
      current_column = 0
      line = line.rstrip()
      for character in line:
        if current_row == 0:
          number_columns = len(line)

        if character == "S":
          terrain_map[current_row * number_columns + current_column] = Node(current_row, current_column, 0, start_node=True)
          starting_coordinates = (current_row, current_column)
        
        elif character == "E":
          terrain_map[current_row * number_columns + current_column] = Node(current_row, current_column, 26, destination_node=True)
          destination_coordinates = (current_row, current_column)

        else:
          terrain_map[current_row * number_columns + current_column] = Node(current_row, current_column, ord(character) - ord('a'))

        current_column += 1

      current_row += 1
  
  number_rows = current_row
  
  print(f"starting_coordinates: {starting_coordinates}")
  print(f"destination_coordinates: {destination_coordinates}")
  print(f"Start node: {terrain_map[starting_coordinates[0] * number_columns + starting_coordinates[1]].height}")
  print(f"Destination node: {terrain_map[destination_coordinates[0] * number_columns + destination_coordinates[1]].height}")
  
  start_node_coordinates = bread_first_search(destination_coordinates, terrain_map, number_rows, number_columns)

  print(f"The number of steps is = {terrain_map[start_node_coordinates[0] * number_columns + start_node_coordinates[1]].distance_to_current_node}")

def main():
  exercise_1()
  # exercise_2()

if __name__ == "__main__":
  main()