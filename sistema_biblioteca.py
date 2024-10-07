class Libro:
    def __init__(self, id, titulo, autor):
        self.__id = id
        self.__titulo = titulo
        self.__autor = autor
        self.__disponible = True

    def get_id(self):
        return self.__id

    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor
    
    def marcar_prestado(self):
        self.__disponible = False

    def marcar_disponible(self):
        self.__disponible = True


