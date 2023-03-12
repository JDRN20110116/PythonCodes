# Definici�n de la base de conocimiento inicial
base_conocimiento = {
    "mam�feros": {
        "h�bitat": "terrestre",
        "caracter�sticas": ["pelo", "mam�feros"]
    },
    "aves": {
        "h�bitat": "a�reo",
        "caracter�sticas": ["plumas", "ov�paros"]
    },
    "peces": {
        "h�bitat": "acu�tico",
        "caracter�sticas": ["escamas", "ov�paros"]
    }
}

# Funci�n para agregar conocimiento a la base de conocimiento
def agregar_conocimiento():
    tipo_animal = input("Ingrese el tipo de animal que desea agregar: ")
    h�bitat = input("Ingrese el h�bitat del animal: ")
    caracter�sticas = input("Ingrese las caracter�sticas del animal separadas por comas: ").split(",")
    base_conocimiento[tipo_animal] = {"h�bitat": h�bitat, "caracter�sticas": caracter�sticas}
    print("Se ha agregado el conocimiento de", tipo_animal, "a la base de conocimiento.")

# Funci�n para consultar la base de conocimiento
def consultar_base_conocimiento():
    tipo_animal = input("Ingrese el tipo de animal que desea consultar: ")
    if tipo_animal in base_conocimiento:
        print("El h�bitat del", tipo_animal, "es", base_conocimiento[tipo_animal]["h�bitat"])
        print("Las caracter�sticas del", tipo_animal, "son:", ", ".join(base_conocimiento[tipo_animal]["caracter�sticas"]))
    else:
        print("Lo siento, el tipo de animal", tipo_animal, "no est� en la base de conocimiento.")

# Ejecuci�n del programa
while True:
    print("\nSeleccione una opci�n:")
    print("1. Agregar conocimiento")
    print("2. Consultar base de conocimiento")
    print("3. Salir")

    opcion = input("Opci�n seleccionada: ")

    if opcion == "1":
        agregar_conocimiento()
    elif opcion == "2":
        consultar_base_conocimiento()
    elif opcion == "3":
        break
    else:
        print("Opci�n inv�lida. Por favor, seleccione una opci�n v�lida.")

