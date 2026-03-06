class Cuenta:

    def __init__(self, usuario, saldo_inicial):
        self.usuario = usuario
        self.saldo = saldo_inicial

    def ingresar(self, cantidad):
        self.saldo += cantidad

    def retirar(self, cantidad):
        self.saldo -= cantidad


# Crear cuenta
nombre = input("Introduce tu nombre: ")
saldo_inicial = float(input("Introduce el saldo inicial: "))

cuenta = Cuenta(nombre, saldo_inicial)

# Elegir operación
print("¿Qué deseas hacer?")
print("1. Ingresar dinero")
print("2. Retirar dinero")

opcion = input("Elige una opción (1 o 2): ")

if opcion == "1":
    cantidad = float(input("¿Cuánto deseas ingresar? "))
    cuenta.ingresar(cantidad)

elif opcion == "2":
    cantidad = float(input("¿Cuánto deseas retirar? "))
    cuenta.retirar(cantidad)

else:
    print("Opción no válida")

# Mostrar saldo final
print("Saldo final:", cuenta.saldo)