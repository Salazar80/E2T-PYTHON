# Ejercicio 3: Lista de números pares 
# Crea una clase Numeros con un atributo que sea una lista de enteros. 
# Incluye un método que devuelva solo los números pares de esa lista.


class Numeros:
    def __init__(self, lista):
        self.lista = lista

    def numero_par (self):
        pares = []
        for i in self.lista:
            if i % 2 == 0:
                pares.append(i)
        return pares
    
lista = range(1,10)

pares = Numeros(lista)

print(pares.numero_par())

