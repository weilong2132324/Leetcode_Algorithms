def bellman_ford(edges, source):
    """
    Bellman-Ford Algorithm
    Finds shortest paths from source to all vertices.
    Handles negative weight edges and detects negative cycles.

    Args:
        graph: list of edges as (u, v, weight)
        source: starting vertex

    Returns:
        dist: dict of shortest distances from source
        predecessor: dict to reconstruct paths
        or None if a negative cycle is detected
    """
    vertices = set()
    
    for u, v, weight in edges:
        vertices.add(u)
        vertices.add(v)

    distances = {node:float('inf') for node in vertices}
    distances[source] = 0

    number_of_edges = len(vertices) - 1

    for _ in range(number_of_edges-1):
        for u, v, weight in edges:
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight

    for u, v, weight in edges:
        if distances[u] != float('inf') and distances[u] + weight < distances[v]:
            return None, None
    
    return distances

def reconstruct_path(predecessor, source, target):
    path = []
    current = target
    while current is not None:
        path.append(current)
        current = predecessor[current]
    path.reverse()
    if path[0] == source:
        return path
    return []  # No path found


# Example usage
if __name__ == "__main__":
    edges = [
        ('A', 'B', 4),
        ('A', 'C', 2),
        ('B', 'C', -1),
        ('B', 'D', 2),
        ('C', 'D', 3),
        ('D', 'E', 1),
    ]

    distances, predecessor = bellman_ford(edges, 'A')

    if distances:
        print("Shortest distances from A:")
        for node, d in sorted(distances.items()):
            print(f"  {node}: {d}")

        print("\nShortest path from A to E:", reconstruct_path(predecessor, 'A', 'E'))
