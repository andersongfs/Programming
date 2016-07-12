parent = dict()
rank = dict()

def make_set(vertice):
    parent[vertice] = vertice
    rank[vertice] = 0

def find(vertice):
    if parent[vertice] != vertice:
        parent[vertice] = find(parent[vertice])
    return parent[vertice]

def union(vertice1, vertice2):
    root1 = find(vertice1)
    root2 = find(vertice2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]: rank[root2] += 1

def kruskal(graph):
    for vertice in graph['vertices']:
        make_set(vertice)
    k_sum = 0
    minimum_spanning_tree = set()
    edges = list(graph['edges'])
    edges.sort()
    for edge in edges:
        weight, vertice1, vertice2 = edge
        if find(vertice1) != find(vertice2):
            union(vertice1, vertice2)
            #minimum_spanning_tree.add(edge)
            k_sum += edge[0]
    #return minimum_spanning_tree
    return k_sum


graph = {'vertices': [], 'edges': set([])}
# graph = {
#         'vertices': ['0', '1', '2', '3', '4', '5', '6'],
#         'edges': set([
#             (7, '0', '1' ),
#             (5, '0', '3' ),
#             (8, '1', '2' ),
#             (9, '1', '3' ),
#             (7, '1', '4' ),
#             (5, '2', '4' ),
#             (15, '3', '4' ),
#             (6, '3', '5' ),
#             (8, '4', '5' ),
#             (9, '4', '6' ),
#             (11, '5', '6' )
#             ])
#         }
m,n = map(int, raw_input().split())
while(n != 0 or m != 0):
    total_sum = 0
    min_sum = 0
    for i in range(m):
        graph['vertices'].append(str(i))
    for i in range(n):
        x, y, metros = map(int, raw_input().split())
        total_sum += metros
        graph['edges'].add((metros, str(x), str(y)))
    k_graph = kruskal(graph)
#    for i in k_graph:
#       min_sum += i[0]
    print total_sum - k_graph
    m,n = map(int, raw_input().split())


