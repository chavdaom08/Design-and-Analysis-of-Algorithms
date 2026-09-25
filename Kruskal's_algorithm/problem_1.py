class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])  
        return self.parent[i]

    def union(self, u, v):
        root_u, root_v = self.find(u), self.find(v)
        if root_u != root_v:
            self.parent[root_u] = root_v
            return True
        return False


def kruskal(num_nodes, edges):
    # Sort edges by weight: (weight, u, v)
    edges.sort()
    uf = UnionFind(num_nodes)
    mst = []
    total_weight = 0

    for weight, u, v in edges:
        if uf.union(u, v):
            mst.append((u, v, weight))
            total_weight += weight

    return mst, total_weight


#  Example Usage 
edges = [
    (1, 0, 1),
    (3, 0, 2),
    (3, 1, 2),
    (6, 1, 3),
    (4, 2, 3),
    (2, 2, 4),
    (5, 3, 4),
]

num_nodes = 5
mst, weight = kruskal(num_nodes, edges)

print("Edges in Minimum Spanning Tree:", mst)
print("Total MST Weight:", weight)