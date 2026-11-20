class _DisjointSet:
    def __init__(self, vertices):
        self.parent = {vertex: vertex for vertex in vertices}
    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]
    def union(self, left, right):
        left_root, right_root = self.find(left), self.find(right)
        if left_root == right_root:
            return False
        self.parent[right_root] = left_root
        return True

def kruskal(vertices, edges):
    """Return minimum-spanning-tree edges sorted by Kruskal's algorithm."""
    sets = _DisjointSet(vertices)
    minimum = []
    for weight, left, right in sorted(edges, key=lambda edge: edge[0]):
        if sets.union(left, right):
            minimum.append((weight, left, right))
    return minimum
