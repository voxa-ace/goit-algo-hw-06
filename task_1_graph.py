import networkx as nx
import matplotlib.pyplot as plt

def create_and_draw_complex_graph():
    G = nx.Graph()

    # Adding vertexes
    nodes = [f"Перехрестя {i}" for i in range(1, 12)]
    G.add_nodes_from(nodes)

    # Adding edges with defects
    weighted_edges = [
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
    ]
    G.add_weighted_edges_from(weighted_edges)

    # Graph visualization
    plt.figure(figsize=(8, 4))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color="skyblue", node_size=2000, edge_color="gray", linewidths=2, font_size=12)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title("Оновлена Модель Транспортної Мережі Міста з 11 Вершинами і Вагами Ребер")
    plt.show()

    return G

def analyze_graph(G):
    num_nodes = G.number_of_nodes()
    num_edges = G.number_of_edges()
    degrees = G.degree()
    average_degree = sum(dict(degrees).values()) / num_nodes

    # Information output
    print(f"Кількість вершин у графі: {num_nodes}")
    print(f"Кількість ребер у графі: {num_edges}")
    print(f"Середній ступінь вершин у графі: {average_degree:.2f}")
    print("Ступені кожної вершини:")
    for node, degree in degrees:
        print(f" - {node} має ступінь {degree}")

# Creating and visualizing a graph
complex_graph = create_and_draw_complex_graph()

# Analysis of the main characteristics of the graph
analyze_graph(complex_graph)
