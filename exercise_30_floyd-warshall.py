def floyd_warshall(graph):
    """Return all-pairs shortest distances for a weighted directed graph."""
    vertices = list(graph)
    distances = {source: {destination: float('inf') for destination in vertices} for source in vertices}
    for source in vertices:
        distances[source][source] = 0
        for neighbor, weight in graph[source]:
            distances[source][neighbor] = min(distances[source][neighbor], weight)
    for intermediate in vertices:
        for source in vertices:
            for destination in vertices:
                candidate = distances[source][intermediate] + distances[intermediate][destination]
                if candidate < distances[source][destination]:
                    distances[source][destination] = candidate
    return distances
