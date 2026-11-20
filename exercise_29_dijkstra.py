import heapq

def dijkstra(graph, start):
    """Return shortest distances from start in a non-negative weighted graph."""
    if start not in graph:
        raise KeyError("start is not a graph vertex")
    distances = {start: 0}
    queue = [(0, start)]
    while queue:
        distance, vertex = heapq.heappop(queue)
        if distance != distances.get(vertex):
            continue
        for neighbor, weight in graph[vertex]:
            if weight < 0:
                raise ValueError("Dijkstra requires non-negative weights")
            candidate = distance + weight
            if candidate < distances.get(neighbor, float('inf')):
                distances[neighbor] = candidate
                heapq.heappush(queue, (candidate, neighbor))
    return distances
