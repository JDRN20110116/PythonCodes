import random

random.seed()

# Definir la lista de trabajadores
trabajadores = [
    {"nombre": "Anna", "Carpinteria": 80, "Plomeria": 85, "Electricista": 90},
    {"nombre": "Miguel", "Carpinteria": 80, "Plomeria": 75, "Electricista": 90},
    {"nombre": "Luis", "Carpinteria": 70, "Plomeria": 95, "Electricista": 65},
    {"nombre": "Cesar", "Carpinteria": 95, "Plomeria": 99, "Electricista": 75},
    {"nombre": "Lucia", "Carpinteria": 85, "Plomeria": 90, "Electricista": 90},
    {"nombre": "Mariana", "Carpinteria": 85, "Plomeria": 70, "Electricista": 95}
]

# Definir la funci�n para calcular la puntuaci�n total de un trabajador
def calcular_puntuacion(trabajador):
    return trabajador["Carpinteria"] + trabajador["Plomeria"] + trabajador["Electricista"]

# Definir la funci�n para calcular el tiempo total de construcci�n
def calcular_tiempo_construccion(asignacion_trabajadores):
    tiempo_total = 10
    for i in range(len(asignacion_trabajadores)):
        habilidad_trabajador = asignacion_trabajadores[i]
        tiempo_total += trabajadores[i][habilidad_trabajador]
    return tiempo_total

# Definir la funci�n para generar una soluci�n vecina
def generar_vecino(asignacion_trabajadores):
    # Copiar la asignaci�n actual de trabajadores
    vecino = asignacion_trabajadores.copy()
    
    # Seleccionar dos trabajos aleatorios para intercambiar
    i = random.randint(0, len(vecino) - 1)
    j = random.randint(0, len(vecino) - 1)
    
    # Intercambiar los trabajos seleccionados
    vecino[i], vecino[j] = vecino[j], vecino[i]
    
    return vecino

# Definir la soluci�n inicial aleatoria
asignacion_trabajadores = ["Carpinteria", "Plomeria", "Electricista"]
random.shuffle(asignacion_trabajadores)

# Calcular el tiempo total de construcci�n para la soluci�n inicial
mejor_tiempo = calcular_tiempo_construccion(asignacion_trabajadores)

# Aplicar el algoritmo Hill Climbing
while True:
    # Generar una soluci�n vecina
    vecino = generar_vecino(asignacion_trabajadores)
    
    # Calcular el tiempo total de construcci�n para la soluci�n vecina
    tiempo_vecino = calcular_tiempo_construccion(vecino)
    
    # Si la soluci�n vecina es mejor que la actual, actualizar la soluci�n actual
    if tiempo_vecino < mejor_tiempo:
        asignacion_trabajadores = vecino
        mejor_tiempo = tiempo_vecino
    # Si la soluci�n vecina no es mejor, salir del bucle
    else:
        break

# Imprimir la soluci�n final
print("Asignacion de trabajos:")
for i in range(len(asignacion_trabajadores)):
   print(f"{trabajadores[i]['nombre']}: {asignacion_trabajadores[i]}")
print(f"Tiempo en horas total de construccion: {mejor_tiempo}")
