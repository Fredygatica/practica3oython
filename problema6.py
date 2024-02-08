class Producto:
    def __init__(self, nombre, codigo, precio, año):
        self.nombre = nombre
        self.codigo = codigo
        self.precio = precio
        self.año = año

    def __str__(self):
        return f"Nombre: {self.nombre}, Código: {self.codigo}, Precio: {self.precio}, Año: {self.año}"


class Catalogo:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        print("Lista de productos:")
        for producto in self.productos:
            print(producto)

    def filtrar_por_año(self, año):
        print(f"Productos para el año {año}:")
        for producto in self.productos:
            if producto.año == año:
                print(producto)


# Ejemplo de uso:
if __name__ == "__main__":
    catalogo = Catalogo()

    # Agregar productos al catálogo
    producto1 = Producto("Llanta", "001", 50.0, 2022)
    producto2 = Producto("Batería", "002", 100.0, 2023)
    producto3 = Producto("Filtro de aceite", "003", 10.0, 2022)

    catalogo.agregar_producto(producto1)
    catalogo.agregar_producto(producto2)
    catalogo.agregar_producto(producto3)

    # Mostrar la lista completa de productos
    catalogo.mostrar_productos()

    # Filtrar productos por año
    catalogo.filtrar_por_año(2022)