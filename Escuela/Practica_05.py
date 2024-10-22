class Universidad:
    def __init__(self,nombre_universidad):
        self.nombre_universidad = nombre_universidad

class Carrera:
    def __init__(self, especialidad):
        self.especialidad = especialidad

#Heredando atributos
#class Estudiante(Universidad,Carrera):
#    def __init__ (self,nombre, edad, nombre_universidad, especialidad):
#        Universidad.__init__(self,nombre_universidad)
#        Carrera.__init__(self, especialidad)
#        self.nombre = nombre
#        self.edad = edad
        
#    def mostrar_informacion(self):
#        return f"""
#        Especilidad: {self.especialidad}
#        Edad: {self.edad}
#        Nombre: {self.nombre}
#        Universidad: {self.nombre_universidad}"""

#Sin heredar atributos
class Estudiante:
    def __init__(self,nombre,edad,universidad,especialidad):
        self.nombre = nombre
        self.edad = edad
        self.universidad = Universidad(universidad)
        self.especialidad = Carrera(especialidad)
    
    def mostrar_informacion(self):
        return f"""
        Especilidad: {self.especialidad}
        Edad: {self.edad}
        Nombre: {self.nombre}
        Universidad: {self.universidad.nombre_universidad}"""

if __name__ == "__main__":
    e1 = Estudiante("Mateo Dominguez",20,"Ist 130","Analista en Sistemas")
    print(e1.mostrar_informacion())