import sys
import re

p_crate = re.compile("(?:\[.\]|   )(?: |$)")
p_label = re.compile("^\[(.)\] ?$")

state = []
for line in sys.stdin:
    line = line.rstrip()
    if line == "":
        break
    for i, crate in enumerate(re.findall(p_crate, line)):
        if len(state) == i:
            state.append([])
        m = p_label.match(crate)
        if m:
            state[i].insert(0, m.group(1))

for line in sys.stdin:
    count, src, dst = [int(x) for x in re.findall(r"[0-9]+", line.rstrip())]
    src -= 1
    dst -= 1
    for i in range(count):
        state[dst].append(state[src].pop())

for s in state:
    print(s[-1], end="")
print()
