from Productos import Productos
from tkinter import *

class Sucursal:
    def __init__(self, nombre):
        self.productos = {}
        self.nombre = nombre

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def agregar_productos(self, nombre_producto, precio_venta, precio_compra, stock_producto):
        id = Productos.generar_id(nombre_producto)
        print(id)
        x = False
        for _, producto in self.productos.items(): #este for es para que no se cree un segundo objeto con el mismo nombre 
            if nombre_producto == producto.get_nombre():
                print("Promedio precio ponderado")
                precio_final = ((producto.get_stock()*producto.get_precio_venta())+(stock_producto*precio_compra))/(producto.get_stock()+stock_producto)
                producto.set_precio_venta(int(precio_final))
                producto.actualizar_stock(stock_producto)
                x = True # si x es verdadera no se creara un objeto y se aplicara la funcion del precio
                break
        if x == False: # si x sigue siendo false se creara un objeto
            print("Producto nuevo")
            self.productos[id] = Productos(nombre_producto, id, precio_venta, precio_compra, stock_producto)
            

    def eliminar_producto(self, id):
        self.productos.pop(id)

    def get_producto(self, id):
        return self.productos[id]
        # return self.productos[id]

    def get_tamano(self): #retorna el tamano de la lista
        return len(self.productos)
    
    def to_dict(self):
        return {
            "nombre": self.nombre,
            "productos": {producto.get_id(): producto.to_dict() for producto in self.productos.values()}
        }