def read_grid(filename):
    with open(filename, 'r') as file:
        grid = [list(line.strip()) for line in file if line.strip()]
    return grid

def is_x_mas(grid, x, y):
    rows = len(grid)
    cols = len(grid[0])

    # Ensure positions are within bounds
    if x - 1 < 0 or x + 1 >= rows or y - 1 < 0 or y + 1 >= cols:
        return False

    center = grid[x][y]
    if center != 'A':
        return False

    # Positions around the center
    positions = {
        'upper_left': (x - 1, y - 1),
        'upper_right': (x - 1, y + 1),
        'lower_left': (x + 1, y - 1),
        'lower_right': (x + 1, y + 1)
    }

    # Letters at the positions
    letters = {
        pos: grid[i][j]
        for pos, (i, j) in positions.items()
    }

    # Possible MAS combinations (forwards and backwards)
    mas = ['MAS', 'SAM']

    # Check both diagonals
    diagonal1 = letters['upper_left'] + center + letters['lower_right']
    diagonal2 = letters['upper_right'] + center + letters['lower_left']

    # Check if diagonals form MAS or SAM
    valid_diagonal1 = diagonal1 in mas
    valid_diagonal2 = diagonal2 in mas

    # An X-MAS is valid if both diagonals form MAS or SAM
    return valid_diagonal1 and valid_diagonal2

def count_x_mas(grid):
    count = 0
    rows = len(grid)
    cols = len(grid[0])

    for x in range(rows):
        for y in range(cols):
            if is_x_mas(grid, x, y):
                count += 1
    return count

if __name__ == "__main__":
    grid = read_grid('./input.txt')
    total_count = count_x_mas(grid)
    print(f'Total occurrences of X-MAS: {total_count}')