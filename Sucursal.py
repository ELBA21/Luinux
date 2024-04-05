class Sucursal:
    def __init__(self, productos, nombre):
        self.productos = productos
        self.nombre = nombre

    def get_nombre(self, nombre):
        return self.nombre

    def __set_nombre__(self, nombre):
        self.nombre = nombre