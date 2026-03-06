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

    def __init__(self, iteraciones):
        self.iteraciones = iteraciones
        self.puertas = [1, 2, 3]

    def concursar(self):
        # contadores para estadísticas
        ganadas_sin_cambiar = 0
        ganadas_cambiando = 0

        for i in range(self.iteraciones):
            premio = random.choice(self.puertas)
            jugador = random.choice(self.puertas)

            # decidir aleatoriamente si el jugador cambia
            cambia = random.choice([True, False])

            if cambia:
                # cambiar a una de las puertas restantes (excepto la inicial)
                otras_puertas = []
                for x in self.puertas:
                    if x != jugador:
                        otras_puertas.append(x)
                jugador_final = random.choice(otras_puertas)
            else:
                jugador_final = jugador

            # actualizar contadores según el resultado
            if jugador_final == premio:
                if cambia:
                    ganadas_cambiando += 1
                else:
                    ganadas_sin_cambiar += 1

        # calcular porcentajes
        porcentaje_sin_cambiar = (ganadas_sin_cambiar / self.iteraciones) * 100
        porcentaje_cambiando = (ganadas_cambiando / self.iteraciones) * 100

        # imprimir informe
        print(f"Ganadas sin cambiar: {porcentaje_sin_cambiar:.2f}%")
        print(f"Ganadas cambiando: {porcentaje_cambiando:.2f}%")


# Crear instancia y ejecutar
juego = Concurso(100)
juego.concursar()


# a lo que se lanza en python se le llama "main"