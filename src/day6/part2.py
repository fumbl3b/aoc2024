
def solve():
    with open('input.txt', 'r') as f:
        original_map = [list(line.strip('\n')) for line in f]

    # Find guard start
    guard_start = None
    guard_dir = None
    directions = {
        '^': (-1, 0),
        'v': (1, 0),
        '<': (0, -1),
        '>': (0, 1)
    }

    for i in range(len(original_map)):
        for j in range(len(original_map[0])):
            if original_map[i][j] in directions:
                guard_start = (i, j)
                guard_dir = original_map[i][j]
                break
        if guard_dir is not None:
            break

    def turn_right(d):
        if d == '^': return '>'
        if d == '>': return 'v'
        if d == 'v': return '<'
        if d == '<': return '^'

    def in_bounds(m, x, y):
        return 0 <= x < len(m) and 0 <= y < len(m[0])

    def simulate(m):
        # Locate guard
        gx, gy, gdir = None, None, None
        for x in range(len(m)):
            for y in range(len(m[0])):
                if m[x][y] in directions:
                    gx, gy = x, y
                    gdir = m[x][y]
                    break
            if gdir is not None:
                break

        visited_states = set()
        max_steps = len(m) * len(m[0]) * 4
        steps = 0

        while True:
            steps += 1
            if steps > max_steps:
                # We haven't left the map and haven't found a repeated state in max_steps steps
                # This should theoretically not happen without a loop, but just to be safe:
                return True  # Assume it's a loop to stop infinite runs

            state = (gx, gy, gdir)
            if state in visited_states:
                # Loop detected
                return True
            visited_states.add(state)

            dx, dy = directions[gdir]
            nx, ny = gx + dx, gy + dy

            if not in_bounds(m, nx, ny):
                # Leaves map
                return False

            if m[nx][ny] == '#':
                # Turn right
                gdir = turn_right(gdir)
                m[gx][gy] = gdir
            else:
                # Move forward
                m[gx][gy] = 'X'
                gx, gy = nx, ny
                m[gx][gy] = gdir

    loop_count = 0
    for x in range(len(original_map)):
        for y in range(len(original_map[0])):
            if (x, y) == guard_start:
                continue
            if original_map[x][y] == '.':
                m_copy = [row[:] for row in original_map]
                m_copy[x][y] = '#'
                if simulate(m_copy):
                    loop_count += 1

    print("loop count: ", loop_count)

solve()
