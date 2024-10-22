class Estudiante():
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    
    def mostrar_nota (self):
        if self.nota > 10:
            return "Numero equivocado"
        elif self.nota >= 4 and self.nota <= 10:
            return f"El alumno/a: {self.nombre}, aprobo"
        else:
            return f"El alumno/a: {self.nombre}, desaprobo"
        
    def __str__(self):
        return f"""
            Su nombre es: {self.nombre}
            Su nota es: {self.nota}
            """
            
pj1 = Estudiante("Mateo", 10)
print(pj1)
print(pj1.mostrar_nota())