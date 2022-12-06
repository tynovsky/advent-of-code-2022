import sys

shape_mapping = dict(
    A = 0, # rock
    B = 1, # paper
    C = 2, # scissors
    X = 0, # rock
    Y = 1, # paper
    Z = 2, # scissors
)

def play(a, b):
    return ((a - b) + 1) % 3

total = 0
for line in sys.stdin:
    (opponent, me) = [shape_mapping[x] for x in line.strip().split()]
    shape_score = me + 1
    result_score = 3 * play(me, opponent)
    score = shape_score + result_score
    total += score

print(total)
