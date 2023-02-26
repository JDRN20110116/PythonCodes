#Esta busqueda en amplitud busca motrar todos los amigos dentro de una red social con relación al grafo principal

from collections import deque

# Definimos el grafo de la red social
graph = {
    'David': ['Juan', 'Monica', 'Ernesto'],
    'Juan': ['David', 'Valeria'],
    'Monica': ['Fernando', 'David', 'Caro'],
    'Ernesto': ['David', 'Valeria'],
    'Valeria': ['Juan', 'Caro'],
    'Fernando': ['Monica'],
    'Caro': ['Valeria', 'Monica']
}

# Definimos la función de búsqueda en amplitud
def bfs(graph, start):
    visited = set()  # Conjunto para guardar los nodos ya visitados
    queue = deque([start])  # Cola para guardar los nodos pendientes de visitar

    while queue:  # Mientras haya nodos pendientes en la cola
        node = queue.popleft()  # Tomamos el primer nodo en la cola
        if node not in visited:
            visited.add(node)
            print(node)  # Mostramos el nodo visitado

            for neighbour in graph[node]:  # Para cada vecino del nodo visitado
                if neighbour not in visited:
                    queue.append(neighbour)  # Añadimos el vecino a la cola

# Ejecutamos la búsqueda desde el nodo 'David'
bfs(graph, 'David')


