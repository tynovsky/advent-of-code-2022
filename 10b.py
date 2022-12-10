import sys

instruction = None

X = 1
for i in range(240):
    if i % 40 == 0:
        print()

    if instruction is None:
        instruction = sys.stdin.readline().rstrip().split()
        instruction_time = 1

    if abs(i%40 - X) <= 1:
        print("#", end="")
    else:
        print(".", end="")

    if instruction[0] == "noop":
        instruction = None
        continue

    if instruction[0] == "addx":
        if instruction_time == 1:
            instruction_time += 1
            continue
        X += int(instruction[1])
        instruction = None
