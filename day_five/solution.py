cargo = []
input_lines = []
cargo_retained = []


def move_stacks_retain_order(stack_origin, stack_destination, number):
    # Pop number from stack_origin
    stacks = []
    for _ in range(0, number):
        stacks.append(cargo_retained[stack_origin].pop())

    stacks.reverse()
    cargo_retained[stack_destination] += stacks


def move_stack_number(stack_origin, stack_destination, number):
    # Pop number from stack_origin
    stacks = []
    for _ in range(0, number):
        stacks.append(cargo[stack_origin].pop())

    cargo[stack_destination] += stacks


def do_instruction(instruction):
    stack_origin_idx = instruction[1] - 1
    stack_dest_idx = instruction[2] - 1
    move_stack_number(stack_origin_idx, stack_dest_idx, instruction[0])
    move_stacks_retain_order(stack_origin_idx, stack_dest_idx, instruction[0])


def parse_line_into_stacks(line):
    stack_no = 0
    for i in range(1, len(line), 4):
        stack = line[i]
        if stack != " ":
            cargo[stack_no] = [stack] + cargo[stack_no]
        stack_no += 1


def parse_instruction(line):
    import re

    instr = re.findall("[0-9]+", line)
    return [int(i) for i in instr]


def print_stacks(stacks):
    for s in stacks:
        print(s)


with open("input.dat") as fp:
    input_lines = fp.readlines()

cargo = [[]] * len(input_lines[0])
print(f"Initialized stack with size {len(cargo)}")


done_parsing_stacks = False
for i, line in enumerate(input_lines):
    if not done_parsing_stacks:
        parse_line_into_stacks(line.replace("\n", ""))

    # Seperated line between cargo and
    if not line or len(line) == 1:
        done_parsing_stacks = True
        continue

    if done_parsing_stacks:
        if not cargo_retained:
            import copy

            cargo_retained = copy.deepcopy(cargo)
        instruction = parse_instruction(line)
        do_instruction(instruction)

print_stacks(cargo[:9])
print_stacks(cargo_retained[:9])
