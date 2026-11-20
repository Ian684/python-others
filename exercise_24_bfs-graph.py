from collections import deque

def breadth_first_search(graph, start):
    """Return vertices in breadth-first discovery order."""
    if start not in graph:
        raise KeyError("start is not a graph vertex")
    visited = {start}
    order = []
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        order.append(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order
