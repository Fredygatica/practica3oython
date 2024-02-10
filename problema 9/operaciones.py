def suma(a, b):
    try:
        resultado = a + b
        return resultado
    except TypeError:
        print("Error: Tipo de dato no válido.")
        return None

def resta(a, b):
    try:
        resultado = a - b
        return resultado
    except TypeError:
        print("Error: Tipo de dato no válido.")
        return None

def producto(a, b):
    try:
        resultado = a * b
        return resultado
    except TypeError:
        print("Error: Tipo de dato no válido.")
        return None

def division(a, b):
    try:
        if b == 0:
            raise ZeroDivisionError("No es posible dividir entre cero.")
        resultado = a / b
        return resultado
    except TypeError:
        print("Error: Tipo de dato no válido.")
        return None
    except ZeroDivisionError as e:
        print("Error:", e)
        return None