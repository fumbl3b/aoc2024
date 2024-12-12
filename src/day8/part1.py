from itertools import combinations

data = []

with open('input.txt', 'r') as f:
    for line in f.readlines():
        data.append([char for char in line.strip()])

# print(data)

# find each node type
nodes = dict()
for x in range(len(data)):
    for y in range(len(data[0])):
        char = data[x][y]
        if char != '.':
            if char not in nodes:
                nodes[char] = set()
                nodes[char].add((x,y))
            else:
                nodes[char].add((x,y))

# find each pair
pairs = []
for ant in nodes:
    combos = combinations(nodes[ant], 2)
    for combo in combos:
        pairs.append(combo)

def check_in_range(x,y):
    if x < 0 or x >= len(data[0]):
        return False
    if y < 0 or y >= len(data):
        return False
    return True

antinodes = set()

for pair in pairs:
    a, b = pair[0], pair[1]
    ax, ay = a
    bx, by = b
    dx, dy = (ax - bx, ay - by)
    ant_a = (ax + dx, ay + dy)
    ant_b = (bx - dx, by - dy)
    if check_in_range(ant_a[0], ant_a[1]):
        antinodes.add(ant_a)
    if check_in_range(ant_b[0], ant_b[1]):
        antinodes.add(ant_b)

# plot antinodes from pair
print(antinodes)
print(len(antinodes))
# count unique antinodes
# print(antinodes.count())
