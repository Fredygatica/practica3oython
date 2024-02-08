class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mostrar_punto(self):
        print(f"Coordenadas del punto: ({self.x}, {self.y})")

    def mover_punto(self, nueva_x, nueva_y):
        self.x = nueva_x
        self.y = nueva_y


# Ejemplo de uso:
if __name__ == "__main__":
    punto1 = Punto(3, 5)
    punto1.mostrar_punto()

    