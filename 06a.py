import sys

for line in sys.stdin:
    buffer = [None] * 4
    for i, c in enumerate(line):
        buffer[i % len(buffer)] = c
        # print(buffer)
        if len(set(buffer)) == len(buffer) and None not in buffer:
            print(i+1)
            break

