# Haz una clase Dado que simule el lanzamiento de un dado de 2 caras (moneda)
# Modificalo para introducir el numero de caras al instanciar la clase


import random

class Dado:
    def __init__(self, caras):
        self.caras = caras

    def __str__(self):
        return ("La cara que ha salido es: " + str(self.lanzar()))

    def lanzar (self):
        resultado = random.randint(1, self.caras)   # randint tiene inicio y fin
        return resultado
    

        
dado = Dado(2)
d6 = Dado(6)
d8 = Dado(8)
d10 = Dado(10)
d12 = Dado(12)
d20 = Dado(20)

print(d6)   # esto daria de resultado <__main__.Dado object at 0x000001868770CE10> siempre que no tenga un metodo str <<def __str__(self):>>
