class Estudiante:
    def __init__(self,nombre, edad, grado):
        self.nombre =nombre
        self.edad = edad
        self.grado = edad
        
    def estudiar (self):
        print(f"El estudiante {self.nombre} esta estudiando")

        
txt_nombre = input(f"Nombre de el estudiante: ")
txt_edad= input(f"Ingrese su edad:")
txt_grado = input (f"Ingrese el grado en el que se encuentra:")

    
estudiante_1 = Estudiante(txt_nombre, txt_edad, txt_grado)
print(f"""El nombre de este estudiante es: {txt_nombre}
      Su edad es: {txt_edad}
      Su grado {txt_grado}""")

txt_estudia = input()
if txt_estudia.lower() == "estudiando":
   estudiante_1.estudiar()
else:
    print("No esta estudiando")
