file = open('./input.txt', 'r')

directions = {
    (-1,  1), # NW
    ( 0,  1), # N
    ( 1,  1), # NE
    ( 1,  0), # E
    ( 1, -1), # SE
    ( 0, -1), # S
    (-1, -1), # SW
    (-1,  0)  # W
}

# backtracking i think

# set up matrix

matrix = []
word = ['X', 'M', 'A', 'S']

for row in file:
    matrix.append(list(row.strip()))

def backtrack(x, y, i):
    if x < 0 or y < 0 or x >= len(matrix) or y >= len(matrix[0]):
        return 0
    if matrix[x][y] != word[i]:
        return 0
    if i == len(word) - 1:
        return 1

    found = 0
    for d in directions:
        dx = x + d[0]
        dy = y + d[1]
        found += backtrack(dx, dy, i + 1)
    return found
        

xmases = 0

for x, row in enumerate(matrix):
    for y, c in enumerate(row):
        if c == word[0]:
            xmases += backtrack(x,y,0)

# print(matrix)
print(xmases)
