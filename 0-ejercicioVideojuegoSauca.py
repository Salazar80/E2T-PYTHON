# Haz un videojuego usando clases
# Hay la clase Personaje que tiene nombre, vida y una función de ataque
# El jugador y el enemigo son Personaje y atacan por turnos
# Gana quien deje la vida del otro a 0
import random

class Personaje:
    def __init__(self, nick, life):
        self.nombre = nick
        self.vida = life

    def atacar(self):
        return random.randint(1,15)

jugador = Personaje("SuMorenitoh19", 50)
enemigo = Personaje("Enemigo", 50)
turno = 1
while jugador.vida > 0 and enemigo.vida > 0:
    enemigo.vida -= jugador.atacar()
    jugador.vida -= enemigo.atacar()
    print("\nTurno:", turno)
    print("Vida jugador:","#"*jugador.vida)
    print("Vida enemigo:","#"*enemigo.vida)
    turno += 1

if jugador.vida <= 0:
    print(f"El jugador {jugador.nombre} ha perdido")
else:
    print("El jugador ha ganado")