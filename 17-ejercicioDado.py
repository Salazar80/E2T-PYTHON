# Haz una clase Dado que simule el lanzamiento de un dado de 2 caras (moneda)



import random

class Dado:
    def __init__(self):
        self.caras = 2

    def lanzar (self):
        resultado = random.randint(1, self.caras)   # randint tiene inicio y fin
        return resultado

        
dado = Dado()
print(dado.lanzar())
