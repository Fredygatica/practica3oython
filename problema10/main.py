import menu_areas

def main():
    while True:
        opcion = menu_areas.mostrar_menu()

        if opcion == '1':
            radio = float(input("Ingrese el radio del círculo: "))
            circulo = menu_areas.Circulo(radio)
            print("El área del círculo es:", circulo.calcular_area())
        elif opcion == '2':
            base = float(input("Ingrese la base del rectángulo: "))
            altura = float(input("Ingrese la altura del rectángulo: "))
            rectangulo = menu_areas.Rectangulo(base, altura)
            print("El área del rectángulo es:", rectangulo.calcular_area())
        elif opcion == '3':
            lado = float(input("Ingrese el lado del cuadrado: "))
            cuadrado = menu_areas.Cuadrado(lado)
            print("El área del cuadrado es:", cuadrado.calcular_area())
        elif opcion == '4':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.")

if __name__ == "__main__":
    main()