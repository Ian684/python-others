def depth_first_search(graph, start):
    """Return vertices in depth-first discovery order."""
    if start not in graph:
        raise KeyError("start is not a graph vertex")
    visited = set()
    order = []
    def visit(vertex):
        visited.add(vertex)
        order.append(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visit(neighbor)
    visit(start)
    return order
