import heapq
import time
import os
import sys

# ANSI escape codes
CLEAR_SCREEN = "\033[2J\033[H"   # Clear screen and move cursor to top-left
RESET_COLOR  = "\033[0m"
RED_COLOR    = "\033[31m"
GREEN_COLOR  = "\033[32m"
BLUE_COLOR   = "\033[34m"
CYAN_COLOR   = "\033[36m"

directions = {
    'N': (-1, 0),
    'E': (0, 1),
    'S': (1, 0),
    'W': (0, -1),
}

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

def in_bounds(r, c, grid):
    return 0 <= r < len(grid) and 0 <= c < len(grid[0])

def print_grid(grid, dist, current_state, visited_cells):
    """
    Print the grid to the terminal with visited cells marked,
    and the current state highlighted.
    - visited_cells: set of (r,c) that we've popped from the queue already
    - current_state: (r, c, direction)
    """
    os.system('')  # On Windows, this enables ANSI escape codes in some terminals
    r_curr, c_curr, d_curr = current_state
    
    print(CLEAR_SCREEN, end="")   # Clear the terminal
    
    for r in range(len(grid)):
        row_str = []
        for c in range(len(grid[r])):
            ch = grid[r][c]
            if (r, c) == (r_curr, c_curr):
                # Current position
                row_str.append(BLUE_COLOR + '@' + RESET_COLOR)
            elif (r, c) in visited_cells and ch not in ('S','E','#'):
                # Mark visited open cells
                row_str.append(CYAN_COLOR + '.' + RESET_COLOR)
            else:
                row_str.append(ch)
        print("".join(row_str))
    # Optionally show some info
    cost = dist.get((r_curr, c_curr, d_curr), 0)
    print(f"\nCost so far: {cost}  Direction: {d_curr}")
    sys.stdout.flush()

def dijkstra_animated(grid, start, end, delay=0.001):
    """
    An animated Dijkstra that displays the map in the terminal at each step.
    Returns the minimal cost to reach E (in any direction).
    """

    # Priority queue: (cost, r, c, direction)
    pq = []
    heapq.heappush(pq, (0, start[0], start[1], 'E'))  # Start facing East
    
    dist = {(start[0], start[1], 'E'): 0}

    visited_cells = set()  # For animation: cells that have been popped from queue

    while pq:
        cost, r, c, d = heapq.heappop(pq)

        # If this cost is outdated, skip
        if cost > dist.get((r, c, d), float('inf')):
            continue

        # Mark this cell as visited in the animation
        visited_cells.add((r, c))

        # Print the current state of the grid
        print_grid(grid, dist, (r, c, d), visited_cells)
        time.sleep(delay)

        # If we've reached E, stop and return cost
        if (r, c) == end:
            return cost

        # Explore next states:

        # 1) Move forward
        dr, dc = directions[d]
        nr, nc = r + dr, c + dc
        if in_bounds(nr, nc, grid) and grid[nr][nc] != '#':
            new_cost = cost + 1
            if new_cost < dist.get((nr, nc, d), float('inf')):
                dist[(nr, nc, d)] = new_cost
                heapq.heappush(pq, (new_cost, nr, nc, d))
        
        # 2) Turn left
        ld = turn_left(d)
        new_cost = cost + 1000
        if new_cost < dist.get((r, c, ld), float('inf')):
            dist[(r, c, ld)] = new_cost
            heapq.heappush(pq, (new_cost, r, c, ld))

        # 3) Turn right
        rd = turn_right(d)
        new_cost = cost + 1000
        if new_cost < dist.get((r, c, rd), float('inf')):
            dist[(r, c, rd)] = new_cost
            heapq.heappush(pq, (new_cost, r, c, rd))

    return None  # No path found

def main():
    with open('input.txt', 'r') as f:
        grid = [list(line.rstrip('\n')) for line in f]

    start = find_char(grid, 'S')
    end = find_char(grid, 'E')
    if not start or not end:
        print("Invalid maze: missing 'S' or 'E'.")
        return

    # Run the animated Dijkstra
    best_score = dijkstra_animated(grid, start, end, delay=0.05)
    if best_score is None:
        print("No solution found.")
    else:
        print(f"Lowest possible score: {best_score}")

if __name__ == "__main__":
    main()
