INPUT_FILE = "day_6_input.txt"

def exercise_1():
  last_four = []
  count = 0
  with open(INPUT_FILE) as input_file:
    while 1:
      character = input_file.read(1)
      if not character:
        break

      if len(last_four) < 4:
        last_four.append(character)
      else:
        last_four[count % 4] = character
        if len(set(last_four)) == 4:
          count += 1
          break
      count += 1

  print(count)

def exercise_2():
  last_fourteen = []
  count = 0
  with open(INPUT_FILE) as input_file:
    while 1:
      character = input_file.read(1)
      if not character:
        break

      if len(last_fourteen) < 14:
        last_fourteen.append(character)
      else:
        last_fourteen[count % 14] = character
        if len(set(last_fourteen)) == 14:
          count += 1
          break
      count += 1

  print(count)


def main():
  # exercise_1()
  exercise_2()

if __name__ == "__main__":
  main()