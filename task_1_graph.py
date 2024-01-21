import networkx as nx
import matplotlib.pyplot as plt

def create_and_draw_complex_graph():
    G = nx.Graph()
    # Додавання вершин
    nodes = [f"Перехрестя {i}" for i in range(1, 12)]
    G.add_nodes_from(nodes)

    # Додавання ребер з більш складною структурою
    edges = [
        ("Перехрестя 1", "Перехрестя 2"),
        ("Перехрестя 1", "Перехрестя 3"),
        ("Перехрестя 2", "Перехрестя 3"),
        ("Перехрестя 2", "Перехрестя 4"),
        ("Перехрестя 3", "Перехрестя 5"),
        ("Перехрестя 4", "Перехрестя 5"),
        ("Перехрестя 4", "Перехрестя 6"),
        ("Перехрестя 5", "Перехрестя 7"),
        ("Перехрестя 6", "Перехрестя 7"),
        ("Перехрестя 6", "Перехрестя 8"),
        ("Перехрестя 7", "Перехрестя 9"),
        ("Перехрестя 8", "Перехрестя 9"),
        ("Перехрестя 8", "Перехрестя 10"),
        ("Перехрестя 9", "Перехрестя 11"),
        ("Перехрестя 10", "Перехрестя 11")
    ]
    G.add_edges_from(edges)

    # Візуалізація графа
    plt.figure(figsize=(8, 4))
    nx.draw(G, with_labels=True, node_color="skyblue", node_size=2000, edge_color="gray", linewidths=2, font_size=12)
    plt.title("Оновлена Модель Транспортної Мережі Міста з 11 Вершинами")
    plt.show()

    return G

if __name__ == "__main__":
    complex_graph = create_and_draw_complex_graph()
