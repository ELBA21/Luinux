from Productos import Productos

class Sucursal:
    def __init__(self, nombre):
        self.productos = []
        self.nombre = nombre

    def get_nombre(self, nombre):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def agregar_productos(self, nombre_producto, precio_producto, stock_producto):
        globals()[str(nombre_producto) + "_objeto"] = Productos(nombre_producto, None, precio_producto, stock_producto)
        globals()[str(nombre_producto) + "_objeto"].set_autoid
        self.productos.append(globals()[str(nombre_producto) + "_objeto"])

    def get_productos(self, value):
        return self.productos[value]