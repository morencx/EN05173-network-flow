class Grafo:
    def __init__(self, vertices) -> None:
        self.vertices = vertices
        self.list_adj = [[] for i in range(vertices)]

    def add_edge(self, u, v, capacity):
        self.list_adj[u][v] = capacity

    def BFS(self):
        pass
