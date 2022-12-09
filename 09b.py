import sys

def main():
    head = (0,0)
    tails = [(0,0)] * 9

    tail_visited = set()

    for line in sys.stdin:
        direction, count = line.rstrip().split()
        count = int(count)
        print(direction, count)

        for i in range(count):
            head = move_head(head, direction)
            prev = head
            for j, tail in enumerate(tails):
                tails[j] = move_tail(tail, prev)
                prev = tails[j]
                print(i, j, "head:", head)
                print(tails)
            tail_visited.add(tails[8])

    print(len(tail_visited))

def move_head(orig, direction):
    if direction == 'U':
        return (orig[0], orig[1]-1)
    if direction == 'D':
        return (orig[0], orig[1]+1)
    if direction == 'L':
        return (orig[0]-1, orig[1])
    if direction == 'R':
        return (orig[0]+1, orig[1])
    raise("This can never happen", orig, direction)

def move_tail(orig, head):
    if abs(orig[0] - head[0]) <= 1 and abs(orig[1] - head[1]) <= 1:
        return orig

    (x, y) = head

    if abs(orig[0] - head[0]) == 2:
        if head[0] > orig[0]:
            x = orig[0] + 1
        else:
            x = orig[0] - 1
            
    if abs(orig[1] - head[1]) == 2:
        if head[1] > orig[1]:
            y = orig[1] + 1
        else:
            y = orig[1] - 1
    return (x, y)
    #raise(Exception("This can never happen", orig, head))

if __name__ == "__main__":
    main()
