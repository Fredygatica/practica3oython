import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio ** 2

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2

def mostrar_menu():
    print("Menú:")
    print("1. Calcular área de un círculo")
    print("2. Calcular área de un rectángulo")
    print("3. Calcular área de un cuadrado")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")
    return opcion