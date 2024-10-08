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

class Prestamo:
    def __init__(self):
        self.prestamos = []

    def registrar_prestamo(self, libro, usuario):
        if libro.get_disponible():
            fecha_prestamo = input("Ingrese la fecha de prestamo: ")
            self.prestamos.append(f"Usuario: {usuario}, Libro: {libro}, Fecha de prestamo: {fecha_prestamo}")
            libro.marcar_prestado()
            print("Prestamo registrado")
        else:
            print("El libro ya se encuentra prestado")

    def registrar_devolucion(self, libro):
        for prestamo in self.prestamos:
            if prestamo["Libro"] == libro:
                fecha_devolucion = input("Ingrese la fecha de devolución: ")
                prestamo["Fecha de devolución"] = fecha_devolucion
                libro.marcar_disponible()
                print("Devolucion registrada")
                break
        else:
            print("El libro no se encuentra prestado")

    libro1 = Libro(1, "El principito", "Antonio Machado")
    libro2 = Libro(2, "Cien años de soledad", "Gabriel Garcia Marquez")
    libro3 = Libro(3, "El señor de los anillos", "JRR Tolkien")
    libro4 = Libro(4, "El resplandor", "Stephen King")
    libro5 = Libro(5, "Harry Potter y la piedra filosofal", "J.K. Rowling")

    

