import sys

def priority(item):
    p = ord(item) - ord("a") + 1
    if p > 0 and p <= 26:
        return p
    return ord(item) - ord("A") + 27

total = 0
seen = dict()
for j, line in enumerate(sys.stdin):
    if j % 3 == 0:
        for s in seen:
            if seen[s] == 3:
                total += priority(s)
                break
        seen = dict()
    rucksack = line.rstrip()
    
    for item in set(rucksack):
        if not item in seen:
            seen[item] = 0
        seen[item] += 1

print(total)
