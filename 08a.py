import sys

def printgrid(grid):
    for row in grid:
        for e in row:
            print(e, end="")
        print()

trees = []
for line in sys.stdin:
    trees.append(list(map(int, line.rstrip())))

printgrid(trees)
size = len(trees)

lmax = [ [0] * size for _ in range(size)]
tmax = [ [0] * size for _ in range(size)]
rmax = [ [0] * size for _ in range(size)]
bmax = [ [0] * size for _ in range(size)]

for i in range(size):
    for j in range(size):
        k = size - i - 1
        l = size - j - 1

        lmax[i][j] = -1 if j == 0 else max(lmax[i][j-1], trees[i][j-1])
        tmax[i][j] = -1 if i == 0 else max(tmax[i-1][j], trees[i-1][j])
        rmax[k][l] = -1 if l == size-1 else max(rmax[k][l+1], trees[k][l+1])
        bmax[k][l] = -1 if k == size-1 else max(bmax[k+1][l], trees[k+1][l])

printgrid(lmax)
printgrid(tmax)
printgrid(rmax)
printgrid(bmax)

visible = 0
for i in range(size):
    for j in range(size):
        if trees[i][j] > lmax[i][j]:
            visible += 1
            continue
        if trees[i][j] > tmax[i][j]:
            visible += 1
            continue
        if trees[i][j] > rmax[i][j]:
            visible += 1
            continue
        if trees[i][j] > bmax[i][j]:
            visible += 1
            continue

print(visible)
