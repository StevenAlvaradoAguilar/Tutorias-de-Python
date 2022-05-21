class Alumno:

    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        """Imprime un saludo en pantalla."""
        print(f"¡Hola, {self.nombre}!")


alumno = Alumno("Pablo")
alumno.saludar()