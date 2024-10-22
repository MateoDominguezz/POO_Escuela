class Calculadora():
    def __init__(self, op1, op2):
        self.op1 = op1
        self.op2 = op2
        
    def suma(self):
        return f"La suma dio: {self.op1 + self.op2}"
    
    def resta (self):
        return f"La resta dio: {self.op1 - self.op2}"
    
    def multiplicacion (self):
        return f"La multiplicacion dio: {self.op1 * self.op2 }"
    
    def division (self):
        if self.op1 == 0 or self.op2 == 0:
            return f"La division no se pudo hacer"
        else:
            return f"La division dio: {self.op1 / self.op2}"
    
    def __str__(self):
        return f"""
        {self.suma()}
        {self.resta()}
        {self.multiplicacion()}
        {self.division()}"""

op1 = int(input("Inregese el primer numero: "))
op2 = int(input("Inregese el segundo numero: "))
c1 = Calculadora(op1,op2)
print(c1)
