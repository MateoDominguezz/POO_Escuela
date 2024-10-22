class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.estado = False
        
    def arrancar(self):
        if self.estado == False:
            self.estado = True
            return f"Vehiculo arrancando"
        else:
            return "Vehiculo ya esta en marcha"
    
    def detener (self):
        if self.estado == True:
            self.estado == False
            return f"Vehiculo detenido"
        else:
            return "Vehiculo ya esta detenido"
    
    def mostrar_informacion(self):
        estado_vehiculo = "arrancado" if self.estado else "detenido"
        return f"""
        Marca: {self.marca}
        Modelo: {self.modelo}
        Año: {self.año}
        Estado de el vehiculo: {estado_vehiculo}"""

vehiculo1 = Vehiculo("Toyota", "Corolla", 2020)


print(vehiculo1.mostrar_informacion())
print(vehiculo1.arrancar())
print(vehiculo1.arrancar())
print(vehiculo1.detener())
print(vehiculo1.mostrar_informacion())