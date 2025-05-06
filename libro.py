class Libro:
    def __init__(self, id_libro, titulo, autor, editorial, categoria, precio, stock):
        self.id_libro = id_libro
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
        self.categoria = categoria
        self.precio = precio
        self.stock = stock
        
        def mostrar_info(self):
            return f"ID: {self.id_libro}, Titulo: {self.titulo}, Autor: {self.autor}, Editorial: {self.editorial}, Categoria: {self.categoria}, Precio: {self.precio}, Stock: {self.stock}"
    def actualizar_stock(self, cantidad):
        self.stock += cantidad
    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio
        
