class DispositivoEntrada():
    def __init__ (self, marca, tipo_marca):
        self.marca = marca
        self.tipo_marca = tipo_marca

class ContadorRaton(DispositivoEntrada):
    contador = 0
    def __init__ (self, marca, tipo_marca):
        super().__init__(marca,tipo_marca)
        ContadorRaton.contador += 1
        self.id_raton = ContadorRaton.contador
    
    def __str__ (self):
        return f"""
        Marca: {self.marca}
        Tipo_marca: {self.tipo_marca}
        Cantidad: {self.id_raton}"""
        
class ContadorTeclado(DispositivoEntrada):
    contador = 0
    def __init__ (self, marca, tipo_marca):
        super().__init__(marca,tipo_marca)
        ContadorTeclado.contador += 1
        self.id_teclado = ContadorTeclado.contador
    
    def __str__ (self):
        return f"""
        Marca: {self.marca}
        Tipo_marca: {self.tipo_marca}
        Cantidad: {self.id_teclado}"""

class Monitor():
    contador = 0
    def __init__ (self, marca,tamaño):
        Monitor.contador += 1
        self.marca = marca
        self.tamaño = tamaño
        self.id_monitor = Monitor.contador
    
    def __str__ (self):
        return f"""
        Marca: {self.marca}
        Tamaño: {self.tamaño}
        Cantidad: {self.id_monitor}"""
        
class Computadora():
    contador = 0
    def __init__ (self, nombre, monitor, teclado, raton):
        Computadora.contador += 1
        self.id_computadora = Computadora.contador
        self.nombre = nombre
        self.monitor = monitor
        self.teclado = teclado
        self.raton = raton
    
    def __str__ (self):
        return f"""
        id_computadora: {self.id_computadora}
        Nombre: {self.nombre}
        Monitor: {self.monitor}
        Teclado: {self.teclado}
        Raton: {self.raton}"""

class Orden():
    contador = 0
    def __init__ (self):
        Orden.contador += 1
        self.id_orden = Orden.contador
        self.computadoras = []
    
    def agregar_computadora(self,computadora):
        self.computadoras.append(computadora)
        return f"La Computadora: {computadora}, se agrego"
    
    def __str__ (self):
        computadoras = ""
        for computadora in self.computadoras:
            computadoras += f"{computadora}"
        return f"""
        Orden: {self.id_orden}
        Computadoras: {computadoras}"""

monitor = Monitor("Dell", "24 pulgadas")
teclado = ContadorTeclado("Logitech", "USB")
raton = ContadorRaton("Logitech", "USB")

computadora = Computadora("PC Gamer", monitor, teclado, raton)
orden = Orden()
print(orden.agregar_computadora(computadora))
print(orden)
        