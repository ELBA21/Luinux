import random
import string

class Productos:
    def __init__(self, nombre, id, precio, stock):
        self.nombre = nombre
        self.id = id
        self.precio = precio
        self.stock = stock
    
    #Getters
    def get_nombre(self):
        return self.nombre

    def get_id(self):
        return self.id

    def get_precio(self):
        return self.precio
    
    def get_stock(self):
        return self.stock
    
    #Setters
    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_id(self, id):
        self.id = id

    def set_precio(self, precio):
        self.precio = precio     

    def set_stock(self, stock):
        self.stock = stock

    def set_autoid(self): #crea una id "unica" para cada objeto basado en su precio y nombre (4 ints para el nombre y dos chars para el precio)
        random.seed(self.nombre)
        a = random.randint(1000, 9999)
        random.seed(self.precio)
        b = ''.join(random.choices(string.ascii_uppercase, k=2))
        self.id = str(a) + "-" + b

    def actualizar_stock(self, stock_update): #actualiza sumando y restando al stock existente
        self.stock = self.stock + stock_update
