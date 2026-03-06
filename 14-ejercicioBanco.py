# Crea una clase para hacer cuentas bancarias 
# El constructor tendrá en cuenta el nombre de usuario y el saldo inicial.
# Añade metodos para:
    # - Retirar dinero
    # - Ingresar dinero


import random
import string

# cuenta = ""

# for i in range(22):
    # numeracion = string.digits
    # cuenta += random.choice(numeracion)

# print(cuenta)


# cantidad = int(input("Introduzca saldo inicial: "))


class Cuentas:
    def __init__(self, name, saldo_inicial):
        self.nombre = name
        self.saldo = saldo_inicial
        

    def retirar_dinero(self,cantidad):
        if cantidad < 0:
            print("La cantidad debe ser positiva")
        elif cantidad > self.saldo:
            print("Su saldo es insuficiente")
        else:
            self.saldo -= cantidad
            print("Retirada realizado. Su saldo actual es: " + str(self.saldo) + "€")    


    def ingresar_dinero(self,cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print("Ingreso realizado. Su saldo actual es: " + str(self.saldo) + "€") 
        else:
            print("La cantidad debe ser positiva")


   


    def mostrar_saldo(self):
        print("Titular: " + self.nombre + ". " "Su saldo actual es: " + str(self.saldo) + "€")

            
cuenta_banco = Cuentas("Antonio", 1200)

cuenta_banco.mostrar_saldo()
cuenta_banco.ingresar_dinero(100)
cuenta_banco.retirar_dinero(1500)





