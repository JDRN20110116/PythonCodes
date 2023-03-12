# Definici�n de la base de conocimiento
base_conocimiento = {
    's�ntoma1': ['enfermedad1', 'enfermedad2'],
    's�ntoma2': ['enfermedad2', 'enfermedad3'],
    's�ntoma3': ['enfermedad1', 'enfermedad3'],
    's�ntoma4': ['enfermedad2']
}

# Definici�n de las reglas
def regla1(s�ntomas):
    if 's�ntoma1' in s�ntomas and 's�ntoma2' in s�ntomas:
        return 'enfermedad2'
    return None

def regla2(s�ntomas):
    if 's�ntoma1' in s�ntomas and 's�ntoma3' in s�ntomas:
        return 'enfermedad1'
    return None

def regla3(s�ntomas):
    if 's�ntoma2' in s�ntomas and 's�ntoma4' in s�ntomas:
        return 'enfermedad2'
    return None

# Definici�n del sistema experto
def sistema_experto(s�ntomas):
    enfermedades_posibles = []
    
    # Buscar enfermedades en la base de conocimiento
    for s�ntoma in s�ntomas:
        if s�ntoma in base_conocimiento:
            enfermedades_posibles += base_conocimiento[s�ntoma]
    
    # Eliminar enfermedades duplicadas
    enfermedades_posibles = list(set(enfermedades_posibles))
    
    # Aplicar las reglas para reducir el n�mero de enfermedades posibles
    enfermedades_reducidas = []
    for regla in [regla1, regla2, regla3]:
        resultado = regla(s�ntomas)
        if resultado and resultado in enfermedades_posibles:
            enfermedades_reducidas.append(resultado)
    
    # Si solo hay una enfermedad posible, se devuelve esa enfermedad
    if len(enfermedades_reducidas) == 1:
        return enfermedades_reducidas[0]
    
    # Si no, se devuelve una lista con las enfermedades posibles
    return enfermedades_reducidas

# Ejemplo de uso
s�ntomas = ['s�ntoma1', 's�ntoma2', 's�ntoma4']
resultado = sistema_experto(s�ntomas)
print(resultado) # Salida: 'enfermedad2'

