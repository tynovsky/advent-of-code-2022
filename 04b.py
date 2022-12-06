import sys

overlapped = 0

for line in sys.stdin:
    a, b = [[int(y) for y in x.split("-")] for x in line.rstrip().split(",")]
    overlapped += int(
            (a[1] >= b[0] >= a[0]) or 
            (a[0] <= b[1] <= a[1]) or
            (b[1] >= a[0] >= b[0]) or 
            (b[0] <= a[1] <= b[1]))
    
print(overlapped)


