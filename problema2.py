def main():
    while True:
        calificaciones_input = input("Ingrese las calificaciones separadas por comas: ")

        # Dividir la cadena en calificaciones individuales
        calificaciones = calificaciones_input.split(',')

        calificaciones_enteros = []

        try:
            # Convertir cada calificación a entero
            for calificacion in calificaciones:
                calificacion_entero = int(calificacion)
                calificaciones_enteros.append(calificacion_entero)

            print("Calificaciones ingresadas:", calificaciones_enteros)
            break

        except ValueError:
            print("Error: Una o más calificaciones no son números enteros.")

if __name__ == "__main__":
    main() 
