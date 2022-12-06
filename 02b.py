import sys

shape_mapping = dict(
    A = 0, # rock
    B = 1, # paper
    C = 2, # scissors
)

result_mapping = dict(
    X = 0, # loss
    Y = 1, # draw
    Z = 2, # win
)

def play(a, b):
    return (a - b + 1) % 3

def pick_shape(opponent, result):
    return (opponent + result - 1) % 3
    
total = 0
for line in sys.stdin:
    l = line.strip().split()
    opponent = shape_mapping[l[0]]
    result = result_mapping[l[1]]
    me = pick_shape(opponent, result)
    shape_score = me + 1
    result_score = 3 * result
    score = shape_score + result_score
    total += score

print(total)
