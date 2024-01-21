import networkx as nx
from task_1_graph import create_and_draw_complex_graph

def dfs(graph, start):
    visited, stack = set(), [start]
    path = []

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            path.append(vertex)
            stack.extend(set(graph[vertex]) - visited)
    
    return path

def bfs(graph, start):
    visited, queue = set(), [start]
    path = []

    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            path.append(vertex)
            queue.extend(set(graph[vertex]) - visited)
    
    return path

if __name__ == "__main__":
    G = create_and_draw_complex_graph()

    dfs_path = dfs(G, "Перехрестя 1")
    bfs_path = bfs(G, "Перехрестя 1")

    print("DFS Path:", dfs_path)
    print("BFS Path:", bfs_path)
