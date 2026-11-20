import heapq

def prim(graph, start=None):
    """Return the minimum spanning tree for a weighted undirected graph."""
    if not graph:
        return []
    if start is None:
        start = next(iter(graph))
    if start not in graph:
        raise KeyError("start is not a graph vertex")
    visited = {start}
    queue = [(weight, start, neighbor) for neighbor, weight in graph[start]]
    heapq.heapify(queue)
    edges = []
    while queue:
        weight, left, right = heapq.heappop(queue)
        if right in visited:
            continue
        visited.add(right)
        edges.append((weight, left, right))
        for neighbor, neighbor_weight in graph[right]:
            if neighbor not in visited:
                heapq.heappush(queue, (neighbor_weight, right, neighbor))
    return edges
