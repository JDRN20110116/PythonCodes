#Aqui se mostraran las tareas a realizar para una cena y las tareas que dependen de ellas mismas.

# Definimos el árbol de tareas como un diccionario de listas de adyacencia
tasks = {
    'Hacer cena especial': ['Comprar ingredientes', 'Preparar comida', 'Decorar mesa'],
    'Comprar ingredientes': ['Hacer lista de compras'],
    'Preparar comida': ['Cocinar plato principal', 'Hacer postre', 'Hacer ensalada', 'Limpiar la cocina'],
    'Cocinar plato principal': ['Picar vegetales', 'Cocinar carne'],
    'Hacer postre': ['Hornear pastel', 'Hacer crema batida'],
    'Decorar mesa': ['Poner platos', 'Poner cubiertos', 'Poner manteles'],
    'Poner platos': [],
    'Poner cubiertos': [],
    'Poner manteles': [],
    'Hacer lista de compras': [],
    'Picar vegetales': [],
    'Cocinar carne': [],
    'Hornear pastel': [],
    'Hacer crema batida': [],
    'Hacer ensalada': [],
    'Limpiar la cocina': []
}

# Definimos la función dfs para recorrer el árbol de tareas en profundidad
def dfs(tasks, node, visited):
    if node not in visited:
        visited.add(node)
        print(f"Completando tarea: {node}")  # Mostramos la tarea completada
        for task in tasks[node]:
            dfs(tasks, task, visited)

# Ejecutamos la búsqueda en profundidad desde la tarea principal
dfs(tasks, 'Hacer cena especial', set())

