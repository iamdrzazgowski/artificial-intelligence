from collections import deque

def BFS(graph, start, end):
    queue = deque()
    queue.append((start, 0))
    visited = set()
    visited.add(start)
    path = {start: None}

    while queue:
        current, cost = queue.popleft()
        if current == end:
            return construct_path(path, start, end)
        for neighbor, weight in graph[current].items():
            if neighbor not in visited:
                visited.add(neighbor)
                path[neighbor] = current
                queue.append((neighbor, cost + weight))
    return None

def construct_path(path, start, end):
    result = []
    current = end
    while current is not None:
        result.append(current)
        current = path[current]
    return result[::-1]

graph_with_weights = {
    'Opole': {'Paryż': 1405, 'Wrocław': 86, 'Częstochowa': 98},
    'Paryż': {'Opole': 1405, 'Gdańsk': 1700},
    'Wrocław': {'Opole': 86, 'Częstochowa': 176, 'Łódź': 204, 'Poznań': 178},
    'Częstochowa': {'Opole': 98, 'Łódź': 121, 'Warszawa': 222, 'Wrocław': 176},
    'Łódź': {'Wrocław': 204, 'Częstochowa': 121, 'Poznań': 212, 'Warszawa': 134, 'Gdańsk': 340},
    'Poznań': {'Wrocław': 178, 'Łódź': 212, 'Gdańsk': 296, 'Warszawa': 310},
    'Warszawa': {'Częstochowa': 222, 'Łódź': 134, 'Poznań': 310, 'Gdańsk': 339},
    'Gdańsk': {'Poznań': 296, 'Łódź': 340, 'Warszawa': 339}
}

start = 'Opole'
end = 'Gdańsk'
path = BFS(graph_with_weights, start, end)
print("Znaleziona ścieżka:", ' -> '.join(path))
