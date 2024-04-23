import random
import string

class Productos:
    def __init__(self, nombre, id, precio_venta, precio_compra, stock):
        self.nombre = nombre
        self.id = id
        self.precio_venta = precio_venta
        self.precio_compra = precio_compra
        self.stock = stock
    
    #Getters
    def get_nombre(self):
        return self.nombre

    def get_id(self):
        return self.id

    def get_precio_venta(self):
        return self.precio_venta

    def get_precio_compra(self):
        return self.precio_compra

    def get_stock(self):
        return self.stock
    
    #Setters
    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_id(self, id):
        self.id = id

    def set_precio_venta(self, precio_venta):
        self.precio_venta = precio_venta     

    def set_precio_compra(self, precio_compra):
        self.precio_compra = precio_compra

    def set_stock(self, stock):
        self.stock = stock

    def set_autoid(self): #crea una id "unica" para cada objeto basado en su nombre (4 ints y dos chars mayusculas)
        random.seed(self.nombre)
        a = random.randint(1000, 9999)
        # random.seed(self.precio) # como el precio puede cambiar decidi hacer que el id solo tenga de semilla el nombre
        b = ''.join(random.choices(string.ascii_uppercase, k=2))
        self.id = str(a) + "-" + b

    def actualizar_stock(self, stock_update): #actualiza sumando y restando al stock existente
        self.stock = self.stock + stock_update
