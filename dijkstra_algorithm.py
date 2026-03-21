import heapq

def dijkstra(graph, start):
    """
    Dijkstra's shortest path algorithm.

    Args:
        graph: dict of {node: [(neighbor, weight), ...]}
        start: starting node

    Returns:
        distances: dict of {node: shortest distance from start}
        predecessors: dict of {node: previous node on shortest path}
    """
    distances = {node:float('inf') for node in graph}
    distances[start] = 0
    heap = [(0, start)]

    while heap:
        distance, curr_node = heapq.heappop(heap)

        if distance > distances[curr_node]:
            continue

        for neighbor, weight in graph[curr_node]:
            new_weight = weight + distance

            if new_weight < distances[neighbor]:
                distances[neighbor] = new_weight
                heapq.heappush(heap, (new_weight, neighbor))

    return distances

def reconstruct_path(predecessors, start, end):
    """Reconstruct the shortest path from start to end."""
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = predecessors[current]
    path.reverse()
    return path if path[0] == start else []


# --- Example Usage ---
if __name__ == "__main__":
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('C', 2), ('D', 6)],
        'C': [('D', 3)],
        'D': []
    }

    start_node = 'A'
    distances, predecessors = dijkstra(graph, start_node)

    print(f"Shortest distances from '{start_node}':")
    for node, dist in distances.items():
        print(f"  {node}: {dist}")

    print(f"\nShortest path from 'A' to 'D':")
    path = reconstruct_path(predecessors, 'A', 'D')
    print(f"  {' -> '.join(path)}")
