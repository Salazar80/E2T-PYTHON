# Crea una clase Kart.
# Cada kart tendrá un piloto, una velocidad inicial, una velocidad máxima y una aceleración.
# Haz metodos para:
#   - Acelerar, que subirá la velocidad el valor de la aceleración.
#   - Frenar, que reducirá la velocidad el valor de la aceleracion.
#   - Mostrar datos, que devolverá que el piloto x va a velocidad Y.
# Añade manejo de excepciones para evitar pasar de las velocidades máximas.


class Kart:
    def __init__(self, name, vel_ini, vel_max, aceleracion):
        self.nombre = name
        self.vel_ini = 0
        self.vel_max = vel_max
        self.acel = aceleracion

    def acelerar(self):
        try:
            resultado_a = self.vel_ini + self.acel
            if resultado_a >= self.vel_max:
                resultado_a = self.vel_max
            else:
                resultado_a
        except:
            resultado_a = "Los datos introducidos no son correctos"
        return resultado_a

    def frenar (self):
        resultado_f = self.acel - self.vel_ini
        if resultado_f >= self.acel:
            resultado_f -= self.acel
            return resultado_f

    def mostrar_datos (self):
        return (f"El piloto {self.nombre} va a {self.acelerar} km/h")


result = Kart("Mario", 180, 250, 120)
# datos = Kart()

print(result.acelerar())
#print(datos)

print(result.frenar())