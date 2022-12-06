import sys

def priority(item):
    p = ord(item) - ord("a") + 1
    if p > 0 and p <= 26:
        return p
    return ord(item) - ord("A") + 27

total = 0
for line in sys.stdin:
    rucksack = line.rstrip()
    compartment_size = len(rucksack)
    seen = set()
    for i, item in enumerate(rucksack):
        if i < compartment_size / 2:
            seen.add(item)
        else:
            if item in seen:
                total += priority(item)
                print(priority(item))
                break

print(total)
