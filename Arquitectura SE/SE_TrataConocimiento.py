# Definir una lista de síntomas
sintomas = ['fiebre', 'tos', 'dolor de garganta', 'dolor de cabeza']

# Definir una lista de reglas
reglas = [
    {'enfermedad': 'gripe', 'sintomas': ['fiebre', 'tos', 'dolor de cabeza']},
    {'enfermedad': 'resfriado', 'sintomas': ['fiebre', 'tos', 'dolor de garganta']},
    {'enfermedad': 'amigdalitis', 'sintomas': ['fiebre', 'dolor de garganta']}
]

# Pedir al usuario que informe sus síntomas
print("Por favor, indique sus síntomas (separe cada síntoma con una coma):")
sintomas_usuario = input().split(',')

# Buscar la enfermedad que coincide con los síntomas informados
enfermedades_posibles = []
for regla in reglas:
    if all(sintoma in sintomas_usuario for sintoma in regla['sintomas']):
        enfermedades_posibles.append(regla['enfermedad'])

# Mostrar el resultado al usuario
if len(enfermedades_posibles) == 0:
    print("Lo siento, no puedo determinar su enfermedad con los síntomas informados.")
elif len(enfermedades_posibles) == 1:
    print("Creo que tiene", enfermedades_posibles[0])
else:
    print("Creo que tiene una de estas enfermedades:", ', '.join(enfermedades_posibles))

