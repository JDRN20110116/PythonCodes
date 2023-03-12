from pyknow import *

# Definición del motor de inferencia
class SistemaExperto(KnowledgeEngine):
    
    # Definición de hechos
    @Fact
    def hecho1(self):
        self.declare(Fact(temperatura=20))

    @Fact
    def hecho2(self):
        self.declare(Fact(humedad_relativa=80))

    # Definición de reglas
    @Rule(Fact(temperatura=P(lambda x: x >= 30)))
    def regla1(self):
        print("La temperatura es demasiado alta")

    @Rule(Fact(humedad_relativa=P(lambda x: x >= 70)))
    def regla2(self):
        print("La humedad es demasiado alta")

    @Rule(Fact(temperatura=P(lambda x: x <= 10)))
    def regla3(self):
        print("La temperatura es demasiado baja")

    @Rule(Fact(humedad_relativa=P(lambda x: x <= 30)))
    def regla4(self):
        print("La humedad es demasiado baja")

# Creación de instancia del motor de inferencia
sistema_experto = SistemaExperto()

# Carga de hechos
sistema_experto.reset()
sistema_experto.declare(Fact(temperatura=35))
sistema_experto.declare(Fact(humedad_relativa=60))

# Ejecución de reglas
sistema_experto.run()

