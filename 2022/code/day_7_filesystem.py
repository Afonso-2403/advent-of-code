INPUT_FILE = "../input_files/day_7_input.txt"

class DirectoryObject():
  def __init__(self, size = 0, parent=None):
    self.size = size
    self.parent = parent


def update_size_directory_and_all_parents(directories_tree, directory, size_to_add):

  while directory != None:
    directories_tree[directory].size += size_to_add
    directory = directories_tree[directory].parent


  # check if in python a copy of the argument is created or if the object is being modified
  # return directories_tree



def exercise_1():
  # check how to type a dictionary
  directories_tree = {}
  current_directory = None
  total_size_small_directories = 0

  count = 0

  with open(INPUT_FILE) as input_file:
    for line in input_file:
      parsed_line = line.rstrip().split()

      if parsed_line[0] == "$":
        if parsed_line[1] == "cd":
          if parsed_line[2] == "..":
            current_directory = directories_tree[current_directory].parent
          else:
            new_directory_key = parsed_line[2] + str(count)
            directories_tree[new_directory_key] = DirectoryObject(size=0)
            directories_tree[new_directory_key].parent = current_directory
            current_directory = new_directory_key
      
      else:
        try:
          file_size = int(parsed_line[0])
        except:
          pass
        else:
          update_size_directory_and_all_parents(directories_tree, current_directory, file_size)


      count += 1

    for directory in directories_tree:
      if directories_tree[directory].size < 100000:
        total_size_small_directories += directories_tree[directory].size
      
    print(total_size_small_directories)

def exercise_2():
  directories_tree = {}
  current_directory = None
  maximum_size = 40000000
  size_directory_to_delete = maximum_size
  total_occupied_size = 0

  count = 0

  with open(INPUT_FILE) as input_file:
    for line in input_file:
      parsed_line = line.rstrip().split()

      if parsed_line[0] == "$":
        if parsed_line[1] == "cd":
          if parsed_line[2] == "..":
            current_directory = directories_tree[current_directory].parent
          else:
            new_directory_key = parsed_line[2] + str(count)
            directories_tree[new_directory_key] = DirectoryObject(size=0)
            directories_tree[new_directory_key].parent = current_directory
            current_directory = new_directory_key
      
      else:
        try:
          file_size = int(parsed_line[0])
        except:
          pass
        else:
          update_size_directory_and_all_parents(directories_tree, current_directory, file_size)


      count += 1

    total_occupied_size = directories_tree["/0"].size

    for directory in directories_tree:
      if total_occupied_size - directories_tree[directory].size <= maximum_size and directories_tree[directory].size < size_directory_to_delete:
        size_directory_to_delete = directories_tree[directory].size

    print(f"total_occupied_size = {total_occupied_size}")
    print(f"Size of directory to delete = {size_directory_to_delete}")


def main():
  # exercise_1()
  exercise_2()

if __name__ == "__main__":
  main()