# Crea una clase para hacer cuentas bancarias
# El constructor tendrá en cuenta el nombre de usuario y el saldo inicial.
# Añade métodos para:
# - Retirar dinero
# - Ingresar dinero
import random

class Cuenta:

    comision_retirada = 1.5
    cantidad_clientes = 0

    def __init__(self, name, balance):
        self.titular = name
        self.saldo = balance
        self.iban = self.numero_cuenta()
        Cuenta.cantidad_clientes += 1
    
    def retirar(self, cantidad):
        self.saldo -= (cantidad + Cuenta.comision_retirada)
    
    def ingresar(self, cantidad):
        self.saldo += cantidad

    def numero_cuenta(self):
        x = ""
        for i in range(20):
            x += str(random.randint(0, 9))
        return x

cuenta_sauca = Cuenta("Sauca", 100)
cuenta_otro = Cuenta("Fulanito", 100)

print(f"Hay {Cuenta.cantidad_clientes} cuentas creadas")

cuenta_3 = Cuenta("X", 10)
cuenta_4 = Cuenta("Y", 10)

print(f"Hay {Cuenta.cantidad_clientes} cuentas creadas")

print(f"La cuenta de {cuenta_sauca.titular} tiene {cuenta_sauca.saldo}€")
cuenta_sauca.retirar(8.5)
print(f"La cuenta de {cuenta_sauca.titular} tiene {cuenta_sauca.saldo}€")

Cuenta.comision_retirada = 10

print(f"La cuenta de {cuenta_otro.titular} tiene {cuenta_otro.saldo}€")
cuenta_otro.retirar(10)
print(f"La cuenta de {cuenta_otro.titular} tiene {cuenta_otro.saldo}€")

# Menu a medio hacer
""" while True:
    print("\nBANCO SAUCA")
    print("Elija opción:")
    print("1. Consultar datos")
    print("2. Retirar dinero")
    print("3. Ingresar dinero")
    print("4. Salir")
    print("5. ADMIN BANCO: Modificar comision")
    print("OTRO. Cuantas cuentas hay?")
    opcion = int(input("Introduzca opción: "))

    if opcion == 1:
        eleccion = int(input("\nEscoja cuenta:\n1. Cuenta Sauca\n2. Cuenta Fulanito\n"))
        if eleccion == 1:
            print(f"Titular: {cuenta_sauca.titular}\nSaldo: {cuenta_sauca.saldo}\nIBAN: {cuenta_sauca.iban}")
        else:
            print(f"Titular: {cuenta_otro.titular}\nSaldo: {cuenta_otro.saldo}\nIBAN: {cuenta_sauca.iban}")

    elif opcion == 2:
        eleccion = int(input("\nEscoja cuenta:\n1. Cuenta Sauca\n2. Cuenta Fulanito\n"))
        if eleccion == 1:
            x = float(input("Dinero a retirar: "))
            cuenta_sauca.retirar(x)
        else:
            x = float(input("Dinero a retirar: "))
            cuenta_otro.retirar(x)
    elif opcion == 3:
        x = float(input("Dinero a ingresar: "))
        cuenta_sauca.ingresar(x)
    elif opcion == 4:
        break
    elif opcion == 5:
        x = float(input("Introduzcca la cantidad de interés de retirada: "))
        Cuenta.comision_retirada = x
    else:
        print(f"Hay {Cuenta.cantidad_clientes} cuentas") """