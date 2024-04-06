class Sucursal:
    def __init__(self, productos, nombre):
        self.productos = productos
        self.nombre = nombre

    def get_nombre(self, nombre):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre