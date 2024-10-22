class Vehiculo:
    def __init__(self,id_vehiculo, capacidad_total):
        self.id_vehiculo = id_vehiculo
        self.capacidad_total = capacidad_total
        self.capacidad_disponible = capacidad_total 
    
    def asignar_envio(self, peso):
        if peso <= self.capacidad_disponible:
            self.capacidad_disponible -= peso
            return f"Se le asignó el envío a: {self.id_vehiculo}, con un peso de: {peso} kg"
        else:
            return f"Sin capacidad para cargar el peso {peso} kg"
    
    def mostrar_informacion(self):
        return f"""
        ID Vehiculo: {self.id_vehiculo}
        Capacidad Total: {self.capacidad_total}
        Capacidad Disponible: {self.capacidad_disponible}"""
    
    def capacidad_restante(self):
        return self.capacidad_disponible 


class Camion(Vehiculo):
    def __init__(self,id_vehiculo, capacidad_total, tipo_combustible, distancia_maxima):
        super().__init__(id_vehiculo, capacidad_total)
        self.tipo_combustible = tipo_combustible
        self.distancia_maxima = distancia_maxima

    def mostrar_informacion(self):
        return f"""
        {super().mostrar_informacion()}
        Tipo de combustible: {self.tipo_combustible}
        Distancia Máxima: {self.distancia_maxima} km"""


class Drone(Vehiculo):
    def __init__(self,id_vehiculo, capacidad_total, autonomia):
        super().__init__(id_vehiculo,capacidad_total)
        self.autonomia = autonomia
    
    def mostrar_informacion(self):
        return f"""
        {super().mostrar_informacion()}
        Autonomía: {self.autonomia} horas"""


class Barco(Vehiculo):
    def __init__(self, id_vehiculo, capacidad_total, tipo_barco, puertos_destino):
        super().__init__(id_vehiculo, capacidad_total)
        self.tipo_barco = tipo_barco
        self.puertos_destino = puertos_destino

    def mostrar_informacion(self):
        return f"""
        {super().mostrar_informacion()}
        Tipo de barco: {self.tipo_barco}
        Puertos a los que llega: {', '.join(self.puertos_destino)}"""


class EmpresaLogistica:
    def __init__ (self):
        self.flota = []
    
    def mostrar_flota(self):
        for vehiculo in self.flota:
            print(vehiculo.mostrar_informacion())  
    
    def buscar_vehiculo_disponible(self, peso_envio):
        for vehiculo in self.flota:
            if vehiculo.capacidad_restante() >= peso_envio:  
                print(f"Vehículo disponible para el envío: {vehiculo.id_vehiculo}")
                print(vehiculo.asignar_envio(peso_envio))
                return
        print(f"No se encontró un vehículo con capacidad suficiente para mover el peso de {peso_envio} kg.")
    
    def agregar_vehiculo(self, vehiculo):
        self.flota.append(vehiculo)
        return f"El vehículo {vehiculo.id_vehiculo} se agregó a la flota"
    
    def asignar_envio(self, id_vehiculo, peso_envio):
        for vehiculo in self.flota:
            if vehiculo.id_vehiculo == id_vehiculo:
                if peso_envio <= vehiculo.capacidad_disponible:
                    return vehiculo.asignar_envio(peso_envio)
                else:
                    return f"El vehículo {id_vehiculo} no tiene suficiente capacidad."
        return f"No se encontró el vehículo con ID {id_vehiculo}."



empresa = EmpresaLogistica()

camion1 = Camion("CAM-001", 20000, "Diesel", 800)
drone1 = Drone("DRN-001", 100, 2)
barco1 = Barco("BAR-001", 50000, "Carguero", ["Puerto A", "Puerto B", "Puerto C"])


print(empresa.agregar_vehiculo(camion1))
print(empresa.agregar_vehiculo(drone1))
print(empresa.agregar_vehiculo(barco1))
empresa.mostrar_flota()
print(empresa.asignar_envio("CAM-001", 5000))
print(empresa.asignar_envio("DRN-001", 50))
print(empresa.buscar_vehiculo_disponible(25000))
empresa.mostrar_flota()