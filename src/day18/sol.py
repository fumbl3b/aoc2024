from collections import deque

# Read and parse input from 'input.txt'
with open('input.txt', 'r') as f:
    orig_input_points = [[int(x) for x in line.strip().split(',')] for line in f]

# Limit to the first 1024 lines initially
input_points = orig_input_points[:1024]

def generate_grid(points, size):
    grid = [['.' for _ in range(size)] for _ in range(size)]
    for x, y in points:
        grid[x][y] = '#'
    return grid

grid_size = 71
grid = generate_grid(input_points, grid_size)

# Directions for movement: E, N, W, S
directions = [(1,0), (0,1), (-1,0), (0,-1)]

def in_map(x, y, size):
    return 0 <= x < size and 0 <= y < size

def is_passable(grid, x, y):
    return in_map(x, y, len(grid)) and grid[x][y] != '#'

def bfs(grid, start, goal):
    # BFS setup
    queue = deque([start])
    visited = set([start])
    parent = {start: None}  # to reconstruct path
    size = len(grid)

    while queue:
        x, y = queue.popleft()
        
        # Goal check
        if (x, y) == goal:
            # Reconstruct path
            path = []
            curr = (x, y)
            while curr is not None:
                path.append(curr)
                curr = parent[curr]
            path.reverse()
            return path
        
        # Explore neighbors
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_passable(grid, nx, ny) and (nx, ny) not in visited:
                visited.add((nx, ny))
                parent[(nx, ny)] = (x, y)
                queue.append((nx, ny))
    
    # No path found
    return None

start = (0,0)
goal = (70,70)
shortest_route = bfs(grid, start, goal)
length_of_shortest_route = 0

if shortest_route is None:
    print("No path found from (0,0) to (70,70).")
else:
    # Create a copy of the grid (not strictly necessary, but clearer)
    solved_grid = [row[:] for row in grid]

    # Mark the path on the solved grid and count length
    for (px, py) in shortest_route:
        length_of_shortest_route += 1
        solved_grid[px][py] = '@'  # We'll print this in red

    # Print the solved map in red for the path
    for row in solved_grid:
        for cell in row:
            if cell == '@':
                print("\033[91m@\033[0m", end="")  # Red '@'
            else:
                print(cell, end="")
        print()  # Newline after each row

    print("length: ", length_of_shortest_route)

# Now, find the first point that breaks the map
curr_points = input_points[:]
for pair in orig_input_points[1024:]:
    curr_points.append(pair)
    new_grid = generate_grid(curr_points, grid_size)
    if bfs(new_grid, start, goal) is None:
        # This point breaks the map
        print('last point that caused break:', pair)
        break
