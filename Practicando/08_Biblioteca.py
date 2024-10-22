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
    
    def buscar_libros_por_autor(self, autor):
        libros_encontrados = []
        for libro in self.libros:
            if libro.autor == autor:
                return f"Se encontro el libro: {libros_encontrados}"
            else:
             return f"No se encontro ningun libro"


    def buscar_libros_por_genero(self, genero):
        libros_encontrados = []
        for libro in self.libros:
            if libro.genero == genero:
                return f"Se encontro el libro: {libros_encontrados}"
            else:
             return f"No se encontro ningun libro"
    
    def mostrar_todos_los_libros(self):
        for libro in self.libros:
            return f"""Titulo: {libro.titulo}
            Autor: {libro.autor}
            Genero: {libro.genero}"""

    def mostrar_libro(self, libro):
        if libro == libro.titulo:
            return f"""Título: {libro.titulo}
            Autor: {libro.autor}
            Genero: {libro.genero}"""
        else:
            return f"No se encontro ningun libro con el nombre: {libro}"
        

        