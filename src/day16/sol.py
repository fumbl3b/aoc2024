directions = { 
    'N':(-1,0),
    'S':(1,0),
    'E':(0,1),
    'W':(0,-1)
}

def turn_left(direction):
    if direction == 'N':
        return 'W'
    elif direction == 'W':
        return 'S'
    elif direction == 'S':
        return 'E'
    elif direction == 'E':
        return 'N'

def explore_maze(map, pos, direction, memo=None, score=0):
    if memo == None:
        memo = set()
    if len(memo) > 0 and score >= min(memo):
        return memo
    row, col = pos
    current_tile = map[row][col]
    if current_tile == 'E':
        memo.add(score)
        return memo

    n_row, n_col = directions.get(direction)
    next_tile = row + n_row, col + n_col
    
    tile = map[next_tile[0]][next_tile[1]]

    if tile == 'E' or tile == '.':
        score += 1
        return explore_maze(map, next_tile, direction, memo, score)
    elif tile == '#':
        score += 1000
        direction = turn_left(direction)
        return explore_maze(map, pos, direction, memo, score)
    else:
        return memo

def find_char(char, map):
    for r in range(len(map)):
        for c in range(len(map[r])):
            if map[r][c] == char:
                return r, c
    return None

def main():
    map = []
    with open('input.txt', 'r') as f:
        map = [list(row.strip()) for row in f.readlines()]
    
    solutions = set()
    start = find_char('S', map)
    end = find_char('E', map)

    print('start: ', start)
    print('end: ', end)

    solutions = explore_maze(map, start, 'N')

    print(min(solutions))

    
if __name__ == "__main__":
    main()
