class Producto:
    def __init__(self,nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
    def mostrar_informacion(self):
        return f"""
        Nombre: {self.nombre}
        Precio: {self.precio}"""

class Telefono(Producto):
    def __init__(self, nombre, precio, tipo_red):
        super().__init__(nombre,precio)
        self.tipo_red = tipo_red

class Computadora(Producto):
    def __init__ (self,nombre, precio, ram, procesador):
        super().__init__(nombre, precio)
        self.ram = ram
        self.procesador = procesador

class CarritoDeCompras:
    def __init__(self):
        self.productos = []
    
    def agregar_producto(self,producto):
        self.productos.append(producto)
        return "Producto agregado"

    def mostrar_productos(self):
        if not self.productos:
            print("No se encontraron productos")
        else:
            for i in self.productos:
                print(i.mostrar_informacion())
    
    def calcular_total(self):
        valor = 0
        for producto in self.productos:
            valor += producto.precio
        return valor


telefono1 = Telefono("iPhone", 1000, "5G")
computadora1 = Computadora("MacBook", 1500, "16GB", "Intel i7")

carrito = CarritoDeCompras()

carrito.agregar_producto(telefono1)
carrito.agregar_producto(computadora1)
carrito.mostrar_productos()

print(f"Total: {carrito.calcular_total()}")  