class Instruction():
    def __init__(self, instruction_string: str):
        res = [int(i) for i in instruction_string.split() if i.isdigit()]
        self.move_count = int(res[0])
        self.stack_from = int(res[1])
        self.stack_to = int(res[2])

    def __repr__(self):
        return f"Move={self.move_count} from={self.stack_from} to={self.stack_to}"


def get_crate_state_from_file(filename: str):
    result = {}

    with open(filename) as f:
        stacks = construct_empty_stacks(9)

        for line in f.readlines():
            if not line.startswith(" 1"):
                result = populate_stacks(stacks, line)
            else:
                break

    return result


def populate_stacks(stacks: dict, line: str):
    column = 1
    count = 0

    for char in line:
        if char != " " and char != "[" and char != "]" and char != "\n":
            stacks[column].append(char)
        count += 1
        if count == 4:
            column += 1
            count = 0
    return stacks


def construct_empty_stacks(no_of_stacks: int) -> dict:
    result_dict = {}

    for i in range(1, no_of_stacks + 1):
        result_dict[i] = []

    return result_dict


def reverse_stacks(stacks: dict) -> dict:

    for value in stacks:
        stacks[value] = stacks[value][::-1]

    return stacks


def get_instructions_from_file(filename: str):
    result = []

    with open(filename) as f:
        for line in f.readlines():
            if line.startswith("move"):
                result.append(Instruction(line))

    return result


def move_crates(instruction: Instruction, stacks: dict):
    items = pop_from_stack(instruction, stacks)
    add_to_stack(instruction.stack_to, stacks, items)

    return stacks


def pop_from_stack(instruction: Instruction, stacks: dict) -> list:
    popped_items = []

    for i in range(0, instruction.move_count):
        popped_items.append(stacks[instruction.stack_from].pop())
    return popped_items[::-1]


def add_to_stack(stack_to: int, stacks: dict, items: list):

    for i in items:
        stacks[stack_to].append(i)




if __name__ == "__main__":

    initial_crates = get_crate_state_from_file("input.txt")
    initial_crates = reverse_stacks(initial_crates)

    instructions = get_instructions_from_file("input.txt")


    for instruction in instructions:
        move_crates(instruction, initial_crates)

    result_str = ""

    for value in initial_crates:
        result_str += initial_crates[value].pop()


    print(f"The crates on top are in this {result_str} configuration.")






