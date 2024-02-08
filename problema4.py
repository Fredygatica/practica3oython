class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def calcular_area(self):
        # El área de un rectángulo se calcula como largo * ancho
        area = self.largo * self.ancho
        return area

# Ejemplo de uso:
if __name__ == "__main__":
    # Crear un objeto Rectangulo con largo 5 y ancho 10
    rectangulo1 = Rectangulo(5, 10)

    # Calcular el área del rectángulo
    area_rectangulo1 = rectangulo1.calcular_area()
    print("El área del rectángulo con largo 5 y ancho 10 es:", area_rectangulo1)

    