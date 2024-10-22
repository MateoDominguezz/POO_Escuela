class Vehiculo:
    def __init__(self, marca, modelo, velocidad_maxima):
        self.marca = marca
        self.modelo = modelo
        self.velocidad_maxima = velocidad_maxima
        self.estado = False
    
    def arrancar(self):
        if self.estado == False:
            self.estado = True
            return f"Su vehiculo arranco"
        else:
            return f"Su vehiculo ya esta encendido"

    def detener(self):
        if self.estado == True:
            self.estado = False
            return f"Se esta deteniendo el vehiculo"
        else:
            return f"Su vehiculo ya estaba detenido"
        
    def mostrar_informacion(self):
        return f"""
        Marca: {self.marca}
        Modelo: {self.modelo}
        Velocidad Maxima: {self.velocidad_maxima}"""


class Auto(Vehiculo):
    def __init__ (self,marca, modelo, velocidad_maxima, numero_puerta):
        super().__init__(marca, modelo, velocidad_maxima)
        self.numero_puerta = numero_puerta

    def mostrar_informacion(self):
        return f"""
        Marca: {self.marca}
        Modelo: {self.modelo}
        Velocidad Maxima: {self.velocidad_maxima}
        Numero de puertas: {self.numero_puerta}"""

class Moto(Vehiculo):
    def __init__(self,marca, modelo, velocidad_maxima,tipo_moto):
        super().__init__(marca, modelo, velocidad_maxima)
        self.tipo_moto = tipo_moto
    
    def mostrar_informacion(self):
        return f"""
        Marca: {self.marca}
        Modelo: {self.modelo}
        Velocidad Maxima: {self.velocidad_maxima}
        Tipo de moto:{self.tipo_moto}"""
        
class Concesionario:
    def __init__(self):
        self.vehiculos = []
        
    def agregar_vehiculo(self, vehiculoo):
        self.vehiculos.append(vehiculoo)
        print("Vehiculo agregado exitosamente")
    
    def mostrar_vehiculos(self):
        for i in self.vehiculos:
            print(i.mostrar_informacion())
    
    def arrancar_todos(self):
        for i in self.vehiculos:
            print(i.arrancar())

coche1 = Auto("Toyota", "Corolla", 180, 4)
moto1 = Moto("Yamaha", "R6", 260, "Deportiva")

concesionario = Concesionario()
concesionario.agregar_vehiculo(coche1)
concesionario.agregar_vehiculo(moto1)


