# Ejercicio 2: Contador de palabras 
# Escribe una función que reciba una cadena de texto y devuelva cuántas palabras contiene. 
# Luego, crea una clase Texto que use esa función como método y almacene el texto como atributo. 


def contar_palabras(frase):
    palabras = frase.split()
    return len(palabras)
    

class Texto:
    def __init__(self, frase):
        self.frase = frase

    def contar_palabras(self):
        return contar_palabras(self.frase)


# Pedir texto
frase = input("Introduce una frase: ")

# Crear objeto
texto = Texto(frase)

# Mostrar resultado
print("Número de palabras:", texto.contar_palabras())


# otra forma de hacerlo más sencilla
'''
class Texto:
    def __init__(self, frase):
        self.frase = frase

    def contar_palabras(self):
        return len(self.frase.split())


# Pedir texto
frase = input("Introduce una frase: ")

# Crear objeto
texto = Texto(frase)

# Mostrar resultado
print("Número de palabras:", texto.contar_palabras())
'''