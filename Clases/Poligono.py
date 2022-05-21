class Poligono:
    """
    Define un polígono según su base y su altura.
    """
    def __init__(self, b, h):
        self.b = b
        self.h = h

class Rectangulo(Poligono):

    def area(self):
        return self.b * self.h

class Triangulo(Poligono):

    def area(self):
        return (self.b * self.h) / 2

valor1 = int(input("Introduce la base del rectángulo: "))
valor2 = int(input("Introduce la altura del rectángulo: "))
rectangulo = Rectangulo(valor1, valor2)

valor3 = int(input("Introduce la base del triangulo: "))
valor4 = int(input("Introduce la altura del triangulo: "))
triangulo = Triangulo(valor3, valor4)

print("Área del rectángulo: ", rectangulo.area())
print("Área del triángulo:", triangulo.area())