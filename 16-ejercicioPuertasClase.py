# Crea una clase concurso que calcule el problema de Monty Hall para un número determinado de veces.
# Hay tres puertas y solo una está premiada.
# El programa hará de jugador y de presentador de manera automática, eligiendo una puerta al azar, 
#   descartando el presentador una puerta vacía no elegida y decidienco de manera de aleatoria 
#   si cambiar o no de elcción.
#
# Al final se imprimirá un informe de:
#   - El porcentaje de veces que ganó manteniendo la elección.
#   - El porcentaje de veces que ganó cambiando la elección.

import random

class Concurso:

    def __init__ (self, iteraciones):
        self.iteraciones = iteraciones
        self.puertas = [1, 2, 3]
    
    def concursar(self):
        # randon.choice = es solo para elegir de una lista []
        premio = random.choice(self.puertas)
        jugador = random.choice(self.puertas)
        
        cambia = random.randint(1, 2)   # genera dos numero, si sale el 1 cambio y si sale el 2 no cambio

        if cambia == 1 and jugador != premio:
            return True, cambia
        elif cambia == 2 and jugador == premio:
            return True, cambia
        else:
            return False, cambia
    
    def iterar(self):

        gana_cambio = 0
        gana_mantiene = 0
        pierde = 0

        for i in range(self.iteraciones):
            result = self.concursar()
            if result[0] and result[1] == 1:
                gana_cambio += 1
            elif result[0] and result[1] == 2:
                gana_mantiene += 1
            else:
                pierde += 1
        return (gana_cambio/self.iteraciones), (gana_mantiene/self.iteraciones), self.iteraciones

# if __name__ == "__main":  # esto es para hacer las pruebas

test = Concurso(1000)   # esto es instanciar el Concurso

x, y, z = test.iterar()

# print (x, y, z)
print (f"RESULTADOS\nEl jugador ha ganado el {round((x+y)*100, 2)}% de las veces\n -El {round(x*100, 2)}% de las veces cambiando\n -El {round(y*100, 2)}% de las veces manteniendo\nHa perdido el {round((1-(x+y))*100, 2)}% de las veces")