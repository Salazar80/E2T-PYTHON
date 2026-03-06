class CuentaBancaria:

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

cuenta = CuentaBancaria(nombre, saldo_inicial)

# Ingresar dinero
ingreso = float(input("¿Cuánto dinero deseas ingresar? "))
cuenta.ingresar(ingreso)

# Retirar dinero
retiro = float(input("¿Cuánto dinero deseas retirar? "))
cuenta.retirar(retiro)

# Mostrar saldo final
print("Usuario:", cuenta.usuario)
print("Saldo final:", cuenta.saldo)