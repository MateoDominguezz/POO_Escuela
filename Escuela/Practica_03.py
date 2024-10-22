class Fabrica ():
    def __init__ (self,llantas, color, precio):
        self.llantas = llantas
        self.color = color
        self.precio = precio
        
    def __str__(self):
        return  f"""
            Las cantidad de llantas son: {self.llantas}
            Color: {self.color}
            El precio es: {self.precio}"""
    
class Moto(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)
        self.llantas = llantas
        self.color = color
        self.precio = precio
        

class Auto(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)
        self.llantas = llantas
        self.color = color
        self.precio = precio

if __name__ == "__main__":
    f1 = Fabrica(50, "Negras", "200usd")
    m1 = Moto(20, "Rojo", "100usd")
    a1 = Auto(28, "Verde", "800usd")
    print(f1)
    print(m1)
    print(a1)
        
        
        