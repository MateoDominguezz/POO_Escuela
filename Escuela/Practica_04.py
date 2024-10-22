class Marino():
    def hablar (self):
        return "Hola..."

class Pulpo(Marino):
    def hablar (self):
        return f"{super().hablar()} Soy un Pulpo"

class Foca(Marino):
    def __init__(self, nombre, mensaje):
        self.nombre = nombre
        self.mensaje = mensaje
    
    def hablar_mensaje(self):
        return f"""
        {super().hablar()} 
        Soy una foca con el nombre: {self.nombre}
        Este es mi mensaje: {self.mensaje}"""

if __name__ == "__main__":
    m1 = Marino()
    print(m1.hablar())
    
    p1 = Pulpo()
    print(p1.hablar())
    
    f1 = Foca("Jose","Cuidenme que estoy en peligro de extinción")
    print(f1.hablar_mensaje())