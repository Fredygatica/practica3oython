def obtener_porcentaje(fraction):
    try:
        x, y = map(int, fraction.split('/'))
        if x <= 0 or y == 0 or x > y:
            print("X debe ser menor o igual a Y, y Y no puede ser 0.")
            return None

        percentage = (x / y) * 100

        if percentage < 1:
            return 'E'
        elif percentage > 99:
            return 'F'
        else:
            return round(percentage)

    except ValueError:
        print("Por favor, ingrese una fracción válida.")
        return None
    except ZeroDivisionError:
        print("Y no puede ser 0.")
        return None

def main():
    while True:
        fraction = input("Ingrese una fracción en formato X/Y (enteros): ")
        resultado = obtener_porcentaje(fraction)
        if resultado is not None:
            if resultado == 'E':
                print("La cantidad de combustible en el tanque es menor al 1%.")
            elif resultado == 'F':
                print("La cantidad de combustible en el tanque es mayor al 99%.")
            else:
                print(f"La cantidad de combustible en el tanque es: {resultado}%")
            break

if __name__ == "__main__":
    main()
    