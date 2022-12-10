import sys

cycles_of = {
    "addx": 2,
    "noop": 1,
}

capture_cycles = [20, 60, 100, 140, 180, 220]
signal_strengths = []

X = 1
cycle = 0
for line in sys.stdin:
    l = line.rstrip().split()
    instruction = l[0]
    cycle += cycles_of[instruction]
    if cycle >= capture_cycles[0]:
        c = capture_cycles.pop(0)
        print(c, X)
        signal_strengths.append(c * X)
    if instruction == "addx":
        X += int(l[1])
    if len(capture_cycles) == 0:
        break

print(signal_strengths)
print(sum(signal_strengths))
