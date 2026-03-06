class Persona:
    def __init__(self, name, age, rank):  # init = constructor - # esto se refiere a la instancia cocreta de la clase Persona. Se referira a cada persona
        self.nombre = name                  # una funcion dentro de una clase se un METODO
        self.edad = age
        self.empleo = rank

    def correr(self):
        print(f"{self.nombre} esta corriendo")

    # def saludar():
        #print("Mano al botón")  # no se pone self porque es un objeto/instacia para todos.

    def cumpleanos(self):
        self.edad += 1
        print(f"Feliz cumple, {self.nombre} por tu {self.edad} cumpleaños")



antonio = Persona("Antonio", 45, "Sgt1")    # esto es un objeto de clase
pepe = Persona("Pepe", 40, "Sgt1")          # esto es un objeto de clase

# Persona.saludar()


pepe.cumpleanos()
antonio.cumpleanos()

pepe.cumpleanos()
antonio.cumpleanos()