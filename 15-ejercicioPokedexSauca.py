# Crea una clase Pokemon para llevar un registro de pokemon capturados
# Los pokemon tendran nombre, tipo, nivel y si estan capturados o no
# Habra un contador del numero de pokemon capturados y otro de vistos
#
# LOS POKEMON NACEN LIBRES!!!
# Ningún pokemon puede nacer capturado. No nacen en cautividad
#
# Crea un método para capturar un pokemon. El método tendrá en cuenta que la probabilidad
# de captura de un pokemon es del 40%

import random

class Pokemon:

    capturados = 0
    vistos = 0

    def __init__(self, name, clase, lvl):
        self.nombre = name
        self.tipo = clase
        self.nivel = lvl
        self.capturado = False
        Pokemon.vistos += 1

    def capturar(self):
        exito = random.randint(1,100)
        if exito <= 40:
            self.capturado = True
            Pokemon.capturados += 1
            return True, exito
        else:
            return False, exito
    
pokemon_1 = Pokemon("Pikachu", "Eléctrico", 10)
pokemon_2 = Pokemon("Blastoise", "Agua", 95)

print(f"Has visto {Pokemon.vistos} pokemon")

x, y = pokemon_1.capturar()
if x:
    print(f"Has capturado a {pokemon_1.nombre}, tienes {Pokemon.capturados} pokemon")
    print(f"La probabilidad fue: {y}")
else:
    print(f"No has capturado a {pokemon_1.nombre}, tienes {Pokemon.capturados} pokemon")
    print(f"La probabilidad fue: {y}")


# MENU POKEDEX:

print("¿qué deseas hacer")
print("1. Pokemon capturados")
print("2. Pokemon vistos")
print("3. Salir")

opcion = input("Elige una opción: ")

if opcion == "1":
    Pokemon.capturados
    print("Los pokemon capturados son: " , Pokemon.capturados)

elif opcion == "2":
    Pokemon.vistos
    print("Los pokemon vistos son: " , Pokemon.vistos)

elif opcion == "3":
    print("Ha decidido salir")
    break

else:
    print("Opción no válida")