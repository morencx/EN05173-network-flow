from collections import deque


class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.lista_adjacencia = [[] for i in range(vertices)]

    def adicionar_aresta(self, u, v):
        self.lista_adjacencia[u].append(v)
        self.lista_adjacencia[v].append(u)

    def imprimir_lista_adjacencia(self):
        for i in range(self.vertices):
            print("Vértice", i, end=" -> ")
            for j in self.lista_adjacencia[i]:
                print(j, end=" ")
            print()

    def BFS(self, origem):
        visitados = [False] * self.vertices
        distancia = [-1] * self.vertices
        caminho = [None] * self.vertices
        fila = deque()

        visitados[origem] = True
        distancia[origem] = 0
        fila.append(origem)

        while fila:
            u = fila.popleft()
            for v in self.lista_adjacencia[u]:
                if not visitados[v]:
                    visitados[v] = True
                    distancia[v] = distancia[u] + 1
                    caminho[v] = u
                    fila.append(v)

        return distancia, caminho


# Criando um grafo com 5 vértices
grafo = Grafo(5)

# Adicionando algumas arestas
grafo.adicionar_aresta(0, 1)
grafo.adicionar_aresta(0, 4)
grafo.adicionar_aresta(1, 2)
grafo.adicionar_aresta(1, 3)
grafo.adicionar_aresta(1, 4)
grafo.adicionar_aresta(2, 3)
grafo.adicionar_aresta(3, 4)

# Imprimindo a lista de adjacência
grafo.imprimir_lista_adjacencia()

# Executando BFS a partir do vértice 0
origem = 0
distancia, caminho = grafo.BFS(origem)

print("Distância a partir do vértice", origem)
for i in range(grafo.vertices):
    print("Vértice", i, ":", distancia[i])

print("Caminho a partir do vértice", origem)
for i in range(grafo.vertices):
    print("Vértice", i, ":", caminho[i])
