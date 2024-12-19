import heapq

# Direction vectors: row, col offsets
directions = {
    'N': (-1, 0),
    'E': (0, 1),
    'S': (1, 0),
    'W': (0, -1)
}

# Helper to turn left or right
def turn_left(d):
    return {'N': 'W', 'W': 'S', 'S': 'E', 'E': 'N'}[d]

def turn_right(d):
    return {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}[d]

def find_char(grid, char):
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == char:
                return (r, c)
    return None

def dijkstra_min_score(grid, start, end):
    """
    grid: 2D list of characters ('.', '#', 'S', 'E', etc.)
    start: (row, col) of 'S'
    end: (row, col) of 'E'
    Return the minimal score from S to E, starting facing East.
    """
    rows, cols = len(grid), len(grid[0])
    
    # (cost, row, col, direction)
    # Start facing East with cost = 0
    start_state = (0, start[0], start[1], 'E')
    
    # Min-heap for Dijkstra
    pq = []
    heapq.heappush(pq, start_state)
    
    # dist[(r, c, d)] = minimal cost to reach (r,c) facing d
    dist = {}
    dist[(start[0], start[1], 'E')] = 0

    while pq:
        cost, r, c, d = heapq.heappop(pq)

        # If we reach 'E', return cost immediately
        if (r, c) == end:
            return cost
        
        # If this cost is worse than our best known, skip
        if cost > dist.get((r, c, d), float('inf')):
            continue
        
        # -- 1) Try moving forward --
        dr, dc = directions[d]
        nr, nc = r + dr, c + dc
        if grid[nr][nc] != '#':  # If not a wall, we can move forward
            new_cost = cost + 1
            if new_cost < dist.get((nr, nc, d), float('inf')):
                dist[(nr, nc, d)] = new_cost
                heapq.heappush(pq, (new_cost, nr, nc, d))
        
        # -- 2) Turn left in place --
        ld = turn_left(d)
        new_cost = cost + 1000
        if new_cost < dist.get((r, c, ld), float('inf')):
            dist[(r, c, ld)] = new_cost
            heapq.heappush(pq, (new_cost, r, c, ld))
        
        # -- 3) Turn right in place --
        rd = turn_right(d)
        new_cost = cost + 1000
        if new_cost < dist.get((r, c, rd), float('inf')):
            dist[(r, c, rd)] = new_cost
            heapq.heappush(pq, (new_cost, r, c, rd))
    
    # If we exhaust all states without finding 'E'
    return None  # or float('inf') to signify no path found

def main():
    with open('input.txt', 'r') as f:
        grid = [list(line.rstrip('\n')) for line in f]
    
    start = find_char(grid, 'S')
    end = find_char(grid, 'E')

    if not start or not end:
        print("Invalid maze: Missing S or E.")
        return
    
    best_score = dijkstra_min_score(grid, start, end)
    if best_score is None:
        print("No solution found.")
    else:
        print("Lowest possible score:", best_score)

if __name__ == "__main__":
    main()
