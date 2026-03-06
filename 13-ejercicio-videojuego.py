# Haz un videojuego usando clases 
# Hay la clase Personaje que tiene nombre, vida y una funcion de ataque
# El jugador y el enemigo son Personajes y atacan por turnos
# Gana quien deje la vida del otro a 0


import random


class Personaje:
    def __init__(self, nick, life): # CONSTRUCTOR __INIT__
        self.nombre = nick
        self.vida = life

    def atacar(self):
        return random.randint(1,15)
        

jugador = Personaje("Jugador", 50)  # variable "jugador", donde se mete un objeto "jugador", "50"
enemigo = Personaje("Enemigo", 50)
turno = 1   # se pone esta variable para mostrar el turno de cada uno


while jugador.vida > 0 and enemigo.vida > 0:
    enemigo.vida -= jugador.atacar()
    jugador.vida -= enemigo.atacar()
    # esto se hace para mostrar en filas las vidas que les va quedando a cada uno
    print("\nturno:", turno)
    print("Vida jugador", "#" * jugador.vida)
    print("Vida enemigo", "#" * enemigo.vida)
    turno +=1    

if jugador.vida <= 0:
        print("Jugador eliminado")
else:
        print("Jugador gana")


    






