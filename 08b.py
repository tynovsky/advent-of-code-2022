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

best_score = 0
for i in range(size):
    for j in range(size):
        cansee_down = 0
        for k in range(i+1, size):
            cansee_down += 1
            if trees[i][j] <= trees[k][j]:
                break

        cansee_up = 0
        for k in range(i-1, -1, -1):
            cansee_up += 1
            if trees[i][j] <= trees[k][j]:
                break

        cansee_right = 0
        for k in range(j+1, size):
            cansee_right += 1
            if trees[i][j] <= trees[i][k]:
                break

        cansee_left = 0
        for k in range(j-1, -1, -1):
            cansee_left += 1
            if trees[i][j] <= trees[i][k]:
                break

        score = cansee_left * cansee_right * cansee_up * cansee_down
        print(score, i, j, ":", cansee_left, cansee_up, cansee_right, cansee_down)
        best_score = max(best_score, score)


print(best_score)
