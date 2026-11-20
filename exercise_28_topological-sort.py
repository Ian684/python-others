from collections import deque

def topological_sort(graph):
    """Return a topological ordering, or raise ValueError for a cycle."""
    indegree = {vertex: 0 for vertex in graph}
    for neighbors in graph.values():
        for neighbor in neighbors:
            indegree.setdefault(neighbor, 0)
    for neighbors in graph.values():
        for neighbor in neighbors:
            indegree[neighbor] += 1
    queue = deque(vertex for vertex, degree in indegree.items() if degree == 0)
    order = []
    while queue:
        vertex = queue.popleft()
        order.append(vertex)
        for neighbor in graph.get(vertex, ()):
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    if len(order) != len(indegree):
        raise ValueError("graph contains a cycle")
    return order
