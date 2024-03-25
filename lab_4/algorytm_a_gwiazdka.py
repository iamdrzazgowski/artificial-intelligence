import heapq

constant_heuristics = {
    'Opole': 0,
    'Paryż': 400,
    'Wrocław': 80,
    'Częstochowa': 90,
    'Łódź': 200,
    'Poznań': 230,
    'Warszawa': 260,
    'Gdańsk': 500
}

def astar(graph, start, goal, heuristic_func):
    open_list = [(0, start)]
    closed_set = set()
    g_score = {city: float('inf') for city in graph}
    g_score[start] = 0
    came_from = {}

    while open_list:
        current_cost, current_city = heapq.heappop(open_list)

        if current_city == goal:
            path = []
            while current_city in came_from:
                path.insert(0, current_city)
                current_city = came_from[current_city]
            path.insert(0, start)
            return path

        closed_set.add(current_city)

        for neighbor, cost in graph[current_city].items():
            if neighbor in closed_set:
                continue
            tentative_g_score = g_score[current_city] + cost
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current_city
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic_func(neighbor)
                heapq.heappush(open_list, (f_score, neighbor))

    return None

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

start_city = 'Opole'
goal_city = 'Gdańsk'

path = astar(graph_with_weights, start_city, goal_city, lambda city: constant_heuristics[city])
print("Znaleziona ścieżka:", ' -> '.join(path))

