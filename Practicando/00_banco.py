#Crea un sistema simple que permita manejar cuentas bancarias con las siguientes 
# funcionalidades:
#Crear una cuenta bancaria con un número de cuenta y un saldo inicial.
#Permitir depositar dinero en la cuenta.
#Permitir retirar dinero de la cuenta, asegurándose de que no se pueda retirar más del saldo disponible.
#Mostrar el saldo de la cuenta.
#Requisitos del sistema:
#Clase CuentaBancaria:
#Atributos:
#numero_cuenta: Número de cuenta de la cuenta bancaria.
#saldo: Saldo disponible en la cuenta.
#Métodos:
#depositar(cantidad): Añade una cantidad al saldo de la cuenta.
#retirar(cantidad): Resta una cantidad del saldo si hay fondos suficientes.
#mostrar_saldo(): Muestra el saldo actual de la cuenta.

class CuentaBancaria:
    def __init__(self,numero_cuenta, saldo):
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo
        
    def depositar(self, cantidad):
        self.saldo +=cantidad
        return f"Se han depositado: {cantidad}$,su saldo actual: {self.saldo}"
    
    def retirar (self,cantidad):
        if cantidad <= self.saldo:
            self.saldo -=cantidad
            return  f"Has retirado:{cantidad} y su saldo actual es {self.saldo}"
        else:
            return f"Saldo insuficiente"
    
    def mostrar (self):
        return f"""
        Su numero de cuenta: {self.numero_cuenta}
        Su saldo es de: {self.saldo}"""
        
c1 = CuentaBancaria("123456789", 1000)

print(c1.depositar(500))
print(c1.retirar(300))
print(c1.mostrar())