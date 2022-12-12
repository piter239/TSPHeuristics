import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

height, width = [int(i) for i in input().split()]

m = [input() for i in range(height)]


# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

def nbr(i, j):
    r = m[i][max(0, j - 1): min(width, j + 2)].count('O')
    if i > 1:
        r += m[i - 1][max(0, j - 1): min(width, j + 2)].count('O')
    if i + 1 < height:
        r += m[i + 1][max(0, j - 1): min(width, j + 2)].count('O')
    if m[i][j] == 'O':
        r -= 1
    return r


for i in range(height):
    for j in range(width):
        print(nbr(i, j), end=' ', file=sys.stderr)
        if m[i][j] == '.' and nbr(i, j) == 3:
            print(end='O')
        elif m[i][j] == 'O' and (2 > nbr(i, j) or nbr(i, j) > 3):
            print(end='.')
        else:
            print(end=m[i][j])
    print(file=sys.stderr, flush=True)
    print()
