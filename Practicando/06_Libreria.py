class Autor:
    def __init__ (self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
    
    def mostrar_informacion(self):
        return f"""
        Nombre: {self.nombre}
        Nacionalidad: {self.nacionalidad}"""

class Libro:
    def __init__(self,titulo, autor, año_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion
        self.disponible = True
    
    def mostrar_informacion(self):
        return f"""
        Titulo: {self.titulo}
        Autor: {self.autor.mostrar_informacion()}
        Año de publicacion: {self.año_publicacion}
        Disponibilidad: {self.disponible}"""
    
    def prestar(self):
        if self.disponible == True:
            self.disponible = False
            return f"El Libro: {self.titulo}, Se lo prestamos"
        else:
            return f"Libro ya usado"
        
    def devolver(self):
        if self.disponible == False:
            self.disponible = True
            return f"Libro actualizado, ahora esta disponible"
        else:
            return f"El Libro no encontrado"

  
class Usuario:
    def __init__ (self,nombre):
        self.nombre = nombre
        self.libros_prestados = []
    
    def prestamo_libro (self,libro):
        if libro.disponible:
            libro.prestar()
            self.libros_prestados.append(libro)
            return f"Se presto el libro: {libro}"
        else:
            return f"No se encontro el libro: {libro}"
    
    def devolver_libro(self,libro):
        if libro in self.libros_prestados:
            libro.devolver()
            self.libros_prestados.remove(libro)
            return f"Libro actualizado"
        else:
            return f"Libro no encontrado"

class Biblioteca:
    def __init__ (self):
        self.libros = []
    
    def agregar_libro(self,libro):
        self.libros.append(libro)
        return f"El libro: {self.libros} se agrego"
    
    def mostrar_libros(self):
        for libro in self.libros:
            print(libro.mostrar_informacion())
    
    def prestar_libro(self,titulo,usuario):
        for libro in self.libros:
            if libro.titulo == titulo:
                return usuario.prestamo_libro(libro)
            else:
                return f"No se encontro el libro: {titulo}"
                
    def devolver_libro(self,titulo,usuario):
        for libro in self.libros:
            if libro.titulo == titulo:
                return usuario.devolver_libro(libro)
            else:
                return f"No se encontro el libro {titulo}"
                      
a1 = Autor("Gabriel García Márquez", "Colombiano")
l1 = Libro("Cien años de soledad", a1, 1967)
l2 = Libro("El otoño del patriarca", a1, 1975)

biblioteca = Biblioteca()
biblioteca.agregar_libro(l1)
biblioteca.agregar_libro(l2)

u1 = Usuario("Mateo Dominguez")
biblioteca.mostrar_libros() 

print(biblioteca.prestar_libro("Cien años de soledad", u1))
print(biblioteca.mostrar_libros())

print(biblioteca.devolver_libro("Cien años de soledad", u1))
print(biblioteca.mostrar_libros())