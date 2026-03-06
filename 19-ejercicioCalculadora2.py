# Crea una clase Calculadora que reciba dos numeros.
# Haz los siguientes métodos:
#   - un metodo para sumar los dos números
#   - Un metodo para restar los dos números
#   - Al hacer print de un objeto Calculadora se impriman los dos números
# Añade try-except para validar la entrada de datos


class Calculadora:
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2
        self.resultado = None

    def __str__(self):
        return (f"Los números para las operacione son {self.numero1} y {self.numero2}")
        # return (f"Resultado suma es: {self.sumar}, Resultado resta es: {self.restar}, Resultado multiplicacion es {self.multiplicar}, Resultado division {self.dividir}")

    def sumar (self):
        try:
            self.resultado = self.numero1 + self.numero2
        except:
            try:
                self.resultado = int(self.numero1) + int(self.numero2)
            except:
                self.resultado = "No son numeros los datos introducidos"
        return self.resultado
                 

    def restar (self):
        resultado_resta = str(self.numero1 - self.numero2)
        return resultado_resta
    
    def multiplicar (self):
        resultado_mul = str(self.numero1 * self.numero2)
        return resultado_mul
    
    def dividir (self):
        resultado_div = str(self.numero1 / self.numero2)
        return resultado_div


calc1 = Calculadora("patata",2)

print(calc1.sumar())
