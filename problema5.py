class Alumno:
    def __init__(self, nombre, num_registro):
        self.nombre = nombre
        self.num_registro = num_registro
        self.edad = None
        self.notas = []

    def display(self):
        print("Información del estudiante:")
        print("Nombre:", self.nombre)
        print("Número de Registro:", self.num_registro)
        if self.edad is not None:
            print("Edad:", self.edad)
        else:
            print("Edad: No asignada")
        if self.notas:
            print("Notas:", ", ".join(map(str, self.notas)))
        else:
            print("Notas: No asignadas")

    def set_age(self, edad):
        self.edad = edad

    def set_notas(self, notas):
        self.notas = notas

# Ejemplo de uso:
if __name__ == "__main__":
    # Crear un objeto Alumno
    alumno1 = Alumno("fredy", "F12345")

    # Asignar la edad del estudiante
    alumno1.set_age(24)

    # Asignar las notas del estudiante
    alumno1.set_notas([15, 20, 18])

    # Mostrar la información del estudiante actualizada
    alumno1.display()