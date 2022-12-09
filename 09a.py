import sys

def main():
    head = (0,0)
    tail = (0,0)

    tail_visited = set()

    for line in sys.stdin:
        direction, count = line.rstrip().split()
        count = int(count)
        print(direction, count)

        for i in range(count):
            head = move_head(head, direction)
            tail = move_tail(tail, head)
            print(i)
            print("head:", head)
            print("tail:", tail)
            tail_visited.add(tail)
            # print(tail_visited)

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
    raise("This can never happen")

def move_tail(orig, head):
    if abs(orig[0] - head[0]) <= 1 and abs(orig[1] - head[1]) <= 1:
        return orig
    if abs(orig[0] - head[0]) == 2:
        if head[0] > orig[0]:
            return (orig[0] + 1, head[1])
        else:
            return (orig[0] - 1, head[1])
    if abs(orig[1] - head[1]) == 2:
        if head[1] > orig[1]:
            return (head[0], orig[1] + 1)
        else:
            return (head[0], orig[1] - 1)
    raise("This can never happen")

if __name__ == "__main__":
    main()
