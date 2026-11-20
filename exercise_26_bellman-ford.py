def bellman_ford(graph, start):
    """Return shortest distances, or raise ValueError for negative cycles."""
    vertices = set(graph)
    for edges in graph.values():
        for destination, _ in edges:
            vertices.add(destination)
    if start not in vertices:
        raise KeyError("start is not a graph vertex")
    distances = {vertex: float('inf') for vertex in vertices}
    distances[start] = 0
    for _ in range(len(vertices) - 1):
        changed = False
        for source in graph:
            for destination, weight in graph[source]:
                candidate = distances[source] + weight
                if candidate < distances[destination]:
                    distances[destination] = candidate
                    changed = True
        if not changed:
            break
    for source in graph:
        for destination, weight in graph[source]:
            if distances[source] + weight < distances[destination]:
                raise ValueError("graph contains a negative cycle")
    return distances
