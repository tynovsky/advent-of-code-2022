import sys

contained = 0

for line in sys.stdin:
    a, b = [[int(y) for y in x.split("-")] for x in line.rstrip().split(",")]
    contained += int((a[0] - b[0]) * (a[1] - b[1]) <= 0)
    
print(contained)


