from random import randint

# Creaciacíon de la clase
class Alumno:

    # Constructor de la clase
    def __init__(self, nombre, apellidos, edad, colores):
        # Variable de instancia nombre
        self.nombre = nombre
        self.apelidos = apellidos
        self.edad = edad
        self.colores = colores

    # Metodos
    def saludar(self):
        """Imprime un saludo en pantalla."""
        #print("Hola", self.nombre)
        #print("Mis apellidos son: ", self.apelidos)
        #print("Mi edad es de: ", self.edad)
        #print("Mi color preferido es: ", self.colores)
        print(f"¡Hola, {self.nombre}")
        print(f"los apellidos son {self.apelidos}")
        print(f"mi edad es: {self.edad}")
        print(f"mi color favorito es: {self.colores}")
        #print(f"Colores favoritos de, {self.nombre} son: {self.colores}")

alumno = Alumno("Michael", "Gómez Hernández", "23", "azul")
alumno1 = Alumno("Juan", "Gómez Orozco", "15", "rojo y naranja")

# Prints del segundo alumno
print("¡Hola", alumno1.nombre)
print("Mis apellidos son:", alumno1.apelidos)
print("Mi edad de es:", alumno1.edad)
print("Mis colores favoritos son:", alumno1.colores)
alumno.saludar()