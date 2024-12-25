grid = []

with open('./src/day17/input.txt', 'r') as f:
    grid = [[int(n) for n in list(line.strip())] for line in f.readlines()]


def neighbors(x: int, y: int): 
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
            yield nx, ny

def bfs(sx, sy):
    '''
    Finds all trails from starting point sx, sy
    '''
    from collections import deque
    visited = set()
    visited.add((sx, sy))
    queue = deque([(sx, sy)])
    count_9 = 0
    alt = 0

    while queue:
        x, y = queue.popleft()

        if grid[x][y] == 9:
            count_9 += 1
            alt = 0
        
        for nx, ny in neighbors(x, y):
            if grid[nx][ny] == alt + 1 and (nx,ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny))
                alt += 1
    return count_9