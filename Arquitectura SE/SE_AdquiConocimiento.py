# Definición de la base de conocimiento inicial
base_conocimiento = {
    "mamíferos": {
        "hábitat": "terrestre",
        "características": ["pelo", "mamíferos"]
    },
    "aves": {
        "hábitat": "aéreo",
        "características": ["plumas", "ovíparos"]
    },
    "peces": {
        "hábitat": "acuático",
        "características": ["escamas", "ovíparos"]
    }
}

# Función para agregar conocimiento a la base de conocimiento
def agregar_conocimiento():
    tipo_animal = input("Ingrese el tipo de animal que desea agregar: ")
    hábitat = input("Ingrese el hábitat del animal: ")
    características = input("Ingrese las características del animal separadas por comas: ").split(",")
    base_conocimiento[tipo_animal] = {"hábitat": hábitat, "características": características}
    print("Se ha agregado el conocimiento de", tipo_animal, "a la base de conocimiento.")

# Función para consultar la base de conocimiento
def consultar_base_conocimiento():
    tipo_animal = input("Ingrese el tipo de animal que desea consultar: ")
    if tipo_animal in base_conocimiento:
        print("El hábitat del", tipo_animal, "es", base_conocimiento[tipo_animal]["hábitat"])
        print("Las características del", tipo_animal, "son:", ", ".join(base_conocimiento[tipo_animal]["características"]))
    else:
        print("Lo siento, el tipo de animal", tipo_animal, "no está en la base de conocimiento.")

# Ejecución del programa
while True:
    print("\nSeleccione una opción:")
    print("1. Agregar conocimiento")
    print("2. Consultar base de conocimiento")
    print("3. Salir")

    opcion = input("Opción seleccionada: ")

    if opcion == "1":
        agregar_conocimiento()
    elif opcion == "2":
        consultar_base_conocimiento()
    elif opcion == "3":
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")

