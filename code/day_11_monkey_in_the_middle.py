import types
from queue import Queue

INPUT_FILE = "../input_files/day_11_input.txt"

class Monkey():
  def __init__(self):
    self.queue = Queue()
    self.operand = 0
    self.divisible_by = 0
    self.throw_to_monkey_case_true = 0
    self.throw_to_monkey_case_false = 0
    self.number_inspected_items = 0

    def __str__(self):
      return f"Number of items: {len(self.queue)}, 3 is transformed to: {self.operation(3)}, worry_level = 3 is thrown to: {self.throw_condition(3)}"

def exercise_1():

  list_monkeys = []

  with open(INPUT_FILE) as input_file:
    for line in input_file:
      line = line.replace(',', ' ')
      parsed_line = line.rstrip().split()

      if len(parsed_line) == 0:
        continue

      if parsed_line[0] == "Monkey":
        list_monkeys.append(Monkey())

      if parsed_line[0] == "Starting":
        for item in parsed_line[2:]:
          list_monkeys[-1].queue.put(int(item))
      
      if parsed_line[0] == "Operation:":
        if parsed_line[4] == '*':
          if parsed_line[5] == 'old':
            def operation(self, old):
              return old * old
          else:
            list_monkeys[-1].operand = int(parsed_line[5])
            def operation(self, old):
              return old * self.operand
        else:
            list_monkeys[-1].operand = int(parsed_line[5])
            def operation(self, old):
              return old + self.operand

        list_monkeys[-1].operation = types.MethodType(operation, list_monkeys[-1])


      if parsed_line[0] == "Test:":
        list_monkeys[-1].divisible_by = int(parsed_line[3])
        list_monkeys[-1].throw_to_monkey_case_true = int(next(input_file).rstrip().split()[5])
        list_monkeys[-1].throw_to_monkey_case_false = int(next(input_file).rstrip().split()[5])

        def throw_to_condition(self, worry_level):
          return self.throw_to_monkey_case_true if worry_level % self.divisible_by == 0 else self.throw_to_monkey_case_false

        list_monkeys[-1].throw_to_condition = types.MethodType(throw_to_condition, list_monkeys[-1])

  for round in range(20):
    for monkey in list_monkeys:
      while not monkey.queue.empty():
        item_worry_level = monkey.queue.get()
        monkey.number_inspected_items += 1
        item_worry_level = monkey.operation(item_worry_level)
        item_worry_level = item_worry_level // 3
        monkey_to_throw_to = monkey.throw_to_condition(item_worry_level)
        list_monkeys[monkey_to_throw_to].queue.put(item_worry_level)

  max_2 = [0, 0]
  for monkey in list_monkeys:
    if monkey.number_inspected_items >= max_2[0]:
      max_2[1] = max_2[0]
      max_2[0] = monkey.number_inspected_items

    elif monkey.number_inspected_items >= max_2[1]:
      max_2[1] = monkey.number_inspected_items
    

  print(f"monkey_business = {max_2[0] * max_2[1]}")

def exercise_2():

  list_monkeys = []
  worry_level_reduction_magic_number = 1

  with open(INPUT_FILE) as input_file:
    for line in input_file:
      line = line.replace(',', ' ')
      parsed_line = line.rstrip().split()

      if len(parsed_line) == 0:
        continue

      if parsed_line[0] == "Monkey":
        list_monkeys.append(Monkey())

      if parsed_line[0] == "Starting":
        for item in parsed_line[2:]:
          list_monkeys[-1].queue.put(int(item))
      
      if parsed_line[0] == "Operation:":
        if parsed_line[4] == '*':
          if parsed_line[5] == 'old':
            def operation(self, old):
              return old * old
          else:
            list_monkeys[-1].operand = int(parsed_line[5])
            def operation(self, old):
              return old * self.operand
        else:
            list_monkeys[-1].operand = int(parsed_line[5])
            def operation(self, old):
              return old + self.operand

        list_monkeys[-1].operation = types.MethodType(operation, list_monkeys[-1])


      if parsed_line[0] == "Test:":
        list_monkeys[-1].divisible_by = int(parsed_line[3])
        worry_level_reduction_magic_number *= list_monkeys[-1].divisible_by
        list_monkeys[-1].throw_to_monkey_case_true = int(next(input_file).rstrip().split()[5])
        list_monkeys[-1].throw_to_monkey_case_false = int(next(input_file).rstrip().split()[5])

        def throw_to_condition(self, worry_level):
          return self.throw_to_monkey_case_true if worry_level % self.divisible_by == 0 else self.throw_to_monkey_case_false

        list_monkeys[-1].throw_to_condition = types.MethodType(throw_to_condition, list_monkeys[-1])

  for round in range(10000):
    for monkey in list_monkeys:
      while not monkey.queue.empty():
        item_worry_level = monkey.queue.get()
        item_worry_level %= worry_level_reduction_magic_number
        monkey.number_inspected_items += 1
        item_worry_level = monkey.operation(item_worry_level)
        monkey_to_throw_to = monkey.throw_to_condition(item_worry_level)
        list_monkeys[monkey_to_throw_to].queue.put(item_worry_level)

  max_2 = [0, 0]
  for monkey in list_monkeys:
    if monkey.number_inspected_items >= max_2[0]:
      max_2[1] = max_2[0]
      max_2[0] = monkey.number_inspected_items

    elif monkey.number_inspected_items >= max_2[1]:
      max_2[1] = monkey.number_inspected_items
    

  print(f"monkey_business = {max_2[0] * max_2[1]}")

def main():
  # exercise_1()
  exercise_2()

if __name__ == "__main__":
  main()