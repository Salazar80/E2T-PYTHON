
import random


class Cuentas:
    def __init__(self, name, balance):
        self.titular = name
        self.saldo = balance
        self.iban = self.numero_cuenta()

        
    def retirar_dinero(self,cantidad):
        self.saldo -= cantidad
        

    def ingresar_dinero(self,cantidad):
        self.saldo += cantidad

    
    def numero_cuenta(self):
        cuenta = ""
        for i in range(20):
            cuenta += str(random.randint(0,9))
        return cuenta


   
       
cuenta_banco = Cuentas("Antonio", 1200)

# print(f"La cuenta de {cuenta_banco.titular} tiene {cuenta_banco.saldo} €\nEl IBAN es {cuenta_banco.iban}")

# print("El IBAN por 2ª vez es ", cuenta_banco)

while True:
    print("BANCO SALAZAR")
    print("Elija una ocpión")
    print("1. Conslutar saldo")
    print("2. Retirar dinero")
    print("3. Ingresar dinero")
    print("4. Salir")
    opcion = int(input("Introduzca opcion: "))

    if opcion == 1:
        print(f"Titular: {cuenta_banco.titular} \nSaldo: {cuenta_banco.saldo} € \nIBAN: {cuenta_banco.iban}")
    elif opcion == 2:
        cuenta = int(input("Dinero a retirar: "))
        cuenta_banco.retirar_dinero(cuenta)
    elif opcion == 3:
        cuenta = int(input("Dinero a ingresar: "))
        cuenta_banco.ingresar_dinero(cuenta)
    elif opcion == 4:
        break
    else:
        print("Opcion no valida")