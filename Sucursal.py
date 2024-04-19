from Productos import Productos

class Sucursal:
    def __init__(self, nombre):
        self.productos = []
        self.nombre = nombre

    def get_nombre(self, nombre):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def agregar_productos(self, nombre_producto, precio_producto, precio_compra_producto, stock_producto):
        x = False
        for producto in self.productos:
            if producto.get_nombre() == nombre_producto:
                print("precio costo")
                precio_final = ((producto.get_stock()*producto.get_precio_venta())+(stock_producto*precio_compra_producto))/(producto.get_stock()+stock_producto)
                producto.set_precio_venta(int(precio_final))
                producto.actualizar_stock(stock_producto)
                x = True
        if x == False:
            globals()[str(nombre_producto) + "_objeto"] = Productos(nombre_producto, None, precio_producto, precio_compra_producto, stock_producto)
            globals()[str(nombre_producto) + "_objeto"].set_autoid
            self.productos.append(globals()[str(nombre_producto) + "_objeto"])
            

    def get_productos(self, value):
        return self.productos[value]

    def eleminar_productos(self, value):
        self.productos.pop(value)

    def get_tamano(self):
        return len(self.productos)