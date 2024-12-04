# file = open('./input.txt', 'r')

def read_grid(filename):
    with open(filename, 'r') as file:
        grid = [list(line.strip()) for line in file if line.strip()]
    return grid

def find_word(grid, word):
    count = 0
    rows = len(grid)
    cols = len(grid[0])
    word_len = len(word)

    # Directions: (dx, dy)
    directions = [
        (0, 1),   # Right
        (1, 0),   # Down
        (0, -1),  # Left
        (-1, 0),  # Up
        (1, 1),   # Down-Right
        (-1, -1), # Up-Left
        (1, -1),  # Down-Left
        (-1, 1),  # Up-Right
    ]

    for x in range(rows):
        for y in range(cols):
            for dx, dy in directions:
                nx, ny = x, y
                matched = True
                for k in range(word_len):
                    if 0 <= nx < rows and 0 <= ny < cols:
                        if grid[nx][ny] != word[k]:
                            matched = False
                            break
                        nx += dx
                        ny += dy
                    else:
                        matched = False
                        break
                if matched:
                    count += 1
    return count

if __name__ == "__main__":
    grid = read_grid('./input.txt')
    word = 'XMAS'
    total_count = find_word(grid, word)
    print(f'Total occurrences of {word}: {total_count}')