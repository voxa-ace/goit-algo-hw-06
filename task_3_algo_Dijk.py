import networkx as nx
import heapq
import matplotlib.pyplot as plt

def create_graph_with_weights():
    G = nx.Graph()
    G.add_weighted_edges_from([
        ("Перехрестя 1", "Перехрестя 2", 2),
        ("Перехрестя 1", "Перехрестя 3", 4),
        ("Перехрестя 2", "Перехрестя 3", 3),
        ("Перехрестя 2", "Перехрестя 4", 5),
        ("Перехрестя 3", "Перехрестя 5", 2),
        ("Перехрестя 4", "Перехрестя 5", 1),
        ("Перехрестя 4", "Перехрестя 6", 3),
        ("Перехрестя 5", "Перехрестя 7", 4),
        ("Перехрестя 6", "Перехрестя 7", 2),
        ("Перехрестя 6", "Перехрестя 8", 5),
        ("Перехрестя 7", "Перехрестя 9", 1),
        ("Перехрестя 8", "Перехрестя 9", 3),
        ("Перехрестя 8", "Перехрестя 10", 2),
        ("Перехрестя 9", "Перехрестя 11", 5),
        ("Перехрестя 10", "Перехрестя 11", 4)
    ])
    return G

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    paths = {vertex: [start] if vertex == start else [] for vertex in graph}

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight['weight']

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                paths[neighbor] = paths[current_vertex] + [neighbor]
                heapq.heappush(priority_queue, (distance, neighbor))

    return paths

def draw_graph(G):
    plt.figure(figsize=(8, 4))
    nx.draw(G, with_labels=True, node_color="skyblue", node_size=2000, edge_color="gray", linewidths=2, font_size=12)
    plt.title("Оновлена Модель Транспортної Мережі Міста з 11 Вершинами")
    plt.show()

def print_paths(all_paths):
    for start_node, paths in all_paths.items():
        print(f"\nНайкоротші шляхи з {start_node}:")
        for end_node, path in paths.items():
            path_str = " -> ".join(path)
            print(f"До {end_node}: {path_str}")

if __name__ == "__main__":
    G = create_graph_with_weights()
    draw_graph(G)

    all_paths = {node: dijkstra(G, node) for node in G.nodes}
    print_paths(all_paths)
