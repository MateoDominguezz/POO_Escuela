class Empleado:
    def __init__(self, nombre, edad, salario_base):
        self.nombre = nombre
        self.edad = edad
        self.salario_base = salario_base
        
    def calcular_salario(self):
        return self.salario_base
    
    def mostrar_informacion(self):
        return f"""
        Nombre: {self.nombre}
        Edad: {self.edad}
        Salario: {self.salario_base}"""

class Gerente(Empleado):
    def __init__(self,nombre,edad, salario_base, bono):
        Empleado.__init__(self,nombre, edad, salario_base)
        self.bono = bono
    
    def calcular_salario(self):
        return self.salario_base + self.bono

class Tecnico(Empleado):
    def __init__(self, nombre, edad, salario_base,horas_extras, pago_por_hora_extra):
        Empleado.__init__(self,nombre, edad, salario_base)
        self.horas_extras = horas_extras
        self.pago_por_hora_extra = pago_por_hora_extra
    
    def calcular_salario(self):
        cuenta = self.salario_base + (self.horas_extras * self.pago_por_hora_extra)
        return cuenta
        
class Empresa:
    def __init__(self):
        self.empleados = []
    
    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)
        print("Empleado agregado satisfactoriamente")
    
    def mostrar_empleados(self):
        for empleado in self.empleados:
            print(empleado.mostrar_informacion())
    
    def calcular_costos_salarios(self):
        costos = 0
        for empleado in self.empleados:
            costos += empleado.calcular_salario()
        print(f"El costo total de los salarios mensuales es: {costos}")
        

empleado1 = Empleado("Ana", 30, 1500)
gerente1 = Gerente("Carlos", 45, 3000, 1000)  
tecnico1 = Tecnico("Luis", 25, 2000, 10, 20)  


empresa = Empresa()
empresa.agregar_empleado(empleado1)
empresa.agregar_empleado(gerente1)
empresa.agregar_empleado(tecnico1)

empresa.mostrar_empleados()
empresa.calcular_costos_salarios()