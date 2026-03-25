# Ejercicio 1: Calculadora básica con clases 
# Crea una clase Calculadora que tenga métodos para sumar, restar, multiplicar y dividir dos números. 
# Incluye un constructor que inicialice los dos números como atributos. 


class Calculadora:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def sumar(self):
        return self.num1 + self.num2

    def restar(self):
        return self.num1 - self.num2

    def multiplicar(self):
        return self.num1 * self.num2

    def dividir(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "Error: no se puede dividir entre 0"
        
if __name__ == "__main__":
    calc = Calculadora(5,4)
    print(calc.sumar())
    calc = Calculadora(5,4)
    print(calc.restar())
    calc = Calculadora(5,4)
    print(calc.multiplicar())
    calc = Calculadora(5,4)
    print(calc.dividir())