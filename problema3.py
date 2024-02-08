import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        # El área de un círculo se calcula como pi * radio al cuadrado
        area = math.pi * (self.radio ** 2)
        return area

# Ejemplo de uso:
if __name__ == "__main__":
    # Crear un objeto Circulo con radio 5
    circulo1 = Circulo(5)

    # Calcular el área del círculo
    area_circulo1 = circulo1.calcular_area()
    print("El área del círculo con radio 5 es:", area_circulo1)

 
   