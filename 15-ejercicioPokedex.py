# crea una clase de Pokemon para llevar un registro de pokemon capturados
# Los pokemos tendran nombre, tipo, nivel y si estan capturados o no
# Habra un contador del numero de Pokemon capturados y otro de vistos
#
# LOS POKEMOS NACEN LIBRES!!!
# Ningun pokemon puede nacer capturado. No nacen en cautividad
#
# Crea un metodo para capturar un pokemon. El metodo tendra en cuenta que la probabilidad de captura de un pokemon es del 40%.

import random

class Pokemon:

    capturados = 0
    vistos = 0

    def __init__(self, name, clase, level):
        self.nombre = name
        self.tipo = clase
        self.nivel = level
        self.capturado = False
        Pokemon.vistos += 1     # Esto es porque cada vez que se cree un pokemon se le suma 1

    def capturar(self):
        exito = random.randint(1,100)
        if exito <= 4:
            self.capturado = True
            Pokemon.capturados += 1
            return True
        else:
            return False

        

pokemon_1 = Pokemon ("Pikachu","Electrico", 10)
pokemon_2 = Pokemon ("Blastoise","Agua", 95)


print(f"Has visto {Pokemon.vistos} pokemon")

if pokemon_1.capturar():
    print (f"Has capturado a {pokemon_1.nombre}, tienes {Pokemon.capturados} pokemon")
else:
    print (f"No has capturado a {pokemon_1.nombre}, tienes {Pokemon.capturados} pokemon")
