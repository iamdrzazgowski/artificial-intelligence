def DFS(graph, start, end):
    stack = [(start, 0)]
    visited = set()
    path = {start: None}

    while stack:
        current, cost = stack.pop()
        if current == end:
            return construct_path(path, start, end)
        visited.add(current)
        for neighbor, weight in graph[current].items():
            if neighbor not in visited:
                path[neighbor] = current
                stack.append((neighbor, cost + weight))
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
    'Wrocław': {'Opole': 86, 'Poznań': 178, 'Częstochowa': 176},
    'Częstochowa': {'Opole': 98, 'Wrocław': 176, 'Łódź': 121},
    'Łódź': {'Częstochowa': 121, 'Wrocław': 204, 'Poznań': 212, 'Warszawa': 134, 'Gdańsk': 340},
    'Poznań': {'Wrocław': 178, 'Łódź': 212, 'Warszawa': 310, 'Gdańsk': 296},
    'Warszawa': {'Łódź': 134, 'Poznań': 310, 'Gdańsk': 339, 'Częstochowa': 222},
    'Gdańsk': {'Poznań': 296, 'Warszawa': 339, 'Łódź': 340, 'Paryż': 1700},
    'Paryż': {'Opole': 1405, 'Gdańsk': 1700}
}

start = 'Opole'
end = 'Gdańsk'

path = DFS(graph_with_weights, start, end)
print("Znaleziona ścieżka:", ' -> '.join(path))

