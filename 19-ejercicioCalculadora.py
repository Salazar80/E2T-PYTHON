# Crea una clase Calculadora que reciba dos numeros.
# Haz los siguientes métodos:
#   - un metodo para sumar los dos números
#   - Un metodo para restar los dos números
#   - Al hacer print de un objeto Calculadora se impriman los dos números


class Calculadora:
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2

    def __str__(self):
        return (f"Los números son {self.numero1} y {self.numero2}")
        # return (f"Resultado suma es: {self.sumar}, Resultado resta es: {self.restar}, Resultado multiplicacion es {self.multiplicar}, Resultado division {self.dividir}")

    def sumar (self):
        resultado_suma = str(self.numero1 + self.numero2)
        return resultado_suma

    def restar (self):
        resultado_resta = str(self.numero1 - self.numero2)
        return resultado_resta
    
    def multiplicar (self):
        resultado_mul = str(self.numero1 * self.numero2)
        return resultado_mul
    
    def dividir (self):
        resultado_div = str(self.numero1 / self.numero2)
        return resultado_div

# numeros = Calculadora(4,5)

suma = Calculadora(4,2)
resta = Calculadora(6,5)
multiplicacion = Calculadora(4,2)
division = Calculadora(6,35)

# print(numeros)

print("\nEl resultado de la suma es: " + suma.sumar())
print("El resultado de la resta es: " + resta.restar())
print("El resultado de la multiplicacion es: " + multiplicacion.multiplicar())
print("El resultado de la division es: " + division.dividir() + "\n")






