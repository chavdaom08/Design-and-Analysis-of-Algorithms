class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])  # Path compression
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j
            return True
        return False

def kruskal(num_vertices, edges):
    # Sort edges by weight: (weight, u, v)
    edges.sort()
    ds = DisjointSet(num_vertices)
    mst = []
    total_weight = 0

    for weight, u, v in edges:
        # If u and v are not in the same component, include the edge
        if ds.union(u, v):
            mst.append((u, v, weight))
            total_weight += weight

    return mst, total_weight