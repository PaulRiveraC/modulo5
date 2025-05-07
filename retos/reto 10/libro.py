class Libro:
    def __init__(self,titulo, autor, paginas):
        self.titulo=titulo
        self.autor=autor
        self.paginas=paginas

    libros=[]

    # Metodo de intancia
    def mostrar_info(self):
        print(f"Título: {self.titulo}, Autor: {self.autor}, Número Páginas: {self.paginas}")

    # Método estático
    @staticmethod
    def es_grande(paginas):
        return f"Es grande: {True}" if paginas>300 else f"Es grande: {False}"
        
    #Método de clase
    @classmethod
    def total_libros(cls):
        return len(cls.libros)

