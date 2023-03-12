# Definición de la base de conocimiento
base_conocimiento = {
    'síntoma1': ['enfermedad1', 'enfermedad2'],
    'síntoma2': ['enfermedad2', 'enfermedad3'],
    'síntoma3': ['enfermedad1', 'enfermedad3'],
    'síntoma4': ['enfermedad2']
}

# Definición de las reglas
def regla1(síntomas):
    if 'síntoma1' in síntomas and 'síntoma2' in síntomas:
        return 'enfermedad2'
    return None

def regla2(síntomas):
    if 'síntoma1' in síntomas and 'síntoma3' in síntomas:
        return 'enfermedad1'
    return None

def regla3(síntomas):
    if 'síntoma2' in síntomas and 'síntoma4' in síntomas:
        return 'enfermedad2'
    return None

# Definición del sistema experto
def sistema_experto(síntomas):
    enfermedades_posibles = []
    
    # Buscar enfermedades en la base de conocimiento
    for síntoma in síntomas:
        if síntoma in base_conocimiento:
            enfermedades_posibles += base_conocimiento[síntoma]
    
    # Eliminar enfermedades duplicadas
    enfermedades_posibles = list(set(enfermedades_posibles))
    
    # Aplicar las reglas para reducir el número de enfermedades posibles
    enfermedades_reducidas = []
    for regla in [regla1, regla2, regla3]:
        resultado = regla(síntomas)
        if resultado and resultado in enfermedades_posibles:
            enfermedades_reducidas.append(resultado)
    
    # Si solo hay una enfermedad posible, se devuelve esa enfermedad
    if len(enfermedades_reducidas) == 1:
        return enfermedades_reducidas[0]
    
    # Si no, se devuelve una lista con las enfermedades posibles
    return enfermedades_reducidas

# Ejemplo de uso
síntomas = ['síntoma1', 'síntoma2', 'síntoma4']
resultado = sistema_experto(síntomas)
print(resultado) # Salida: 'enfermedad2'

