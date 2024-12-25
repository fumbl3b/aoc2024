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
    # sort the connections of a and add them to list neighbors
    neighbors = sorted(graph[a])
    # iterate through all connections
    for i in range(len(neighbors)):
        connection = neighbors[i]

def find_cliques_of_size_k_or_more(graph, k=3):
    """
    Returns all cliques of size >= k (not necessarily maximal) in 'graph'.
    graph is a dict: node -> set_of_neighbors
    """
    all_cliques = []

    def backtrack(potential_clique, candidates):
        # potential_clique: the current set of nodes forming a clique so far
        # candidates: nodes that can still be added if they are connected to everything in potential_clique

        if len(potential_clique) >= k:
            # We can record it now. 
            # (If you only want *maximal* cliques, you'd keep exploring or do a different check.)
            all_cliques.append(potential_clique.copy())

        # Explore each candidate one by one
        while candidates:
            node = candidates.pop()
            # Intersect neighbors with 'candidates' to keep only those that are connected to 'node'
            new_candidates = candidates.intersection(graph[node])
            # Only add 'node' if it is connected to *all* in potential_clique
            # (If we arrived here, we already ensured 'node' is connected to the existing clique.)
            new_potential_clique = potential_clique | {node}
            backtrack(new_potential_clique, new_candidates)

    # Start with each node as a seed
    nodes = list(graph.keys())
    for i, start_node in enumerate(nodes):
        # For the first node, your candidate set is the neighbors of 'start_node' 
        # (since only they could join a clique with 'start_node')
        backtrack({start_node}, set(graph[start_node]))

    return all_cliques


# print('the largest clique is: ', find_cliques_of_size_k_or_more(graph).sort())
sorted_list = sorted(find_cliques_of_size_k_or_more(graph), key=len, reverse=True)
biggest = sorted(list(sorted_list[0]))
print(','.join(biggest))
