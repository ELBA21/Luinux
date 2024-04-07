class Productos:
    def __init__(self, nombre, id, precio, cantidad):
        self.nombre = nombre
        self.id = id
        self.precio = precio
        self.cantidad = cantidad
    
    #Getters
    def get_nombre(self):
        return self.nombre

    def get_id(self):
        return self.id

    def get_precio(self):
        return self.precio
    
    def get_cantidad(self):
        return self.get_cantidad
    
    #Setters
    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_id(self, id):
        self.id = id

    def set_precio(self, precio):
        self.precio = precio     
    def set_cantidad(self, cantidad):
        self.get_cantidad = cantidad