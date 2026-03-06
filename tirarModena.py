# Nivel 1 — Lanzamiento de moneda (Básico)
# Crear una clase Moneda que simule lanzar una moneda n veces.
# Requisitos: 
#  - La moneda puede salir "cara" o "cruz".
#  - Simular el lanzamiento n veces.
#  - Mostrar: 
#       - Número total de caras
#       - Número total de cruces

import random

class Moneda:
    def __init__(self, lanzamiento):
        self.lanzamiento = lanzamiento

    def lanzar(self):
        cara = 0
        cruz = 0
        for n in range (self.lanzamiento):
            moneda = random.choice(["cara", "cruz"])
            if moneda == "cara":
                cara += 1
            else:
                cruz += 1
        print("El numero de lanzamientos son: ", self.lanzamiento)
        print("El numero de caras son:", cara)
        print("El numero de cruces son:", cruz)

moneda = Moneda (100)
moneda.lanzar ()







        
