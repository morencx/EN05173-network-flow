from collections import defaultdict


class Grafo:
    def __init__(self) -> None:
        self.grafo = defaultdict(dict)

    def add_edge(self, u, v, capacidade):
        self.grafo[u][v] = capacidade

    def BFS(self, origem, destino, pai):
        visitado = [False] * len(self.grafo)
        fila = []
        fila.append(origem)
        visitado[origem] = True

        while fila:
            u = fila.pop(0)
            for v in self.grafo[u]:
                if not visitado[v] and self.grafo[u][v] > 0:
                    fila.append(v)
                    visitado[v] = True
                    pai[v] = u
                    if v == destino:
                        return True
        return False

    def FordFulkerson(self, origem, destino):
        pai = [-1] * len(self.grafo)
        fluxo_maximo = 0

        while self.BFS(origem, destino, pai):
            fluxo_caminho = float("inf")
            v = destino
            while v != origem:
                u = pai[v]
                fluxo_caminho = min(fluxo_caminho, self.grafo[u][v])
                v = pai[v]

            fluxo_maximo += fluxo_caminho

            v = destino
            while v != origem:
                u = pai[v]
                self.grafo[u][v] -= fluxo_caminho
                self.grafo[v][u] += fluxo_caminho
                v = pai[v]

        return fluxo_maximo


g = Grafo()
g.add_edge(0, 1, 16)
g.add_edge(0, 2, 13)
g.add_edge(1, 2, 10)
g.add_edge(1, 3, 12)
g.add_edge(2, 1, 4)
g.add_edge(2, 4, 14)
g.add_edge(3, 2, 9)
g.add_edge(3, 5, 20)
g.add_edge(4, 3, 7)
g.add_edge(4, 5, 4)

origem = 0
destino = 5

fluxo_maximo = g.FordFulkerson(origem, destino)
print("O fluxo máximo possível é:", fluxo_maximo)
