#Realizar una clase llamada Persona con atributos privados: nombre, edad, DNI, sexo, peso y altura.
#Crea métodos (getters y setters) para acceder y
#modificar todos los atributos.
#Por defecto, todos los atributos menos el DNI tendrán valores por defecto según su tipo
#(0 números, cadena vacía para String, etc.).
#Sexo será mujer por defecto.
#La clase deberá tener los siguientes métodos:
#calcularIMC(): calcula el índice de masa corporal de la persona (peso en kg/(altura^2 en m))
#valorarPesoCorporal() devuelve un -1 si está por debajo de su peso ideal, un 0 si está en su peso ideal y un 1 si tiene sobrepeso.
#Sobrepeso se define como IMC> 25 y se considera que se está por debajo del peso ideal si IMC <18.
#esMayorDeEdad(): indica si es mayor de edad, devuelve un booleano.
#__str__() devuelve toda la información de la persona como una cadena de
#caracteres.
#generaDNI(): genera un numero aleatorio de 8 cifras que será el DNI de lapersona.
#Este método no será visible desde el exterior. Este método deberá invocarse desde cualquier constructor para generar el DNI.
#Métodos set y get de cada parámetro, excepto de DNI, que sólo tendrá get
import random
class Persona:
    def __init__(self, nombre = "",edad = 0 ,sexo = "mujer", peso = 0,altura= 0):
        self._nombre = nombre
        self._edad = edad
        self._DNI = self._generarDNI()
        self._sexo = sexo
        self._peso = peso
        self._altura = altura
    
    @property
    def nombre (self):
        return self._nombre
    @nombre.setter
    def nombre_set(self, nombre):
        self._nombre= nombre
        
    @property
    def edad(self):
        return self._edad
    @edad.setter
    def edad_set(self,edad):
        self._edad = edad
        
    @property
    def DNI (self):
        return self._DNI
    
    @property
    def sexo (self):
        return self._sexo
    @sexo.setter
    def sexo_set (self,sexo):
        self._sexo = sexo
    
    @property
    def peso (self):
        return self._peso
    @peso.setter
    def peso_set(self, peso):
        self._peso= peso

    @property
    def altura (self):
        return self._altura
    @altura.setter
    def altura_set(self,altura):
        self._altura= altura        

    def calcularIMC(self):
        return (self._peso / (self._altura ** 2))   

    def valorarPesoCorporal (self):
        imc = self.calcularIMC()
        if imc < 18:
            return -1
        elif imc > 25:
            return 1
        return 0
            
    def mayoredad (self):
        return self._edad >= 18

    def __str__(self):
        return f"""
              Nombre = {self._nombre}
              Edad = {self._edad}
              DNI = {self._DNI}
              Sexo = {self._sexo}
              Peso = {self._peso}
              Altura = {self._altura}
              """
      
    def _generarDNI (self):
        return random.randint(10000000, 99999999)

pj1 = Persona("dasdas", 12, "asdaasdas", 20, 120)

pj1.nombre_set =("Mateo")
pj1.edad_set = (20)
pj1.sexo_set = ("Hombre")
pj1.peso_set = (64)
pj1.altura_set = (1.72)

print (pj1)
print(f"Su IMC es de: {pj1.calcularIMC()}")
print(f"Valoracion de su peso corporal: {pj1.valorarPesoCorporal()}")
print(f"Usted es mayor de edad ?: {pj1.mayoredad()}")