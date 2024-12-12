map_grid = []

with open('input.txt', 'r') as f:
    map_grid = [list(line.strip('\n')) for line in f]

directions_list = ['^', 'v', '<', '>']
obstacle = '#'

# dx, dy for each direction symbol: note that we must be consistent with the orientation
directions = {
    '^': (-1, 0),  # up means decreasing x-index
    'v': (1, 0),   # down means increasing x-index
    '<': (0, -1),  # left means decreasing y-index
    '>': (0, 1)    # right means increasing y-index
}

def find_guard(m):
    for x in range(len(m)):
        for y in range(len(m[0])):
            if m[x][y] in directions_list:
                return (x, y)
    return None

def is_in_map(m, x, y):
    return 0 <= x < len(m) and 0 <= y < len(m[0])

def turn_90(direction):
    if direction == '^':
        return '>'
    if direction == '>':
        return 'v'
    if direction == 'v':
        return '<'
    if direction == '<':
        return '^'

guard = find_guard(map_grid)

while True:
    facing = map_grid[guard[0]][guard[1]]
    dx, dy = directions[facing]
    nx, ny = guard[0] + dx, guard[1] + dy

    # Check if moving forward would go out of map
    if not is_in_map(map_grid, nx, ny):
        # The guard will leave the map, so mark current position as visited and stop
        map_grid[guard[0]][guard[1]] = 'X'
        break

    # If inside map, check if next position is obstacle
    if map_grid[nx][ny] == obstacle:
        # Turn right in place
        new_dir = turn_90(facing)
        map_grid[guard[0]][guard[1]] = new_dir
    else:
        # Move forward
        # Mark the current cell as visited
        map_grid[guard[0]][guard[1]] = 'X'
        # Move guard
        guard = (nx, ny)
        # Place the guard facing symbol in the new position
        map_grid[guard[0]][guard[1]] = facing

# Count distinct positions visited (marked as 'X')
visited_count = sum(row.count('X') for row in map_grid)
print(visited_count)
