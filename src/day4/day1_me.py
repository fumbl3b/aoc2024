with open('./input.txt', 'r') as file:
    matrix = [list(row.strip()) for row in file]

directions = [
    (-1,  1), # NW
    ( 0,  1), # N
    ( 1,  1), # NE
    ( 1,  0), # E
    ( 1, -1), # SE
    ( 0, -1), # S
    (-1, -1), # SW
    (-1,  0)  # W
]

word = ['X', 'M', 'A', 'S']

def search_from(x, y, dx, dy):
    for i in range(len(word)):
        nx = x + i * dx
        ny = y + i * dy

        if nx < 0 or ny < 0 or nx >= len(matrix) or ny >= len(matrix[0]):
            return 0
        
        if matrix[nx][ny] != word[i]:
            return 0
    return 1  

xmases = 0

for x in range(len(matrix)):
    for y in range(len(matrix[0])):
        for dx, dy in directions:
            if matrix[x][y] == word[0]:
                xmases += search_from(x, y, dx, dy)

print(xmases)