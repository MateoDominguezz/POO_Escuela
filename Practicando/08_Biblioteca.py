class Libro():
    def __init__ (self, titulo, autor, genero):
        self.__titulo = titulo
        self.__autor = autor
        self.__genero = genero
        
    @property
    def titulo (self):
        return self.__titulo
    
    @titulo.setter
    def titulo (self,titulo):
        self.__titulo = titulo
    
    @property
    def autor(self):
        return self.__autor
    
    @autor.setter
    def autor(self, autor):
        self.__autor = autor
        
    @property
    def genero(self):
        return self.__genero
    
    @genero.setter
    def genero(self, genero):
        self.__genero = genero

class Biblioteca():
    def __init__(self, nombre):
        self.__nombre = nombre
        self.libros= []
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def genero(self, nombre):
        self.nombre =nombre

    def agregar_libro(self,libro1):
        self.libros.append(libro1)
        return f"El libro: {libro1}, se añadio a la biblioteca"

    def buscar_libro_autor(self, autor):
        for libro in self.libros:
            if libro.autor == autor:
                return f"Tu libro encontrado por autor es: {libro.mostrar_libro()}"
        return "No se encontraron ningun libro con ese autor"

    def buscar_libros_genero(self, genero):
        for libro in self.libros:
            if libro.genero == genero:
                return f"Tu libro es: {libro.mostrar_libro()}"
        return "No se encontraro ningun libro, con ese genero"
    
    def mostrar_todos_los_libros(self):
        for libro in self.libros:
            print (f"""Titulo: {libro.titulo}
            Autor: {libro.autor}
            Genero: {libro.genero}""")

    def mostrar_libro(self, libro):
        if libro == libro.titulo:
            return f"""Título: {libro.titulo}
            Autor: {libro.autor}
            Genero: {libro.genero}"""
        else:
            return f"No se encontro ningun libro con el nombre: {libro}"

l1 = Libro("Cien Años de Soledad", "Gabriel Garcia Marquez", "Realismo magico")
l2 = Libro("1984", "George Orwell", "Distopia")
l3 = Libro("El Hobbit", "J.R.R. Tolkien", "Fantasia")
l4 = Libro("El Principito", "Antoine de Saint-Exupery", "Ficcion")

mi_biblioteca = Biblioteca("Biblioteca de Olavarria")

mi_biblioteca.agregar_libro(l1)
mi_biblioteca.agregar_libro(l2)
mi_biblioteca.agregar_libro(l3)
mi_biblioteca.agregar_libro(l4)

print(mi_biblioteca.mostrar_todos_los_libros())

        

        