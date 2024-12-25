input_data = []

with open('input.txt', 'r') as f:
    for line in [l.strip() for l in f.readlines()]:
        line = line.split('-')
        a, b = line[0], line[1]
        input_data.append((a,b))


graph = {}

for connection in input_data:
    if connection[0] not in graph:
        graph[connection[0]] = set()
    if connection[1] not in graph:
        graph[connection[1]] = set()
    graph[connection[0]].add(connection[1])
    graph[connection[1]].add(connection[0])
options = [node for node in graph if node[0] == 't']

triangles = set()

for a in graph:
    # For each distinct pair (b, c) among neighbors of a
    neighbors = sorted(graph[a])
    for i in range(len(neighbors)):
        b = neighbors[i]
        for j in range(i+1, len(neighbors)):
            c = neighbors[j]
            # Check if there's also an edge b--c
            if c in graph[b]:
                # We found a triangle a--b--c
                tri = tuple(sorted([a, b, c]))
                triangles.add(tri)

# Now `triangles` is a set of all unique 3-node triangles.
# If you only want the ones that contain at least one node
# starting with 't', then filter further:
triangles_with_t = [
    tri for tri in triangles
    if any(node.startswith('t') for node in tri)
]

print(len(triangles_with_t))
