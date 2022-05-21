class Triangulo:
    """
    Define un triángulo según su base y su altura.
    """
    def __init__(self, b, h):
        self.b = b
        self.h = h

    def area(self):
        return (self.b * self.h) / 2
    
triangulo = Triangulo(20, 10)
print("Área del triangulo: ", triangulo.area())